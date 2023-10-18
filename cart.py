"""Cart Function"""
import setup  # pylint: disable=unused-import, wrong-import-order
import logging
from flask import request
from flask_restful import Resource
from flask_restful import reqparse
import pymysql
from params import Params
import helper_funcs as helpers

logging.basicConfig(
    filename="kumpe3d-api.log",
    filemode="a",
    format="%(asctime)s: [%(name)s] [%(levelname)s] %(message)s",
    level=Params.log_level(),
)
logger = logging.getLogger("cart")


class Cart(Resource):
    """Shopping Cart Functions"""

    def get(self):
        """Get Cart Items"""
        logger.debug("start get product images")
        args = request.args
        session_id = args["session_id"]

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
        sql = """SELECT
                    session_id,
                    user_id,
                    sku,
                    title,
                    quantity,
                    customization
                FROM
                    Web_3dprints.cart__items
                WHERE 1=1
                    AND session_id = %s;"""
        cursor.execute(sql, (session_id))
        logger.debug(sql)
        response = cursor.fetchall()
        cursor.close()
        db.close()
        logger.debug(response)
        refresh_session(session_id)
        return (
            {"response": response, "status_code": 200},
            200,
            {"Access-Control-Allow-Origin": Params.base_url},
        )


def refresh_session(session_id: str):
    """Update session timestamp"""
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
    sql = "UPDATE `Web_3dprints`.`cart__items` SET `timestamp` = now() WHERE session_id = %s"
    cursor.execute(sql, (session_id))
    db.commit()
    db.close()
