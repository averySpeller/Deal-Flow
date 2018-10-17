#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Author      : Carter Bourette
# Description : Per service router, wrap Falcon functionality.
#               ...
#----------------------------------------------------------------------------
#
# Use explicit package path so that modules may be imported from parent.
# As per: https://docs.python.org/3/tutorial/modules.html#packages
#
import falcon


class Service:

    def __init__(self, service_name):
        self.app = falcon.API(middleware=[
            # AuthMiddleware(),
            # RequireJSON(),
            # JSONTranslator(),
        ])
        self.task_manager = None
        self.service_name = service_name
        self.base_url = '/' + service_name.lower()

    def register(self, resources):
        if type(resources) != list: resources = [ resources ]

        print('registering')

        for res in resources:

            ep_map = res.fetch_endpoints()

            for ep_list in ep_map['endpoints']:
                if ep_list['type'] == 'collection':
                    self.app.add_route(ep_list['endpoint'], res, suffix='collection')
                else:
                    self.app.add_route(ep_list['endpoint'], res)
                print('Added route for ' + str(ep_list['endpoint']))
