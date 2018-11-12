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
from api.core.utils import Utils

class Authenticate(Model):
    _properties = {
        'user_id': Property('.', Type.uid),
        'username': Property('.', Type.string),
        'password': Property('.', Type.string)
    }

class Auth(Resource):
    model = Authenticate

    def on_post_collection(self, req, res):
        # HACK HACK HACK-IN AWAY

        # Create an instance of the model
        model = self.new_model(None, req)

        # Load the request values into the model
        model.set_map()

        # Query the DAL directly to grab the requested user
        model._dao._db.query('select * from user where username = %s limit 1', (model.username),)

        result = model._dao._db.fetch_result()

        res.status = falcon.HTTP_401
        if result and Utils.verify(model.password,result['password']):
            res.media = { 'type': 'access', 'token': Utils.jwt_encode({'some_payload': 'payload'}) }
            res.status = falcon.HTTP_OK
        return res
