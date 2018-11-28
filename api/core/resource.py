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
import re
from inspect import signature
from api.core.model import *
from api.core.srql import *


class Resource(object):

    def __init__(self):
        pass

    def new_model(self, id, req):
        return self.__class__.model(id=id, parser=SRQLParser(request=req))

    def new_model_collection(self, req):
        return ModelCollection(model=self.__class__.model, parser=SRQLParser(request=req))

    def default_response(self, req, res, id=None):
        # build the models HACK: we don't really want to check for POST
        #  but we also dont want to move the model instantiation into the functions.
        if id or req.method == 'POST':
            model = self.new_model(id, req)
        else:
            model = self.new_model_collection(req)

        def _default_get(req, res, model):
            res.media = model.serialize()
            res.status = falcon.HTTP_OK

            if model.is_error_state():
                res.status = falcon.HTTP_NOT_FOUND
                res.media = None
            return res

        def _default_put(req, res, model):
            # Update the model with the new data
            model.set_map()
            model.save()

            res.media = model.serialize()
            res.status = falcon.HTTP_OK

            if model.is_error_state():
                res.status = falcon.HTTP_NOT_FOUND
            return res

        def _default_post(req, res, model):
            # Create the model object using json payload
            model.set_map()
            model.save()

            res.media = model.serialize()
            res.status = falcon.HTTP_CREATED

            if model.is_error_state():
                res.status = falcon.HTTP_BAD_REQUEST
            return res

        def _default_delete(req, res, model):
            success = model.delete()
            res.status = falcon.HTTP_NO_CONTENT

            if not success or model.is_error_state():
                res.status = falcon.HTTP_BAD_REQUEST
            return res

        # do some stuff with the models based on the resource verb
        supported_methods = {
            'GET': _default_get,
            'PUT': _default_put,
            'POST': _default_post,
            'DELETE': _default_delete
        }

        # handle the given HTTP method
        res = supported_methods[req.method](req, res, model)

        # print('method')
        # print(req.method)

        return res

    def build_response(self, res, model):
        # set the response
        res.media = model.serialize()
        res.status = falcon.HTTP_404

    def definitions(self):
        pass

    #
    # WARNING: Beware, this is some pretty pseudo magic
    #             meta code.
    def fetch_endpoints(self):

        # Get the name of the calling resource instance
        resource_name = type(self).__name__.lower()

        # Define the map of endpoints
        resource_endpoint_list = []

        # Get the function list of the calling resource
        for function in dir(self):
            if not re.search(r'on_(get|put|post|delete)+', function, re.I): continue

            if re.search(r'on_(get|put|post|delete)+_collection', function, re.I):
                resource_type = 'collection'
                ep = '/' + resource_name
            else:
                resource_type = 'instance'

                # Get the function signature
                sig = signature(getattr(self, function))

                # Retrieve the name of the resource id
                ep = '/' + resource_name + '/{' + str(sig).split(',')[-1][:-1].strip() + '}'

            # print(function)
            # print(resource_type)
            # print(ep)
            # print()

            continue_flag = False
            # Check to see if the endpoint already exists
            for ep_map in resource_endpoint_list:
                if ep_map['endpoint'] == ep:
                    continue_flag = True

            if continue_flag: continue

            # Add the endpoint to the endpoint mappings
            resource_endpoint_list.append(
                { 'endpoint': ep, 'type': resource_type }
            )
        return { 'endpoints': resource_endpoint_list }
