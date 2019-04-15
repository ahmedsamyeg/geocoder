"""

    File:           config.py
    Version:        1.0.0.0
    Author:         Ahmed Elsayed.
    License:        MIT.
    Description:    this script reads and parses the config.ini file.

"""

import configparser
import os

# the name of the environment
env = 'default'

# check if config.ini exists
if not os.path.isfile('config.ini') :
    print("Cannot open config.ini")
    exit(1)

config_parser = configparser.ConfigParser()
config_parser.read('config.ini')

# get the configurations.
server_port = int(config_parser[env]['SERVER_PORT'])
service_version = config_parser[env]['SERVICE_VERSION']
reponse_encoding = config_parser[env]['RESPONSE_ENCODING']
here_app_id = config_parser[env]['HERE_APP_ID']
here_app_code = config_parser[env]['HERE_APP_CODE']
google_api_app_key = config_parser[env]['GOOGLE_API_APP_KEY']
log_file_name = config_parser[env]['LOG_FILE_NAME']
