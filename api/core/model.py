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

class Model:

    def __init__(self, id=None, parser=None, auto_save=False):
        self._dao = DAO()

        self._id = id
        self._documents = {}
        self._properties = {}
        self._parser = parser
        self._error_state = False
        self._auto_save = auto_save

        print('instantiated ' + type(self).__name__)


    # -------------------------------------------
    # Purpose: Override the default get accessor in the model class
    #           to search the class property values.
    # Passed-in: Instance, var name.
    def __getattr__(self, name):
        if name in (self.__class__._properties.keys()):
            try:
                self._fetch_document(name)
                return self._properties[name]
            except KeyError:
                return None
        else:
            return super().__getattribute__(name)


    # -------------------------------------------
    # Purpose: Override the default set accessor in the model class
    #           to search the class property values.
    # Passed-in: Instance, var name, and property value.
    def __setattr__(self, name, value):
        print('in set attr')
        if name in (self.__class__._properties.keys()):
            self._invalidate_document(name)
            self._properties[name] = value
        else:
            if name[0] is not '_':
                self._error()
                # raise ValueError
            super().__setattr__(name, value)


    def _invalidate_document(self, property):
        pass

    def _fetch_document(self, property):

        # If record is stale

            # get the records

            # Determine document
            # ...

        # Else
            # return

        # Populate the document using the DAO
        self._dao.fetch_document(document)

        pass

    def serialize(self):

        # Iterate the property list and retrieve the values
        for property in self.__class__._properties.keys():
            property_value = getattr(self, property)

        # HACK: hm, we retrieve all those values just to throw away the output
        #       and populate the instance _properties.
        return self._properties

    def _error(self, title=None, msg=None):
        # TODO: Write an error document to return when the model gets serialized
        self._error_state = True

    def is_error_state(self):
        return self._error_state

    def set_map(self, map=None):
        # Parse a given map or fetch it from the request
        if not map:
            map = self._parser.get_payload()

        print(map)

        for key,value in map.items():
            print('setting %s to %s' % (key,value))
            setattr(self, key, value)

    #
    # DANGER ZONE
    #
    def delete(self, soft=False):
        # self._dao.delete()
        pass

    def save(self):
        pass
        # self._dao.create()
        # if updating

        # if creating

class ModelCollection:

    def __init__(self, model=None, parser=None):
        self._dao = DAO(bulk=True)
        self._parser = parser
        self._data_model = model
        self._model_list = []

    def _create_model(self):
        return self._data_model()

    def populate(self, dao):
        pass

    def serialize(self):
        pass



class _Document:
    pass
    # self.loaded = False
    # self.stale = True

class Property:

    def __init__(self, name, type, relation=None, document=None, **kwargs):
        print('registering property: ' + name)

        self.document = document
        self.source = None

        self.description = None
        self.format = None
        self.options = None

    def validate(self):
        return True

class Type:
    uid = ''
    integer = 'a'
    string = ''
    boolean = ''
    datetime = ''
    enum = ''



class DAO:

    def __init__(self, bulk=False):
        self._connection = None
        self._is_bulk = bulk
        self.result_buffer = []

    def _connect(self):
        pass
        # if not self._connection:
        #     self._connection =

    def _store_map(self, relation, map):
        pass

    def fetch_from_buffer(self):
        return None if len(self.result_buffer) == 0 else self.result_buffer.pop(0)


    def create(self, relation, payload):
        pass

    def read(self, relation, id):
        pass

    def update(self, relation, id, payload):
        pass

    def delete(self, relation, id):
        pass
