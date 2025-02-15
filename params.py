"""Parameters file for Kumpe3D API"""

import setup  # pylint: disable=unused-import, wrong-import-order
import os
import sys
import logging
import configparser
from dotenv import load_dotenv
from loguru import logger

config = configparser.ConfigParser()
config.read("config.ini")

load_dotenv(override=True)
service_token = os.getenv("SERVICE_TOKEN")
app_env = os.getenv("APP_ENV")
log_level = os.getenv("LOG_LEVEL", "INFO")
logger.remove()
logger.add(sys.stderr, level=log_level)


class Params:
    """Parameters"""

    base_url = config["WEB"]["BASE_URL"]
    app_env = os.getenv("APP_ENV", "dev")

    def log_level():  # pylint: disable=no-method-argument
        """Returns Log Level"""
        if os.getenv("LOG_LEVEL").lower() == "info":
            return logging.INFO
        elif os.getenv("LOG_LEVEL").lower() == "warning":
            return logging.WARNING
        elif os.getenv("LOG_LEVEL").lower() == "error":
            return logging.ERROR
        elif os.getenv("LOG_LEVEL").lower() == "debug":
            return logging.DEBUG
        elif os.getenv("LOG_LEVEL").lower() == "critical":
            return logging.CRITICAL
        else:
            return logging.INFO

    class SQL:
        """SQL Parameters for Web_3d User"""

        username = config["MYSQL"]["USERNAME"]
        password = config["MYSQL"]["PASSWORD"]
        server = config["MYSQL"]["SERVER"]
        port = config["MYSQL"]["PORT"]
        database = config["MYSQL"]["DATABASE"]

        def dict():  # pylint: disable=no-method-argument
            """returns as dictionary"""
            return {
                "user": Params.SQL.username,
                "passwd": Params.SQL.password,
                "host": Params.SQL.server,
                "port": Params.SQL.port,
                "db": Params.SQL.database,
            }

    class PayPal:
        """PayPal Parameters"""

        api_url = config["PAYPAL"]["API_URL"]
        client_id = config["PAYPAL"]["CLIENT_ID"]
        secret = config["PAYPAL"]["SECRET"]

    class SendPulse:
        """Send Pulse Parameters"""

        server = config["SENDPULSE"]["SERVER"]
        port = config["SENDPULSE"]["PORT"]
        username = config["SENDPULSE"]["USERNAME"]
        password = config["SENDPULSE"]["PASSWORD"]
        sender = config["SENDPULSE"]["SENDER"]

    class Pushover:
        """Pushover API Parameters"""

        apikey = config["PUSHOVER"]["APIKEY"]
        orders_group = config["PUSHOVER"]["ORDERS_GROUP"]
        server = config["PUSHOVER"]["SERVER"]


if __name__ == "__main__":
    print(
        """Error: This file is a module to be imported and has no functions
          to be ran directly."""
    )
    print(Params.Email.username)
