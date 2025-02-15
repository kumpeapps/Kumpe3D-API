"""Parameters file for Kumpe3D API"""

import setup  # pylint: disable=unused-import, wrong-import-order
import os
import sys
import logging
from dotenv import load_dotenv
from infisical_api import infisical_api # type: ignore
from loguru import logger

load_dotenv(override=True)
service_token = os.getenv("SERVICE_TOKEN")
app_env = os.getenv("APP_ENV")
log_level = os.getenv("LOG_LEVEL")
logger.remove()
logger.add(sys.stderr, level=log_level)
creds = infisical_api(
    service_token=service_token,
    infisical_url="https://creds.kumpeapps.com",
    workspace_id="65ef13b36b97c857293579af",
    log_level=log_level,
)


class Params:
    """Parameters"""

    base_url = creds.get_secret( # pylint: disable=no-member
        "URL", environment=app_env, path="/WEB/"
    ).secretValue
    app_env = os.getenv("APP_ENV")

    def log_level():  # pylint: disable=no-method-argument
        """Returns Log Level"""
        if os.getenv("LOG_LEVEL") == "info":
            return logging.INFO
        elif os.getenv("LOG_LEVEL") == "warning":
            return logging.WARNING
        elif os.getenv("LOG_LEVEL") == "error":
            return logging.ERROR
        elif os.getenv("LOG_LEVEL") == "debug":
            return logging.DEBUG
        elif os.getenv("LOG_LEVEL") == "critical":
            return logging.CRITICAL
        else:
            return logging.INFO

    class SQL:
        """SQL Parameters for Web_3d User"""

        username = creds.get_secret(  # pylint: disable=no-member
            secret_name="USERNAME", environment=app_env, path="/MYSQL/"
        ).secretValue
        password = creds.get_secret(  # pylint: disable=no-member
            secret_name="PASSWORD", environment=app_env, path="/MYSQL/"
        ).secretValue
        server = creds.get_secret(  # pylint: disable=no-member
            secret_name="SERVER", environment=app_env, path="/MYSQL/"
        ).secretValue
        port = creds.get_secret(  # pylint: disable=no-member
            secret_name="PORT", environment=app_env, path="/MYSQL/"
        ).secretValue
        database = creds.get_secret(  # pylint: disable=no-member
            secret_name="DATABASE", environment=app_env, path="/MYSQL/"
        ).secretValue

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

        api_url = creds.get_secret(  # pylint: disable=no-member
            secret_name="API_URL", environment=app_env, path="/PAYPAL/"
        ).secretValue
        client_id = creds.get_secret(  # pylint: disable=no-member
            secret_name="CLIENT_ID", environment=app_env, path="/PAYPAL/"
        ).secretValue
        secret = creds.get_secret(  # pylint: disable=no-member
            secret_name="SECRET", environment=app_env, path="/PAYPAL/"
        ).secretValue

    class SendPulse:
        """Send Pulse Parameters"""

        server = creds.get_secret(  # pylint: disable=no-member
            secret_name="SERVER", environment=app_env, path="/SENDPULSE/"
        ).secretValue
        port = creds.get_secret(  # pylint: disable=no-member
            secret_name="PORT", environment=app_env, path="/SENDPULSE/"
        ).secretValue
        username = creds.get_secret(  # pylint: disable=no-member
            secret_name="USERNAME", environment=app_env, path="/SENDPULSE/"
        ).secretValue
        password = creds.get_secret(  # pylint: disable=no-member
            secret_name="PASSWORD", environment=app_env, path="/SENDPULSE/"
        ).secretValue
        sender = creds.get_secret(  # pylint: disable=no-member
            secret_name="SENDER", environment=app_env, path="/SENDPULSE/"
        ).secretValue

    class Pushover:
        """Pushover API Parameters"""

        apikey = creds.get_secret(  # pylint: disable=no-member
            secret_name="APIKEY", environment=app_env, path="/PUSHOVER/"
        ).secretValue
        orders_group = creds.get_secret(  # pylint: disable=no-member
            secret_name="ORDERS_GROUP", environment=app_env, path="/PUSHOVER/"
        ).secretValue
        server = creds.get_secret(  # pylint: disable=no-member
            secret_name="SERVER", environment=app_env, path="/PUSHOVER/"
        ).secretValue


if __name__ == "__main__":
    print(
        """Error: This file is a module to be imported and has no functions
          to be ran directly."""
    )
    print(Params.Email.username)
