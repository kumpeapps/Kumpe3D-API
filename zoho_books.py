"""Zoho Books Webhooks"""
import setup  # pylint: disable=unused-import, wrong-import-order
import logging
from flask import request, Response
from flask_restful import Resource

# from flask_restful import reqparse
import pymysql
from params import Params
import helper_funcs as helpers

logging.basicConfig(
    filename="kumpe3d-api.log",
    filemode="a",
    format="%(asctime)s: [%(name)s] [%(levelname)s] %(message)s",
    level=Params.log_level(),
)
logger = logging.getLogger("zoho")


class Zoho(Resource):
    """Product Functions"""
    logger = logging.getLogger("zoho")
    def post(self):
        """Get Product Data"""
        logger.debug("start get")
        json_args = request.get_json(force=True)
        self.logger.debug("JSON ARGS: %s", json_args)
        if True:
            return (
                {"response": "response", "status_code": 200},
                200,
                {"Access-Control-Allow-Origin": Params.base_url},
            )
        else:
            return (
                {"response": [], "status_code": 200},
                200,
                {"Access-Control-Allow-Origin": Params.base_url},
            )
