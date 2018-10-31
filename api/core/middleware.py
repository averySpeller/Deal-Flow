import jwt
import falcon
from api.core.utils import *

# class NegotiationMiddleware(object):
#     def process_request(self, req, resp):
#         resp.content_type = req.accept

class AuthMiddleware(object):

    def process_request(self, req, resp):
        if req.path == '/auth':
            print('in excepted ep')
            return
        else:
            print('required auth')
            print(req.path)

        token = req.get_header('Authorization')

        # parse out token from bearer
        try:
            token = token.split(' ')[1]
        except:
            pass

        challenges = ['Token type="JWT"']

        # Check to see the user has provided a token
        if token is None:
            description = ('Please provide an auth token '
                           'as part of the request.')
            raise falcon.HTTPUnauthorized('Auth token required',
                                          description,
                                          challenges,
                                          href='http://docs.example.com/auth')
        # Check the validity of the JWT
        if not self._token_is_valid(token):
            description = ('The provided auth token is not valid. '
                           'Please request a new token and try again.')
            raise falcon.HTTPUnauthorized('Authentication required',
                                          description,
                                          challenges,
                                          href='http://docs.example.com/auth')

    def _token_is_valid(self, token):
        return Utils.jwt_decode(token)



class CORSComponent(object):

    def process_response(self, req, resp, resource, req_succeeded):

        resp.set_header('Access-Control-Allow-Origin', '*')

        if (req_succeeded
            and req.method == 'OPTIONS'
            and req.get_header('Access-Control-Request-Method')
        ):
            # NOTE(kgriffs): This is a CORS preflight request. Patch the
            #   response accordingly.
            allow = resp.get_header('Allow')
            resp.delete_header('Allow')

            allow_headers = req.get_header(
                'Access-Control-Request-Headers',
                default='*'
            )

            resp.set_headers((
                ('Access-Control-Allow-Methods', allow),
                ('Access-Control-Allow-Headers', allow_headers),
                ('Access-Control-Max-Age', '86400'),  # 24 hours
            ))
