#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Author      : Carter Bourette
# Description : ..
#               ...
#----------------------------------------------------------------------------
#
# Use explicit package path so that modules may be imported from parent.
# As per: https://docs.python.org/3/tutorial/modules.html#packages
#
from api.core.database import *
from api.core.dao import *
from api.core.utils import *
from enum import Enum, auto
import falcon

class Relationships:
    pass

#
#   Model
#   Description: The data model.
#
#
class Model:
    class _InternalStateModel:

        def __init__(self):
            self.read_sync = False
            self.write_sync = True
            self.fields = []

        def get_fields(self):
            return self.fields

        def in_read_sync(self):
            return self.read_sync

        def in_write_sync(self):
            return self.write_sync

        def confirm_read_sync(self):
            self.read_sync = True

        def confirm_write_sync(self):
            self.write_sync = True

        def invalidate_state_with_write(self, property):
            self.write_sync = False
            if property not in self.fields:
                self.fields.append(property)

    def __init__(self, id=None, parser=None, auto_save=False, from_map=None):
        print('instantiated ' + type(self).__name__)
        self._dao = DAO(relation=type(self).__name__)

        self._id = id
        self._documents = {}
        self._properties = {}
        self._internal_state = {}
        self._parser = parser

        self._error_state = False
        self._auto_save = auto_save
        self._relation = type(self).__name__

        if from_map: self.set_map(from_map, encrypted=True)


    # -------------------------------------------
    # Purpose: Override the default get accessor in the model class
    #           to search the class property values.
    # Passed-in: Instance, var name.
    def __getattr__(self, name):
        # If the class requested the value of a property, we'll let our internal
        #  property logic fetch the value
        if name in (self.__class__._properties.keys()):
            # Get the document name from the class properties
            doc = self.__class__._properties[name].get_document()

            # Fetch the object containting the state of each internal docuemnt
            internal_model = self._internal_state.get(doc, Model._InternalStateModel() )

            # If the document state is NOT in read_sync or DNE, we need to load from the DB
            if not internal_model.in_read_sync() or name not in self._properties:

                if self._id is not None:
                    print('would hit db for %s' % (name,))

                    # Use DAL to access the database
                    results = self._dao.read(doc, self._id)

                    # Handle the db response
                    if results == None:
                        print('Not Found! id: ' + str(self._id))
                        raise falcon.HTTPNotFound()
                        # self._error()
                    else:
                        # print('sending to decryptor')
                        self.set_map(results, encrypted=True)

                    # Update the internal document state
                    internal_model.confirm_read_sync()

            # TODO: I would love to not perform this operation everytime
            #        plz fix me...
            self._internal_state[doc] = internal_model

            # Return the attribute we set to get from the properties model
            return self._properties.get(name, None)

        # Otherwise, we'll have the class handle it
        else:
            return super().__getattribute__(name)


    # -------------------------------------------
    # Purpose: Override the default set accessor in the model class
    #           to search the class property values.
    # Passed-in: Instance, var name, and property value.
    def __setattr__(self, name, value):
        # If the class requested to write the value of a property, we'll let
        #  our internal property logic set the value
        if name in (self.__class__._properties.keys()):

            # Get the document name from the class properties
            doc = self.__class__._properties[name].get_document()

            # Fetch the object containting the state of each internal docuemnt
            internal_model = self._internal_state.get(doc, Model._InternalStateModel() )

            # Set the property
            self._properties[name] = value

            # Invalidate the document model
            internal_model.invalidate_state_with_write(name)

            # TODO: I would love to not perform this operation everytime
            #        plz fix me...
            self._internal_state[doc] = internal_model
        else:
            # TODO: handle differently
            if name[0] is not '_':
                # raise KeyError
                print('Property Not Found! Implement me')
                # self._error()
            super().__setattr__(name, value)


    def _populate(self):
        for property in self.__class__._properties.keys():
            property_value = getattr(self, property)


    def serialize(self):
        # Iterate the property list and retrieve the values
        self._populate()

        # HACK: hm, we retrieve all those values just to throw away the output
        #       and populate the instance _properties.
        return self._properties


    def _error(self, title=None, msg=None):
        # TODO: Write an error document to return when the model gets serialized
        self._error_state = True


    def is_error_state(self):
        return self._error_state


    def set_map(self, map=None, encrypted=False):
        # Parse a given map or fetch it from the request
        if not map:
            map = self._parser.get_payload()

        for key,value in map.items():

            # TODO: Added this as a fail-safe for missing sync between db and code
            #        probably a better way of incorporating this in a performant way
            if self.__class__._properties.get(key) is None: continue

            # print('setting %s to %s' % (key,value))
            if encrypted and self.__class__._properties.get(key).encrypt:
                setattr(self, key, Utils.decrypt(value))
            else:
                setattr(self, key, value)


    #
    # DANGER ZONE
    #
    # TODO: More efficient document lookup??
    def delete(self, soft=False):
        relation_list = []

        for property in self.__class__._properties.keys():
            document = self.__class__._properties[property].get_document()
            if document is None: document = self._relation

            if document not in relation_list: relation_list.append(document)


        status = True
        for rel in relation_list:
            status = status and self._dao.delete(rel, self._id)

        return status


    def save(self):
        # Look through docuemnt model
        for doc in self._internal_state.keys():

            internal_state = self._internal_state.get(doc, Model._InternalStateModel() )

            # If the document model is out of sync with the db.. write
            if not internal_state.in_write_sync():
                print('not in write sync')

                payload = {}
                for field in internal_state.get_fields():
                    if self.__class__._properties.get(field).encrypt:
                        payload[field] = Utils.encrypt(self._properties[field])
                    else:
                        payload[field] = self._properties[field]

                # if updating
                if self._id is not None:

                    self._dao.update(doc, self._id, payload)
                # if creating
                else:
                    result = self._dao.create(doc, payload)
                    self.set_map(result, encrypted=True)

                internal_state.confirm_write_sync()

                # TODO: See TODO above
                self._internal_state[doc] = internal_state

