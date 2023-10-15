"""Parameters file for HAC"""
import setup # pylint: disable=unused-import, wrong-import-order
import os
from dotenv import load_dotenv
import infisical


load_dotenv()
service_token = os.getenv('SERVICE_TOKEN')
app_env = os.getenv('APP_ENV')
creds = infisical.InfisicalClient(token=service_token, site_url='https://creds.kumpeapps.com')

class Params:
    """Parameters"""
    base_url = creds.get_secret("URL", environment=app_env, path="/WEB/").secret_value
    class SQL:
        """SQL Parameters for Web_3d User"""
        username = creds.get_secret("USERNAME", environment=app_env, path="/MYSQL/").secret_value
        password = creds.get_secret("PASSWORD", environment=app_env, path="/MYSQL/").secret_value
        server = creds.get_secret("SERVER", environment=app_env, path="/MYSQL/").secret_value
        port = creds.get_secret("PORT", environment=app_env, path="/MYSQL/").secret_value
        database = creds.get_secret("DATABASE", environment=app_env, path="/MYSQL/").secret_value

        def dict(): # pylint: disable=no-method-argument
            """returns as dictionary"""
            return {
                'user': Params.SQL.username,
                'passwd': Params.SQL.password,
                'host': Params.SQL.server,
                'port': Params.SQL.port,
                'db': Params.SQL.database
            }


if __name__ == "__main__":
    print("""Error: This file is a module to be imported and has no functions
          to be ran directly.""")
    print(Params.Email.username)
