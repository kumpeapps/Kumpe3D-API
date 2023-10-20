"""Cart Function"""
import setup  # pylint: disable=unused-import, wrong-import-order
import logging
from flask import request
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
                    *
                FROM
                    Web_3dprints.vw_cart__items
                WHERE 1=1
                    AND session_id = %s;"""
        cursor.execute(sql, (session_id))
        logger.debug(sql)
        cart_list = cursor.fetchall()
        total_sql = """SELECT 
                            SUM(totalPrice)
                    FROM Web_3dprints.vw_cart__items
                    WHERE 1=1
                        AND session_id = %s;"""
        cursor.execute(total_sql, (session_id))
        cart_total = cursor.fetchone()
        response = {
            "list": cart_list,
            "total": cart_total
        }
        cursor.close()
        db.close()
        logger.debug(response)
        refresh_session(session_id, user_id)
        return (
            {"response": response, "status_code": 200},
            200,
            {"Access-Control-Allow-Origin": Params.base_url},
        )

    def post(self):
        """Post New Item to Cart"""
        logger.debug("start create cart item")
        args = request.args
        logger.debug("Args: %s", args)
        json_args = request.get_json(force=True)
        logger.debug("JSON ARGS: %s", json_args)
        try:
            qty = int(json_args["quantity"])
        except KeyError:
            qty = 1
        custom = json_args.get("customization", "")
        try:
            sku = json_args["sku"]
        except KeyError:
            logger.error("sku missing")
            return (
                {
                    "error": "session_id sku parameter is required in json",
                    "status_code": 422,
                },
                422,
                {"Access-Control-Allow-Origin": Params.base_url},
            )
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
        sql = """INSERT INTO `Web_3dprints`.`cart__items`
                    (`session_id`,
                    `user_id`,
                    `sku`,
                    `quantity`,
                    `customization`)
                VALUES
                    (%s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE quantity = quantity + %s;"""
        cursor.execute(sql, (session_id, user_id, sku, qty, custom, qty))
        logger.debug(sql)
        db.commit()
        cursor.close()
        db.close()
        refresh_session(session_id, user_id)
        return (
            {"status_code": 201},
            201,
            {"Access-Control-Allow-Origin": "*"},
        )

    def put(self):
        """Update Cart Item"""
        logger.debug("start update cart item")
        args = request.args
        json_args = request.get_json(force=True)
        try:
            qty = int(json_args["quantity"])
        except KeyError:
            qty = 1
        try:
            sku = json_args["sku"]
        except KeyError:
            logger.error("sku missing")
            return (
                {
                    "error": "session_id sku parameter is required in json",
                    "status_code": 422,
                },
                422,
                {"Access-Control-Allow-Origin": Params.base_url},
            )
        customization = json_args.get("customization", "")
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
        sql = """UPDATE `Web_3dprints`.`cart__items`
                    SET quantity = %s
                WHERE 1=1
                    AND `session_id` = %s
                    AND `sku` = %s
                    AND `customization` = %s"""
        cursor.execute(sql, (qty, session_id, sku, customization))
        logger.debug(sql)
        db.commit()
        cursor.close()
        db.close()
        refresh_session(session_id, user_id)
        return (
            {"status_code": 202},
            202,
            {"Access-Control-Allow-Origin": Params.base_url},
        )

    def delete(self):
        """Delete Cart Item"""
        logger.debug("start delete cart item")
        args = request.args
        json_args = request.get_json(force=True)
        try:
            sku = json_args["sku"]
        except KeyError:
            logger.error("sku missing")
            return (
                {
                    "error": "session_id sku parameter is required in json",
                    "status_code": 422,
                },
                422,
                {"Access-Control-Allow-Origin": Params.base_url},
            )
        customization = json_args.get("customization", "")
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
        sql = """DELETE FROM `Web_3dprints`.`cart__items`
                WHERE 1=1
                    AND `session_id` = %s
                    AND `sku` = %s
                    AND `customization` = %s"""
        cursor.execute(sql, (session_id, sku, customization))
        logger.debug(sql)
        db.commit()
        cursor.close()
        db.close()
        refresh_session(session_id, user_id)
        return (
            {"status_code": 204},
            204,
            {"Access-Control-Allow-Origin": Params.base_url},
        )

    def patch(self):
        """Update user cart to current session"""
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
