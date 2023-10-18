"""Cart Function"""
import setup  # pylint: disable=unused-import, wrong-import-order
import logging
from flask import request
from flask_restful import Resource
import pymysql
from params import Params
import helper_funcs as helpers

logging.basicConfig(
    filename="kumpe3d-api.log",
    filemode="a",
    format="%(asctime)s: [%(name)s] [%(levelname)s] %(message)s",
    level=Params.log_level(),
)


# TODO:
class Order(Resource):
    """Endpoints for Checkout"""

    logger = logging.getLogger("checkout")

    # TODO:
    def post(self):
        """Checkout"""
        self.logger.debug("start post")
        return (
            {"response": "Not Implemented", "status_code": 501},
            501,
            {"Access-Control-Allow-Origin": Params.base_url},
        )

    # TODO:
    def get(self):
        """Order Status"""
        self.logger.debug("start post")
        return (
            {"response": "Not Implemented", "status_code": 501},
            501,
            {"Access-Control-Allow-Origin": Params.base_url},
        )

    # TODO:
    def put(self):
        """Order Update"""
        self.logger.debug("start post")
        return (
            {"response": "Not Implemented", "status_code": 501},
            501,
            {"Access-Control-Allow-Origin": Params.base_url},
        )
