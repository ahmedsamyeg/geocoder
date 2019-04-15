"""

    File:           server.py
    Version:        1.0.0.0
    Author:         Ahmed Elsayed.
    License:        MIT.
    Description:    the entry point of the app that starts http server and listens to all requests
                    on port specified in the config file.

"""

import http.server
import config
from requests_handler import RequestHandler
from utilities.logger import Logger


def run(host, port):

    log = Logger()
    try:
        # create http server.
        server = http.server.HTTPServer((host, port), RequestHandler)
        print(f"Geocoding Proxy Service - v{config.service_version}")
        print(f"Server Started on port :{port}")
        # log the start of the server.
        log.log_info(f"Server Started on port :{str(port)}")
        # listen for ever.
        server.serve_forever()

    except Exception as ex:
        # in case of exception, log the incident as critical.
        msg = f"Server Start error - {str(ex)}"
        log.log_critical(msg)
        exit(1)


# run the server
run('', config.server_port)
