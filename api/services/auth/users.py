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
from api.core.utils import *

class User(Model):
    _properties = {
        'user_id': Property('.', Type.uid),
        'username': Property('.', Type.string),
        'password': Property('.', Type.string),
        'first': Property('.', Type.string),
        'last': Property('.', Type.string),
        'privillege': Property('.', Type.integer)
    }

class Users(Resource):
    model = User

    def on_post_collection(self, req, res):

        print('in here')

        model = self.new_model(None, req)

        model.set_map()

        model.password = Utils.hash(model.password)

        model.save()

        res.media = model.serialize()
        res.status = falcon.HTTP_CREATED

        if model.is_error_state():
            res.status = falcon.HTTP_BAD_REQUEST
        return res
