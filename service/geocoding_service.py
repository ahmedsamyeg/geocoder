"""

    File:           geocoding_service.py
    Version:        1.0.0.0
    Author:         Ahmed Elsayed.
    License:        MIT.
    Description:    base class for all geocoding service wrapper classes.

"""
import time


class geocoding_service:

    def __init__(self):

        self.latitude = 0
        self.longitude = 0
        self.geocoding_service_used = ""
        self.full_address = ""
        self.timestamp = int(time.time())
        self.status = 0
        self.geocoding_api_url = ""
        self.status_desc = ""


    def get_geocodes(self, address_to_find):
        pass

