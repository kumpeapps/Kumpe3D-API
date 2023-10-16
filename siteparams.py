"""Site Params Function"""
import setup  # pylint: disable=unused-import, wrong-import-order
import logging
import json
from flask import request, jsonify
from flask_restful import Resource
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
        sql = "call Web_3dprints.get_site_params();"
        cursor.execute(sql)
        logger.debug(sql)
        logger.debug("Get Product Pricing")
        params = cursor.fetchall()
        cursor.close()
        db.close()
        response = {}
        for param in params:
            if param['type'] == "int":
                response[param['parameter']] = param['value']
            elif param['type'] == "json":
                response[param['parameter']] = json.loads(param['value'])
            else:
                response[param['parameter']] = param['value']
        logger.debug(response)
        try:
            referrer = request.environ["HTTP_X_FORWARDED_FOR"]
        except KeyError:
            referrer = base_url
        if referrer == base_url:
            return 401
        else:
            return (
                {"response": response, "status_code": 200},
                200,
                {"Access-Control-Allow-Origin": Params.base_url},
            )
