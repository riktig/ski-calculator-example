from http.server import BaseHTTPRequestHandler
import json

from .calculator import Skier, calculate_ski_length

#TODO http.server is not recommended for production. It only implements basic security checks.
class SkiRequestHandler(BaseHTTPRequestHandler):
    def _send_success_response(self, response):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))

    def _get_post_data(self):
        content_length = int(self.headers['Content-Length'])
        return self.rfile.read(content_length)

    #TODO add error handling
    def do_POST(self):
        post_data = self._get_post_data()
        json_data = _load_json(post_data)

        skier = _create_skier(json_data)
        ski_length = calculate_ski_length(skier)

        response = _create_response_json(*ski_length)
        self._send_success_response(response)


def _load_json(data):
    #TODO use json schema or something similar to validate json
    return json.loads(data)


def _create_skier(json_data):
    return Skier(json_data["length"], json_data["age"], json_data["style"])


def _create_response_json(ski_length_min, ski_length_max):
    if ski_length_min == ski_length_max:
        return json.dumps({'ski_length': ski_length_min})
    else:
        return json.dumps(
            {
                'ski_length_min': ski_length_min,
                'ski_length_max': ski_length_max,
            })
