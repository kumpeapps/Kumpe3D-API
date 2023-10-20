"""Cart Function"""
import setup  # pylint: disable=unused-import, wrong-import-order
import logging
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


# TODO:
class Order(Resource):
    """Endpoints for Checkout"""

    logger = logging.getLogger("checkout")

    def options(self):
        """Return Options for Inflight Browser Request"""
        res = Response()
        res.headers["Access-Control-Allow-Origin"] = "*"
        res.headers[
            "Access-Control-Allow-Methods"
        ] = "GET, OPTIONS, POST, PUT, PATCH, DELETE"
        return res

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


class ZipCodes(Resource):
    """Endpoints for Zip Code Database"""

    logger = logging.getLogger("ZipCodes")

    def options(self):
        """Return Options for Inflight Browser Request"""
        res = Response()
        res.headers["Access-Control-Allow-Origin"] = "*"
        res.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        return res

    def get(self):
        """Get Zip code Data"""
        self.logger.debug("start get")
        args = request.args
        zip_filter = args.get("zip", "%")
        city_filter = args.get("city", "%")
        state_filter = args.get("state", "%")

        sql_params = Params.SQL
        db = pymysql.connect(
            db=sql_params.database,
            user=sql_params.username,
            passwd=sql_params.password,
            host=sql_params.server,
            port=3306,
        )
        self.logger.debug("create cursor")
        cursor = db.cursor(pymysql.cursors.DictCursor)
        sql = """SELECT
                    *
                FROM
                    Public.vw_Addresses__Zips
                WHERE 1=1
                    AND state_id LIKE %s
                    AND city LIKE %s
                    AND zip LIKE %s;"""
        cursor.execute(sql, (state_filter, city_filter, zip_filter))
        self.logger.debug(sql)
        response = cursor.fetchall()
        cursor.close()
        db.close()
        self.logger.debug(response)
        return (
            {"response": response, "status_code": 200},
            200,
            {"Access-Control-Allow-Origin": Params.base_url},
        )
