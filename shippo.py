"""Products Function"""
import setup  # pylint: disable=unused-import, wrong-import-order
import logging
import json
from flask import request, Response
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
logger = logging.getLogger("shippo")


class ShippoWebhook(Resource):
    """Shippo Webhook Functions"""

    def options(self):
        """Return Options for Inflight Browser Request"""
        res = Response()
        res.headers["Access-Control-Allow-Origin"] = "*"
        res.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        return res

    def post(self):
        """ShippoWebhook Post"""
        logger.debug("Start ShippoWebhook POST")
        json_args = request.get_json(force=True)
        # Serializing json
        json_object = json.dumps(json_args, indent=4)

        # Writing to sample.json
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)
