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

class TagMapping(Model):
    _properties = {
        'tag_mapping_id': Property('', Type.uid),
        'tag_id': Property('', Type.string),
        'contact_id': Property('', Type.string),
        'organization_id': Property('', Type.string)
    }

class TagMappings(Resource):
    model = TagMapping

    def on_post_collection(self, req, res):
        res = self.default_response(req, res)

    def on_get(self, req, res, tag_mapping_id):
        res = self.default_response(req, res, tag_mapping_id)

    def on_get_collection(self, req, res):
        res = self.default_response(req, res)

    def on_put(self, req, res, tag_mapping_id):
        res = self.default_response(req, res, tag_mapping_id)

    def on_delete(self, req, res, tag_mapping_id):
        res = self.default_response(req, res, tag_mapping_id)
