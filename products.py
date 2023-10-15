"""Products Function"""
import setup  # pylint: disable=unused-import, wrong-import-order
from flask import request
from flask import jsonify, json
from flask_restful import Resource
from flask_restful import reqparse
import pymysql
from params import Params
import helper_funcs as helpers
import logging


class Product(Resource):
    """Product Functions"""

    logging.basicConfig(
        filename="kumpe3d-api.log",
        filemode="a",
        format="%(asctime)s: [%(name)s] [%(levelname)s] %(message)s",
        level=Params.log_level(),
    )
    logger = logging.getLogger("products")

    def get(self):
        """Get Product Data"""
        self.logger.debug("start get")

        sql_params = Params.SQL
        db = pymysql.connect(
            db=sql_params.database,
            user=sql_params.username,
            passwd=sql_params.password,
            host=sql_params.server,
            port=3306,
        )
        args = request.args
        self.logger.debug("convert sku to array")
        sku = helpers.get_sku_array(args["sku"])
        self.logger.debug("create cursor")
        cursor = db.cursor(pymysql.cursors.DictCursor)
        sql = "CALL get_products(%s, %s, %s)"
        cursor.execute(sql, (sku["base_sku"], "%", "%"))
        self.logger.debug(sql)
        response = cursor.fetchone()
        # response.headers.add("Access-Control-Allow-Origin", "*")
        # response.mimetype = "application/json"
        cursor.close()
        db.close()
        self.logger.debug(response)
        if response:
            return (
                {"response": response, "status_code": 200},
                200,
                {"Access-Control-Allow-Origin": Params.base_url},
            )
        else:
            return (
                {"response": response, "status_code": 204},
                204,
                {"Access-Control-Allow-Origin": Params.base_url},
            )
        
