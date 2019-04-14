"""

    File:           requests_handler.py
    Version:        1.0.0.0
    Author:         Ahmed Elsayed.
    License:        MIT.
    Description:    a class inherits BaseHTTPRequestHandler to handle all
                    requests received by the http server and returns results from
                    geocoding services.

"""
import urllib.parse as urlparse
import config
import json
from http.server import BaseHTTPRequestHandler
from service.here import Here
from service.google import Google
from utilities.logger import Logger


class RequestHandler(BaseHTTPRequestHandler):

    def _get_geocode(self, param):

        log = Logger()
        # log the address received
        log.log_info(f"search for {param}")
        # get the geocodes using here service.
        service = Here()
        service.get_geocodes(param)
        # if the returned status is nnot 200: ok, call google service.
        if service.status != 200:
            service = Google()
            service.get_geocodes(param)
        # build meta data to attach to the result.
        meta = {'status': service.status, 'status_desc': str(service.status_desc),
                'service_used': service.geocoding_service_used,
                'requested_address': param, 'timestamp': service.timestamp}
        # compose the final results.
        result = {'lat': service.latitude, 'lng': service.longitude,
                  'meta': meta}
        # write the results is json format and in the encoding sepcified in the config file
        self.wfile.write(json.dumps(result).encode(config.reponse_encoding))

    def do_GET(self):

        log = Logger()
        # log the received command and the client ip address and port number.
        log.log_info(f"{self.command} received from {self.client_address}")
        # parse the url
        url = urlparse.urlparse(self.path)
        # check if the client call is correct.
        if url.path == '/geocode':
            # send 200 : Ok status.
            self.send_response(200)
            self.send_header('Content-type', 'json')
            self.end_headers()
            # check if address query string is passed
            if urlparse.parse_qs(url.query).get('address'):
                # get the geocodes off the passed address
                address = urlparse.parse_qs(url.query)['address'][0].replace(" ", "+")
                self._get_geocode(address)
            else:
                # send 400 : Bad Request status and log the error.
                self.send_response(400)
                log.log_error("address parameter not passed")
        else:
            # send 404 : Not Found status and log the error.
            self.send_response(404)
            log.log_error("Unknown service requested.")
