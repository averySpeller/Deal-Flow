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

class Deal(Model):
    _properties = {
        'deal_id': Property('.', Type.uid),
        'organization_id': Property('.', Type.uid),

        'organization': Property('.', Type.string),
        'contacts': Property('.', Type.string),

        'interest': Property('.', Type.string),
        'status': Property('.', Type.string, encrypt=True),

        'valuation': Property('.', Type.string, encrypt=True),
        'raise_type': Property('.', Type.string, encrypt=True),
        'raise': Property('.', Type.string, encrypt=True),
        'revenue': Property('.', Type.string),
        'revenue_model': Property('.', Type.string),

        'round': Property('.', Type.string, encrypt=True),

        'slide_deck': Property('.', Type.string),
        'notes': Property('.', Type.string, encrypt=True)
        'date_added': Property('.', Type.datetime),
        'date_viewed': Property('.', Type.datetime)
    }
    _documents = {
        # 'organization': Document(Organization, Relation.one_to_many)
    }


class Deals(Resource):
    model = Deal

    def on_post_collection(self, req, res):
        res = self.default_response(req, res)

    def on_get(self, req, res, deal_id):
        res = self.default_response(req, res, deal_id)

    def on_get_collection(self, req, res):
        res = self.default_response(req, res)

    def on_put(self, req, res, deal_id):
        res = self.default_response(req, res, deal_id)

    def on_delete(self, req, res, deal_id):
        res = self.default_response(req, res, deal_id)
