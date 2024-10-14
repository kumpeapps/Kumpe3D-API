"""Cart Function"""
import setup  # pylint: disable=unused-import, wrong-import-order
import logging
from flask import request, Response, render_template
from flask_restful import Resource
import pymysql
from params import Params

logging.basicConfig(
    filename="kumpe3d-api.log",
    filemode="a",
    format="%(asctime)s: [%(name)s] [%(levelname)s] %(message)s",
    level=Params.log_level(),
)


class CaseLabel(Resource):
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

    def get(self):
        """Get Checkout Data"""
        self.logger.debug("start get checkout data")
        args = request.args
        self.logger.debug("Args: %s", args)
        qr_data = args['qr_data']
        try:
            session_id = args["session_id"]
        except KeyError:
            self.logger.error("session_id missing")
            return (
                {"error": "session_id query parameter is required", "status_code": 422},
                422,
                {"Access-Control-Allow-Origin": "*"},
            )
        self.logger.debug(session_id)
        item_row = """
            <tr>
            <td class='sku'>test product</td>
            <td class='sku'>k3d-test</td>
            <td align='center'>5</td>
            </tr>
        """
        items = item_row

        return (
            {"response": "response", "status_code": 200},
            200,
            {"Access-Control-Allow-Origin": "*"},
        )
