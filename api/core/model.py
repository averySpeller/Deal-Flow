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

    # data = [
    #     'contact': [
    #         { 'contactID': 10, 'first': 'Bobby', 'Last':'Joe' },
    #         { 'contactID': 11, 'first': 'Avery', 'Last':'Speller' },
    #         { 'contactID': 12, 'first': 'Kevin', 'Last':'Prince' }
    #     ],
    #     'contactorganization': [
    #         { 'contactorganizationid': 1, 'contactID': 10}
    #     ]
    # ]

    def __init__(self, id=None, parser=None):
        self._dao = DAO()

        self._id = id
        self._documents = {}
        self._properties = {}
        self._parser = parser

        print('created ' + type(self).__name__)


    def __getattr__(self, name):
        if name in (self.__class__._properties.keys()):
            try:
                return self._properties[name]
            except KeyError:
                return None
        else:
            return super().__getattribute__(name)


    def __setattr__(self, name, value):
        if name in (self.__class__._properties.keys()):
            self._properties[name] = value
            # raise AttributeError("%s is an immutable attribute.")
        else:
            super().__setattr__(name, value)


    def _fetch_document(self):
        pass

    def _fetch_property(self):
        pass

    def serialize(self):
        # for attribute in self.__class__._properties.keys():
        #     getattr(self, attribute)
        return self._properties

    def response_status(self):
        pass

    def set_map(self, map):
        pass
        # foreach in map: self.attr_set(key, value)

    #
    # DANGER ZONE
    #
    def delete(self, soft=False):
        pass

    def save(self):
        pass
        # if updating

        # if creating



class ModelCollection:

    def __init__(self, model=None, parser=None):
        self._dao = DAO(bulk=True)
        self._parser = parser
        self._data_model = model
        self._model_list = []

    def _create_model():
        return self._data_model()

    def populate(dao):
        pass

    def serialize(self):
        pass



class _Document:
    pass
    # self.loaded = False
    # self.stale = True

class Property:

    def __init__(self, name, type, document=None, **kwargs):
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

    def _connect(self):
        pass
        # if not self._connection:
        #     self._connection =

    def _store_map(self, relation, map):
        pass

    def fetch_document(self):
        pass
