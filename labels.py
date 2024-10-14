"""Cart Function"""
import setup  # pylint: disable=unused-import, wrong-import-order
import logging
from flask import request, Response, render_template, make_response
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
        res.headers["Content-Type"] = "html"
        return res

    def get(self):
        """Get Checkout Data"""
        self.logger.debug("start get checkout data")
        args = request.args
        self.logger.debug("Args: %s", args)
        qr_data = args['qr_data']
        item_row = """
            <tr>
            <td class='sku'>test product</td>
            <td class='sku'>k3d-test</td>
            <td align='center'>5</td>
            </tr>
        """
        items = item_row

        return make_response(render_template("case_label.html", qr_data=qr_data, items=items))
