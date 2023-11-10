"""Parameters file for Kumpe3D API"""
import setup  # pylint: disable=unused-import, wrong-import-order
import os
import logging
from dotenv import load_dotenv
import infisical


load_dotenv()
service_token = os.getenv("SERVICE_TOKEN")
app_env = os.getenv("APP_ENV")
creds = infisical.InfisicalClient(
    token=service_token, site_url="https://creds.kumpeapps.com"
)


class Params:
    """Parameters"""

    base_url = creds.get_secret("URL", environment=app_env, path="/WEB/").secret_value
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

        username = creds.get_secret(
            "USERNAME", environment=app_env, path="/MYSQL/"
        ).secret_value
        password = creds.get_secret(
            "PASSWORD", environment=app_env, path="/MYSQL/"
        ).secret_value
        server = creds.get_secret(
            "SERVER", environment=app_env, path="/MYSQL/"
        ).secret_value
        port = creds.get_secret(
            "PORT", environment=app_env, path="/MYSQL/"
        ).secret_value
        database = creds.get_secret(
            "DATABASE", environment=app_env, path="/MYSQL/"
        ).secret_value

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

        api_url = creds.get_secret(
            "API_URL", environment=app_env, path="/PAYPAL/"
        ).secret_value
        client_id = creds.get_secret(
            "CLIENT_ID", environment=app_env, path="/PAYPAL/"
        ).secret_value
        secret = creds.get_secret(
            "SECRET", environment=app_env, path="/PAYPAL/"
        ).secret_value

    class SendPulse:
        """Send Pulse Parameters"""

        server = creds.get_secret(
            "SERVER", environment=app_env, path="/SENDPULSE/"
        ).secret_value
        port = creds.get_secret(
            "PORT", environment=app_env, path="/SENDPULSE/"
        ).secret_value
        username = creds.get_secret(
            "USERNAME", environment=app_env, path="/SENDPULSE/"
        ).secret_value
        password = creds.get_secret(
            "PASSWORD", environment=app_env, path="/SENDPULSE/"
        ).secret_value
        sender = creds.get_secret(
            "SENDER", environment=app_env, path="/SENDPULSE/"
        ).secret_value

    class Pushover:
        """Pushover API Parameters"""

        apikey = creds.get_secret(
            "APIKEY", environment=app_env, path="/PUSHOVER/"
        ).secret_value
        orders_group = creds.get_secret(
            "ORDERS_GROUP", environment=app_env, path="/PUSHOVER/"
        ).secret_value
        server = creds.get_secret(
            "SERVER", environment=app_env, path="/PUSHOVER/"
        ).secret_value


if __name__ == "__main__":
    print(
        """Error: This file is a module to be imported and has no functions
          to be ran directly."""
    )
    print(Params.Email.username)
