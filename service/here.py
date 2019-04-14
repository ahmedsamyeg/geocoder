"""

    File:           here.py
    Version:        1.0.0.0
    Author:         Ahmed S. Elsayed.
    License:        MIT.
    Description:    a wrapper class for here  geocoding service used to call
                    here service and returns the geocodes.

"""

from urllib import request
from service.geocoding_service import geocoding_service
import json
import config
from utilities.logger import Logger

class Here(geocoding_service):

    def __init__(self):

        # call the base class constructor.
        geocoding_service.__init__(self)
        self.geocoding_service_used = "Here"
        self.geocoding_api_url = f"https://geocoder.api.here.com/6.2/geocode.json?app_id={config.here_app_id}&app_code={config.here_app_code}&searchtext="

    def get_geocodes(self, address_to_find):

        # log the usage of here service.
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
                    self.latitude = json_response['Response']['View'][0]["Result"][0]["Location"]["DisplayPosition"]["Latitude"]
                    self.longitude = json_response['Response']['View'][0]["Result"][0]["Location"]["DisplayPosition"]["Longitude"]
                    self.full_address = json_response['Response']['View'][0]["Result"][0]["Location"]["Address"]["Label"]

                    # log the result.
                    log.log_info(f"Status= {api_response.status}, lat={self.latitude}, lng={self.longitude}")

            api_response.close()

        except Exception as ex:

            # set the status to 500 - internal server error.
            self.status_desc = ex
            self.status = 500

            # log the critical error.
            log.log_critical(str(ex))

