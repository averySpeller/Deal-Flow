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

class Contact(Model):
    _properties = {
        'contact_id': Property('ContactID', Type.uid),
        'organization_id': Property('OrganizationID', Type.uid),
        'avatar': Property('.', Type.string, hidden=True),
        'first': Property('First', Type.string),
        'last': Property('Last', Type.string),
        'title': Property('Title', Type.string),
        'email': Property('Email', Type.string),
        'phone1': Property('Phone1', Type.string),
        'phone2': Property('Phone2', Type.string),
        'website': Property('Website', Type.string),
        'notes': Property('Notes', Type.string, encrypt=True),
        'skill1': Property('.', Type.string),
        'skill2': Property('.', Type.string),
        'skill3': Property('.', Type.string),
        'skill4': Property('.', Type.string),
        'skill5': Property('.', Type.string)
    }


class Contacts(Resource):
    model = Contact

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
