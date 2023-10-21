"""Site Params Function"""
import setup  # pylint: disable=unused-import, wrong-import-order
import logging
import json
from flask import request
from flask_restful import Resource
from helper_funcs import snake_to_camel

# from flask_restful import reqparse
import pymysql
from params import Params

logging.basicConfig(
    filename="kumpe3d-api.log",
    filemode="a",
    format="%(asctime)s: [%(name)s] [%(levelname)s] %(message)s",
    level=Params.log_level(),
)
logger = logging.getLogger("SiteParams")


class SiteParams(Resource):
    """Site Params Functions"""

    def get(self):
        """Get Site Params"""
        sql_params = Params.SQL
        db = pymysql.connect(
            db=sql_params.database,
            user=sql_params.username,
            passwd=sql_params.password,
            host=sql_params.server,
            port=3306,
        )
        logger.debug("start get")
        base_url = Params.base_url
        logger.debug("create cursor")
        cursor = db.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT parameter, value, type FROM Web_3dprints.site_parameters;"
        cursor.execute(sql)
        logger.debug(sql)
        logger.debug("Get Product Pricing")
        params = cursor.fetchall()
        cursor.close()
        db.close()
        response = {}
        for param in params:
            parameter = snake_to_camel(param["parameter"])
            if param["type"] == "int":
                response[parameter] = json.loads(param["value"])
            elif param["type"] == "bool":
                response[parameter] = bool(param["value"])
            elif param["type"] == "json":
                response[parameter] = json.loads(param["value"])
            else:
                response[parameter] = param["value"]
        logger.debug(response)
        try:
            referrer = request.environ["HTTP_REFERER"]
        except KeyError:
            referrer = "none"
        logger.info("Referrer: %s", referrer)
        if referrer != base_url + "/":
            logger.error("Returned 401 Unauthorized")
            return (
                {"error": "Unauthorized"},
                401,
                {"Access-Control-Allow-Origin": "*"},
            )
        else:
            logger.info("Returned 200 Success")
            return (
                {"response": response, "status_code": 200},
                200,
                {"Access-Control-Allow-Origin": "*"},
            )
