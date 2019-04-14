"""

    File:           logger.py
    Version:        1.0.0.0
    Author:         Ahmed Elsayed.
    License:        MIT.
    Description:    a wrapper class for logging to additionally output to the CLI.

"""

import logging
import time
from datetime import datetime
import config

class Logger:

    def __init__(self):
        # set the basic configurations; logging level to Info, log file name and log format
        logging.basicConfig(level=logging.INFO, filename=config.log_file_name,
                    filemode='a', format='%(asctime)s: %(levelname)s: %(message)s')
        self.log = logging.getLogger()

    def log_error(self, msg):
        # log an error.
        self.log.error(msg)
        self.write("ERROR", msg)

    def log_critical(self, msg):
        # log a critical error.
        self.log.critical(msg)
        self.write("CRITICAL", msg)

    def log_info(self, msg):
        # log information.
        self.log.info(msg)
        self.write("INFO", msg)

    def write(self, level, msg):
        print(f"{datetime.now()}: {level}: {msg} ")
