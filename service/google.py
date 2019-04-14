"""

    File:           google.py
    Version:        1.0.0.0
    Author:         Ahmed S. Elsayed.
    License:        MIT.
    Description:    a wrapper class for google maps geocoding service used to call
                    google service and returns the geocodes.

"""

from urllib import request
from service.geocoding_service import geocoding_service
import json
import config
from utilities.logger import Logger


class Google(geocoding_service):

    def __init__(self):

        # call the base class constructor.
        geocoding_service.__init__(self)
        self.geocoding_service_used = "Google"
        self.geocoding_api_url = f"https://maps.googleapis.com/maps/api/geocode/json?key={config.google_api_app_key}&address="

    def get_geocodes(self, address_to_find):

        # log the usage of google service.
        log = Logger()
        log.log_info(f"Calling {self.geocoding_service_used} service")

        # create a request object
        req = request.Request(self.geocoding_api_url + address_to_find)

        try:

            # open the URL.
            with request.urlopen(req) as api_response:

                # get the HTTP status code from the service
                self.status = api_response.getcode()

                if api_response.status == 200:

                    self.status_desc = "Ok"

                    # get the response and load in json format.
                    json_response = json.loads(api_response.read())

                    # assign the variables with values returned from the api call.
                    self.latitude = json_response["results"][0]["geometry"]["location"]["lat"]
                    self.longitude = json_response["results"][0]["geometry"]["location"]["lng"]
                    self.full_address = json_response["results"][0]["formatted_address"]

                    # log the result.
                    log.log_info(f"Status= {api_response.status}, lat={self.latitude}, lng={self.longitude}")

            # close the request.
            api_response.close()

        except Exception as ex:

            # set the status to 500 - internal server error.
            self.status_desc = ex
            self.status = 500

            # log the critical error.
            log.log_critical(str(ex))
