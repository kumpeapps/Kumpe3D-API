"""Shipping Functions"""
import setup  # pylint: disable=unused-import, wrong-import-order
import logging
from flask import request, Response
from flask_restful import Resource
import pymysql
from params import Params

logging.basicConfig(
    filename="kumpe3d-api.log",
    filemode="a",
    format="%(asctime)s: [%(name)s] [%(levelname)s] %(message)s",
    level=Params.log_level(),
)
logger = logging.getLogger("cart")


class Countries(Resource):
    """Shipping Countries"""

    def options(self):
        """Return Options for Inflight Browser Request"""
        res = Response()
        res.headers["Access-Control-Allow-Origin"] = "*"
        res.headers[
            "Access-Control-Allow-Methods"
        ] = "GET"
        return res

    def get(self):
        """Country Data"""
        logger.debug("start get cart data")
        args = request.args
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
        sql = """
            SELECT 
                name,
                iso2,
                currency,
                currency_name,
                currency_symbol,
                emoji,
                emojiU,
                us_sanctions,
                high_risk,
                packaging_restrictions,
                usps_block
            FROM
                Public.countries
            WHERE 1=1
                AND us_sanctions = 0
                AND high_risk = 0
                AND packaging_restrictions = 0
                AND usps_block = 0
        """
        cursor.execute(sql)
        logger.debug(sql)
        country_list = cursor.fetchall()
        cursor.close()
        db.close()
        logger.debug(country_list)
        return (
            {"response": country_list, "status_code": 200},
            200,
            {"Access-Control-Allow-Origin": "*"},
        )
