# geocoder

**Geocoding** is the process of converting addresses (like a street address) into geographic coordinates (like latitude and longitude), which you can use to place markers on a map, or position the map.

**Reverse geocoding** is the process of converting geographic coordinates into a human-readable address.

#### Geocoding Proxy Service

a simple network service that resolves the lat, lng coordinates for that address
by using third party geocoding services. The service provides a RESTful HTTP interface and
uses JSON for data serialization.

The service implemenst two different third party geocoding services. It has a primary service and additional backup services used for each request. 

For example if the primary geocoding service does not return a result or there is a network error when accessing the
service your code should fall back to using a secondary service to complete the geocoding resolution.

The service implements it's own HTTP request code and does not use third party libraries to access the geocoding services. The service is fully written in Python 3.7 and uses Python Standard Libraries.

The service is written to be production level of quality.

#### Geocoding services used

A. Here: 
two keys are required for Here service, HERE_APP_ID and HERE_APP_CODE, these keys can be obtained from [Here Developer website](https://developer.here.com/documentation/geocoder/topics/quick-start.html).  

B. Google: GOOGLE_API_APP_KEY can be obtained from [Google Developer website]( https://developers.google.com/maps/documentation/geocoding/start).

#### Downloading and running the service 

A. Clone the repository

> git clone --recursive https://github.com/ahmedsamyeg/geocoder.git

B. Set the configurations

1. Rename the 'config.ini.example' to 'config.ini'.
2. Open the config.ini in any text editor and set the configurations. example of configurations:
```
[default]
SERVER_PORT = 3091
SERVICE_VERSION = 1.0.0.0
RESPONSE_ENCODING = utf-8
HERE_APP_ID = xyz212332342
HERE_APP_CODE = ruruirt74
GOOGLE_API_APP_KEY = eerrerte4545
LOG_FILE_NAME = geocoder.log
```
3- run the server browse to the application folder and run the following command:
``` 
python3 server.py
```
the server should run on the port configured in config.ini, here is an example of CLI output 
```
Geocoding Proxy Service - v1.0.0.0
Server Started on port :3091
2019-04-14 11:31:46.183461: INFO: Server Started on port :3091
```

#### Calling the service 

once the server is running, the service can be called from the web browser or Postman by the following format:
```
[HOST]:[PORT]/geocode?address=[address]
```
here is an example
```
http://localhost:3091/geocode?address=835 turk street san francisco
```

#### Service response format

this is an example of the response from the service 
```
{
    "lat": 37.78141,
    "lng": -122.42291,
    "meta": {
        "status": 200,
        "status_desc": "Ok",
        "service_used": "Here",
        "requested_address": "835+turk+street+san+francisco",
        "timestamp": 1555267319
    }
}
```
However if something went wrong the response will have status code other than 200 and the error will be noted in the status description.
```
{
    "lat": 0,
    "lng": 0,
    "meta": {
        "status": 500,
        "status_desc": "list index out of range",
        "service_used": "Google",
        "requested_address": "835+turk+street+san+francisco",
        "timestamp": 1555267501
    }
}
```
beside the response the service log transactions in both the log file and server CLI. the log should look like
```
2019-04-14 11:45:01.492622: INFO: GET received from ('127.0.0.1', 56293) 
2019-04-14 11:45:01.505300: INFO: search for 835+turk+street+san+francisco 
2019-04-14 11:45:01.505621: INFO: Calling Here service 
2019-04-14 11:45:01.770735: CRITICAL: HTTP Error 401: Unauthorized 
2019-04-14 11:45:01.771045: INFO: Calling Google service 
2019-04-14 11:45:01.941228: CRITICAL: list index out of range
```
