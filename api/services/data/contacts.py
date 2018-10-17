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
from api.core.model import *

class Contact(Model):
    _properties = {
        'contact_id': Property('ContactID', Type.uid),
        'first': Property('First', Type.string),
        'last': Property('Last', Type.string),
        'email': Property('Email', Type.string),
        'phone1': Property('Phone1', Type.string),
        'phone2': Property('Phone2', Type.string),
        'website': Property('Website', Type.string),
        'notes': Property('Notes', Type.string),
        'json_store': Property('JSONStore', Type.string)
    }


class Contacts(Resource):
    model = Contact

    def on_post(self, req, res):
        res = self.default_response(req, res)

    def on_get(self, req, res, contactID):
        res = self.default_response(req, res, contactID)

    def on_get_collection(self, req, res):
        res = self.default_response(req, res)
