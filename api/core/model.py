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

class Model:

    def __init__(self, id=None, parser=None, auto_save=False, from_map=None):
        print('instantiated ' + type(self).__name__)

        self._dao = DAO(relation=type(self).__name__)

        self._id = id
        self._documents = {}
        self._properties = {}
        self._parser = parser
        self._error_state = False
        self._auto_save = auto_save
        self._relation = type(self).__name__

        if from_map: self.set_map(from_map)


    # -------------------------------------------
    # Purpose: Override the default get accessor in the model class
    #           to search the class property values.
    # Passed-in: Instance, var name.
    def __getattr__(self, name):
        if name in (self.__class__._properties.keys()):
            # Get the document name from the class properties
            doc = self.__class__._properties[name].get_document()

            # HACK: ???  We dont like to shoot first
            try:                instance_document = self._documents[doc]
            except KeyError:    instance_document = None

            # If the document is NOT in read_sync or DNE, we need to load from the DB
            # TODO: I really dont like this... Maybe clean me up by creating lazy loaded Document models
            if instance_document is None or instance_document['read_sync'] is False or name not in self._properties and self._id is not None:
                print('would hit db for %s' % (name,))
                results = self._dao.read(doc, self._id)
                if results == None:
                    self._error()
                    print('no read')
                else:
                    self.set_map(results)

                # Update the document model
                try:
                    document = self._documents[doc]
                    document['read_sync'] = True
                except KeyError:
                    self._documents[doc] = {
                        'read_sync': True,
                        'write_sync': True,
                        'fields' : []
                    }
            try:
                return self._properties[name]
            except KeyError:

                self._properties[name] = None
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

            # Get the document name from the class properties
            doc = self.__class__._properties[name].get_document()

            # Set the property
            self._properties[name] = value

            # Invalidate the document model
            try:
                document = self._documents[doc]
                document['read_sync'] = True
                document['write_sync'] = False
                if name not in document['fields']: document['fields'].append(name)
            except KeyError:
                self._documents[doc] = {
                    'read_sync': True,
                    'write_sync': False,
                    'fields' : [ name ]
                }
        else:
            if name[0] is not '_':
                print('Property Not Found! Implement me')
                self._error()
                # raise ValueError
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


    def set_map(self, map=None):
        # Parse a given map or fetch it from the request
        if not map:
            map = self._parser.get_payload()

        for key,value in map.items():
            print('setting %s to %s' % (key,value))
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
        for doc in self._documents.keys():

            # If the document model is out of sync with the db.. write
            if self._documents[doc]['write_sync'] is False:

                payload = {}
                for field in self._documents[doc]['fields']:
                    payload[field] = self._properties[field]

                if self._id is not None:
                    # if updating
                    self._dao.update(doc, self._id, payload)
                else:
                    # if creating
                    result = self._dao.create(doc, payload)
                    self.set_map(result)

                # TODO: REDO document model


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
        self._dao.bulk_read(self._relation)

        # self._create_model()
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



class Property:

    def __init__(self, name, type, relation=None, document=None, **kwargs):
        print('registering property: ' + name)
        self.document = document
        self.source = None

        self.description = None
        self.format = None
        self.options = None

    def get_document(self):
        return self.document

    def validate(self):
        return True

class Type:
    uid = ''
    integer = 'a'
    string = ''
    boolean = ''
    datetime = ''
    enum = ''


# TODO: Needs a mess of work on the relation types (self(recurse), 1..1, 1..N, M..N)
class DAO:

    def __init__(self, relation=None, bulk=False):
        self._relation = relation
        self._db = DBWrapper( DBExplodeOnError() )
        self._is_bulk = bulk
        self.result_buffer = []

    def fetch_buffer(self):
        return self.result_buffer

    def create(self, relation, payload):
        def format_insert(relation, keys, values):
            query_string = 'insert into ' + relation + ' ('

            cnt = 0
            for key in keys:
                if cnt == len(keys) - 1:
                    query_string = query_string + key +') values ('
                else: query_string = query_string + key + ','
                cnt = cnt + 1

            cnt = 0
            for value in values:
                if cnt == len(keys) - 1:
                    query_string = query_string + '%s)'
                else: query_string = query_string + '%s,'
                cnt = cnt + 1

            return query_string

        if relation is None:
            relation = self._relation

        # Start a transaction
        self._db.begin_transaction()

        q = format_insert(relation, payload.keys(), payload.values())
        self._db.query(q, (*payload.values(),))
        self._db.commit()

        # Lookup the record to obtain the id
        self._db.query('select * from ' + relation +' order by ' + relation + '_id desc limit 1')

        record = self._db.fetch_one()
        self._db.end_transaction()

        return record

    def read(self, relation, id=None):
        if relation is None:
            relation = self._relation

        self._db.query('select * from ' + relation + ' where ' + relation + '_id = %s limit 1', (id))
        return self._db.fetch_one()

    def update(self, relation, id, payload):
        def format_update(relation, keys, id):
            query_string = 'update ' + relation + ' set '

            cnt = 0
            for key in keys:
                if cnt == len(keys) - 1:
                    query_string = query_string + key + ' = %s where ' + relation + '_id = ' + id
                else: query_string = query_string + key + ' = %s,'
                cnt = cnt + 1

            return query_string
        if relation is None:
            relation = self._relation

        query = format_update(relation, payload.keys(), id)

        self._db.query(query, (*payload.values(),))

    def delete(self, relation, id):
        self._db.query('delete from ' + relation + ' where ' + relation + '_id = %s', (id,))
        return self._db.cursor.rowcount > 0 and not self._db.error()

    def bulk_create(self): pass

    def bulk_read(self, relation, page_size=30, current_page=1):
        if relation is None:
            relation = self._relation

        offset = (current_page - 1) * page_size

        self._db.query('select * from ' + relation + ' limit ' + str(offset) + ', ' + str(page_size))

        self.result_buffer = self._db.fetch_all()

    def bulk_update(self): pass

    def bulk_delete(self): pass
