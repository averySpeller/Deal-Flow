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

class RQLParser:

    def __init__(self, request=None):
        self.request = request
        self.url_query = None
        self.reserved = ['includes', 'fields', 'order', 'group', 'limit']
        self.payload = None
        # print(Utils.fetch_query_string(req))
        # print(Utils.fetch_payload(req))


    # -------------------------------------------
    # Purpose: Purpose.
    # Passed-in: (Request) the request object.
    def parse(self, req=None):

        if req:
            pass
        else:
            pass
            # self.request

        # Fetch the query string as a dictionary
        self.url_query = Utils.fetch_query_string(req)

        # Step 1: Parse all parameters with reserved words

        # Step 2: Parse all filters
        for filter in self.url_query:
            if filter in self.reserved: continue

            # Parse filters
            # Rules:
            #  - foreach filter:
            #  - split(';')
            #  - split(':')
            #  - split('.')
