
import json

class Utils:

    def fetch_query_string(req):
        """ Get parameters from falcon query string. """
        return req.params


    def fetch_payload(req):
        """ Get nested falcon parameters. """
        try:
            return json.load(req.bounded_stream)
        except json.decoder.JSONDecodeError:
            return None
