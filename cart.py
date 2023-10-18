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
logger = logging.getLogger("cart")


class Cart(Resource):
    """Shopping Cart Functions"""

    def get(self):
        """Get Cart Items"""
        logger.debug("start get cart data")
        args = request.args
        try:
            session_id = args["session_id"]
        except KeyError:
            logger.error("session_id missing")
            return (
                {"error": "session_id query parameter is required", "status_code": 422},
                422,
                {"Access-Control-Allow-Origin": Params.base_url},
            )

        try:
            user_id = int(args["user_id"])
        except KeyError:
            logger.warning("user_id missing")
            user_id = 0

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
        refresh_session(session_id, user_id)
        return (
            {"response": response, "status_code": 200},
            200,
            {"Access-Control-Allow-Origin": Params.base_url},
        )

    # TODO:
    def post(self):
        """Post New Item to Cart"""
        logger.debug("start create cart item")
        args = request.args
        json_args = request.get_json(force=True)
        try:
            session_id = args["session_id"]
        except KeyError:
            logger.error("session_id missing")
            return (
                {"error": "session_id query parameter is required", "status_code": 422},
                422,
                {"Access-Control-Allow-Origin": Params.base_url},
            )

        try:
            user_id = int(args["user_id"])
        except KeyError:
            logger.warning("user_id missing")
            user_id = 0
        refresh_session(session_id, user_id)

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
        refresh_session(session_id, user_id)
        return (
            {"response": response, "status_code": 201},
            201,
            {"Access-Control-Allow-Origin": Params.base_url},
        )

    # TODO:
    def put(self):
        """Update Item in Cart"""
        logger.debug("start put")
        return (
            {"response": "Not Implemented", "status_code": 501},
            501,
            {"Access-Control-Allow-Origin": Params.base_url},
        )

    # TODO:
    def delete(self):
        """Update Item in Cart"""
        logger.debug("start delete")
        return (
            {"response": "Not Implemented", "status_code": 501},
            501,
            {"Access-Control-Allow-Origin": Params.base_url},
        )

    def patch(self):
        """Update session timestamp on patch"""
        logger.debug("start patch")
        args = request.args
        try:
            session_id = args["session_id"]
        except KeyError:
            logger.error("session_id missing")
            return (
                {
                    "error": "session_id query parameter is required",
                    "status_code": 422,
                },
                422,
                {"Access-Control-Allow-Origin": Params.base_url},
            )
        try:
            user_id = int(args["user_id"])
        except KeyError:
            logger.warning("user_id missing")
            user_id = 0

        refresh_session(session_id, user_id)
        return (
            {"status_code": 204},
            204,
            {"Access-Control-Allow-Origin": Params.base_url},
        )


def refresh_session(session_id: str, user_id: int):
    """Update session timestamp"""
    logger.debug("start refresh_session")
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
    if user_id != 0:
        sql = "UPDATE `Web_3dprints`.`cart__items` SET `session_id` = %s WHERE user_id = %s"
        cursor.execute(sql, (session_id, user_id))
        db.commit()
    sql = "UPDATE `Web_3dprints`.`cart__items` SET `timestamp` = now() WHERE session_id = %s"
    cursor.execute(sql, (session_id))
    cursor.callproc("expire_sessions")
    db.commit()
    db.close()


# TODO:
class Checkout(Resource):
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
