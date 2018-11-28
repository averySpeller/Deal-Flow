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
from api.core.utils import *

class SRQLParser:

    def __init__(self, request=None):
        self.request = request
        self.reserved = ['includes', 'fields', 'order', 'group', 'limit', 'page']

        self.url_params = None
        self.payload = None

        self.fields = None
        self.includes = None
        self.order = None
        self.group = None
        self.limit = None
        self.filters = {}
        self.page = 1
        self.page_size = 100

        self.url_query = Utils.fetch_query_string(request)
        self.payload = Utils.fetch_payload(request)

        self.parse()


    def get_payload(self):
        return self.payload

    def serialize(self):
        return None

    # -------------------------------------------
    # Purpose: Purpose.
    # Passed-in: (Request) the request object.
    def parse(self):

        for k,v in self.url_query.items():
            if k not in self.reserved:
                self.filters[k] = v

        # Fetch the query string as a dictionary
        # self.url_query = Utils.fetch_query_string(req)

        f_list = self.url_query.get('fields', None)
        if f_list:
            self.fields = f_list
        else: self.fields = []

        # Step 1: Parse all parameters with reserved words
        # if 'word' in self.reserved:

        # TODO: Remove shoot first logic
        try:
            if int(self.url_query['page']) > 0:
                self.page = int(self.url_query['page'])
        except: pass

        # # Step 2: Parse all filters
        # for filter in self.url_query:
        #     if filter in self.reserved: continue

            # Parse filters
            # Rules:
            #  - foreach filter:
            #  - split(';')
            #  - split(':')
            #  - split('.')
