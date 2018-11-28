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

class Tag(Model):
    _properties = {
        'tag_id': Property('', Type.uid),
        'tag_name': Property('', Type.string),
        'tag_color': Property('', Type.string)
    }

class Tags(Resource):
    model = Tag

    def on_post_collection(self, req, res):
        res = self.default_response(req, res)

    def on_get(self, req, res, tag_id):
        res = self.default_response(req, res, tag_id)

    def on_get_collection(self, req, res):
        res = self.default_response(req, res)

    def on_put(self, req, res, tag_id):
        res = self.default_response(req, res, tag_id)

    def on_delete(self, req, res, tag_id):
        res = self.default_response(req, res, tag_id)
