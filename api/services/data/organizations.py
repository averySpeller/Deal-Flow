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

class Organization(Model):
    _properties = {
        'organization_id': Property('OrganizationID', Type.uid),
        'name': Property('Name', Type.string),
        'stock_symbol': Property('StockSymbol', Type.string),
        'logo': Property('Logo', Type.string, hidden=True),
        'vision': Property('Vision', Type.string),
        'revenue_model': Property('RevenueModel', Type.string),
        'revenue': Property('Revenue', Type.string),
        'valuation': Property('Valuation', Type.string),
        'phone1': Property('Phone1', Type.string),
        'phone2': Property('Phone2', Type.string),
        'line1': Property('line1', Type.string),
        'line2': Property('line2', Type.string),
        'city': Property('city', Type.string),
        'state': Property('state', Type.string),
        'country': Property('state', Type.string),
        'postal': Property('postal', Type.string),
        'website': Property('Website', Type.string),
        'notes': Property('Notes', Type.string, encrypt=True)
    }

# class OrganizationRelationships(Relationships):
#     contacts = Document(Contacts, Relation.many_to_one)


class Organizations(Resource):
    model = Organization
    # relationships = OrganizationRelationships

    def on_post_collection(self, req, res):
        res = self.default_response(req, res)

    def on_get(self, req, res, organization_id):
        res = self.default_response(req, res, organization_id)

    def on_get_collection(self, req, res):
        res = self.default_response(req, res)

    def on_put(self, req, res, organization_id):
        res = self.default_response(req, res, organization_id)

    def on_delete(self, req, res, organization_id):
        res = self.default_response(req, res, organization_id)