#
#   ModelCollection
#   Description: ...
#
#
class ModelCollection:

    def __init__(self, model=None, parser=None):
        self._dao = DAO(bulk=True)
        self._parser = parser
        self._data_model = model
        self._model_list = []
        self._relation = self._data_model.__name__

    def _create_model(self):
        self._model_list.append(self._data_model(from_map=self._dao.fetch_from_buffer()))

    def is_error_state(self):
        pass

    def populate(self):
        print('bulk read')
        self._dao.bulk_read(self._relation, parser=self._parser)

        # create the models
        for item in self._dao.fetch_buffer():
            self._model_list.append( self._data_model(from_map=item) )


    def serialize(self):
        print('serialize the collection')
        self.populate()
        output = []

        for model in self._model_list:
            output.append(model.serialize())
        return output

#
#   Type
#   Description: ...
#
#
class Type(Enum):
    uid = auto()
    integer = auto()
    string = auto()
    boolean = auto()
    datetime = auto()
    enum = auto()
    auto = auto()

#
#   Property
#   Description: ...
#
#
class Property:

    def __init__(self, name, type, relation=None, document=None, encrypt=False, **kwargs):
        print('registering property: ' + name)
        self.document = document
        self.source = None

        self.description = None
        self.format = None
        self.options = None

        self.encrypt = encrypt

    def get_document(self):
        return self.document

    def validate(self):
        return True

#
#   Relation
#   Description: ...
#
#
class Relation(Enum):
    one_to_one = auto()
    one_to_many = auto()
    many_to_one = auto()
    many_to_many = auto()

#
#   Document
#   Description: ...
#
#
class Document:

    def __init__(self, model, relation):
        self.model = model
        self.relation = relation

    def _map_relation(self, relation):
        _map = {
            Relation.one_to_one: _handle_one_to_one,
            Relation.one_to_many: _handle_one_to_many,
            Relation.many_to_one: _handle_many_to_one,
            Relation.many_to_many: _handle_many_to_many
        }
        _map[relation]()

    def serialize(self):
        pass
