"""Products Function"""
import setup  # pylint: disable=unused-import, wrong-import-order
import logging
from flask import request
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
logger = logging.getLogger("product")


class Product(Resource):
    """Product Functions"""

    def get(self):
        """Get Product Data"""
        logger.debug("start get")
        args = request.args
        logger.debug("convert sku to array")
        sku = helpers.get_sku_array(args["sku"])
        response = get_products(sku)
        response["sku_parts"] = sku
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


class ProductPrice(Resource):
    """Product Price Functions"""

    logging.basicConfig(
        filename="kumpe3d-api.log",
        filemode="a",
        format="%(asctime)s: [%(name)s] [%(levelname)s] %(message)s",
        level=Params.log_level(),
    )
    logger = logging.getLogger("product-price")

    def get(self):
        """Get Product Pricing"""
        self.logger.debug("start get")
        args = request.args
        self.logger.debug("convert sku to array")
        sku = helpers.get_sku_array(args["sku"])
        quantity = int
        try:
            quantity = int(args["quantity"])
        except (KeyError, ValueError):
            quantity = 1
        response = get_product_pricing(sku, quantity)
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


def get_product_pricing(sku: dict, quantity: int) -> dict:
    """Get Product Pricing"""
    sql_params = Params.SQL
    db = pymysql.connect(
        db=sql_params.database,
        user=sql_params.username,
        passwd=sql_params.password,
        host=sql_params.server,
        port=3306,
    )
    logger.debug("create cursor")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = "CALL Web_3dprints.get_product_price(%s, %s);"
    cursor.execute(sql, (sku["base_sku"], quantity))
    logger.debug(sql)
    logger.debug("Get Product Pricing")
    response = cursor.fetchone()
    cursor.close()
    db.close()
    logger.debug(response)
    return response


def get_products(sku: dict, category_filter: str = "%", tag_filter: str = "%"):
    """Get Product Data"""
    logger.debug("start get product data")
    if sku == "%":
        single = False
    else:
        single = True

    sql_params = Params.SQL
    db = pymysql.connect(
        db=sql_params.database,
        user=sql_params.username,
        passwd=sql_params.password,
        host=sql_params.server,
        port=3306,
    )
    logger.debug("create cursor")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = "CALL get_products(%s, %s, %s)"
    cursor.execute(sql, (sku["base_sku"], category_filter, tag_filter))
    logger.debug(sql)
    if single:
        response = cursor.fetchone()
    else:
        response = cursor.fetchall()
    cursor.close()
    db.close()
    logger.debug(response)
    return response


class ProductImages(Resource):
    """Product Images"""

    logging.basicConfig(
        filename="kumpe3d-api.log",
        filemode="a",
        format="%(asctime)s: [%(name)s] [%(levelname)s] %(message)s",
        level=Params.log_level(),
    )
    logger = logging.getLogger("product-images")

    def get(self) -> list:
        """Get Product Images"""
        logger.debug("start get product images")
        args = request.args
        logger.debug("convert sku to array")
        sku = helpers.get_sku_array(args["sku"])

        sql_params = Params.SQL
        db = pymysql.connect(
            db=sql_params.database,
            user=sql_params.username,
            passwd=sql_params.password,
            host=sql_params.server,
            port=3306,
        )
        logger.debug("create cursor")
        cursor = db.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM Web_3dprints.product_photos WHERE sku = %s;"
        cursor.execute(sql, (sku["base_sku"]))
        logger.debug(sql)
        response = cursor.fetchall()
        cursor.close()
        db.close()
        logger.debug(response)
        return (
            {"response": response, "status_code": 200},
            200,
            {"Access-Control-Allow-Origin": Params.base_url},
        )
