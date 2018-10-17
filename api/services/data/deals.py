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
from api.core.resource import *

class Deals(Resource):

    data = [
        { 'dealID': 1 },
        { 'dealID': 2 },
        { 'dealID': 3 },
    ]


    def on_get(self, req, res, dealID):
        no_error = False
        for item in self.data:
            if item['dealID'] == int(dealID):
                res.media = item
                no_error = True
                break
        if not no_error:
            res.status = falcon.HTTP_404


    def on_get_collection(self, req, res):
        res.status = falcon.HTTP_200
        res.media = self.data
