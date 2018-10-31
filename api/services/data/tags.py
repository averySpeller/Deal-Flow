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
        'tag_id': Property(Type.uid),
        'name': Property(Type.string),
    }

    _documents = {
        'tag_mapping': Document(relation.many_to_many, auto_load=True)
    }

class TagMapping(Model):
    _properties = {
        'tag_mapping_id': Property('.', Type.uid)
    }

    _documents = {
        'organization': Document(relation.one_to_many)
        'contact': Document(relation.one_to_many)
    }



class Tags(Resource):
    model = Tag

    def on_post_collection(self, req, res):
        res = self.default_response(req, res)

    def on_get(self, req, res, contact_id):
        res = self.default_response(req, res, contact_id)

    def on_get_collection(self, req, res):
        res = self.default_response(req, res)

    def on_put(self, req, res, contact_id):
        res = self.default_response(req, res, contact_id)

    def on_delete(self, req, res, contact_id):
        res = self.default_response(req, res, contact_id)
