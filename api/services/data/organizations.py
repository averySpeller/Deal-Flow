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

class Organizations(Resource):

    data = [
        { 'organizationID': 1 },
        { 'organizationID': 2 },
        { 'organizationID': 3 },
    ]


    def on_get(self, req, res, organizationID):
        no_error = False
        for item in self.data:
            if item['organizationID'] == int(organizationID):
                res.media = item
                no_error = True
                break
        if not no_error:
            res.status = falcon.HTTP_404


    def on_get_collection(self, req, res):
        res.status = falcon.HTTP_200
        res.media = self.data
