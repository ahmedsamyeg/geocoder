# geocoder
Geocoding Proxy Service

a simple network service that resolves the lat, lng coordinates for that address
by using third party geocoding services. The service provides a RESTful HTTP interface and
uses JSON for data serialization.

The service implemenst two different third party geocoding services. It has a primary service and additional backup services used for each request. 

For example if the primary geocoding service does not return a result or there is a network error when accessing the
service your code should fall back to using a secondary service to complete the geocoding resolution.

The service implements it's own HTTP request code and does not use third party libraries to access the geocoding services. The service is fully written in Python 3.7 and uses Python Standard Libraries.

The service is written to be production level of quality.

# Geocoding Services

A. Here: https://developer.here.com/documentation/geocoder/topics/quick-start.html
B. Google: https://developers.google.com/maps/documentation/geocoding/start
