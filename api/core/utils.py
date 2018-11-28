import json, re
import jwt, datetime, base64
from passlib.hash import bcrypt
from api.etc.config import *
from cryptography.fernet import Fernet

class Utils:

    def hash(pwd):
        return bcrypt.hash(pwd)

    def verify(pwd, h):
        return bcrypt.verify(pwd, h)

    def encrypt(text):
        if isinstance(text, str) or isinstance(text, bytes):
            f = Fernet(CRYPT_KEY)
            return f.encrypt(text.encode())
        return text

    def decrypt(text):
        if isinstance(text, str) or isinstance(text, bytes):
            f = Fernet(CRYPT_KEY)
            return f.decrypt(text.encode()).decode('utf8')
        return text

    def jwt_encode(json_dict={}):
        json_dict['exp'] = datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        return jwt.encode(json_dict, SECRET, algorithm='HS256').decode('utf-8')

    def jwt_decode(encoded_jwt):
        try:
            a = jwt.decode(encoded_jwt, SECRET, algorithms=['HS256'])
            # print(a)
            return True
        except:
            # print('Not valid')
            return False


    def convert_to_snake():
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    # or
    # >>> a = re.compile('((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))')
    # >>> a.sub(r'_\1', 'getHTTPResponseCode').lower()
    # 'get_http_response_code'
    # >>> a.sub(r'_\1', 'get2HTTPResponseCode').lower()
    # 'get2_http_response_code'
    # >>> a.sub(r'_\1', 'get2HTTPResponse123Code').lower()
    # 'get2_http_response123_code'
    # >>> a.sub(r'_\1', 'HTTPResponseCode').lower()
    # 'http_response_code'
    # >>> a.sub(r'_\1', 'HTTPResponseCodeXYZ').lower()
    # 'http_response_code_xyz'


    def fetch_query_string(req):
        """ Get parameters from falcon query string. """
        return req.params


    def fetch_payload(req):
        """ Get nested falcon parameters. """
        try:
            return json.load(req.bounded_stream)
        except json.decoder.JSONDecodeError:
            return None
