"""Cart Function"""

import setup  # pylint: disable=unused-import, wrong-import-order
import logging
from flask import request, Response, render_template, make_response
from flask_restful import Resource
import pymysql
from params import Params
import scan_list_builder as slb

logging.basicConfig(
    filename="kumpe3d-api.log",
    filemode="a",
    format="%(asctime)s: [%(name)s] [%(levelname)s] %(message)s",
    level=Params.log_level(),
)


class CaseLabel(Resource):
    """Endpoints for Case Label"""

    logger = logging.getLogger("case label")

    def options(self):
        """Return Options for Inflight Browser Request"""
        res = Response()
        res.headers["Access-Control-Allow-Origin"] = "*"
        res.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        res.headers["Content-Type"] = "html"
        return res

    def get(self):
        """Build and display case label"""
        args = request.args
        self.logger.debug("Args: %s", args)
        qr_data = args["qr_data"]
        items_dict = slb.build_k3d_item_dict(qr_data)
        items_list = []
        for item in items_dict:
            item["title"] = ""
            items_list.append(item)

        return make_response(
            render_template("case_label.html", qr_data=qr_data.upper(), items=items_list)
        )


class SquareLabel(Resource):
    """Endpoints for Square Label"""

    logger = logging.getLogger("square label")

    def options(self):
        """Return Options for Inflight Browser Request"""
        res = Response()
        res.headers["Access-Control-Allow-Origin"] = "*"
        res.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        res.headers["Content-Type"] = "html"
        return res

    def get(self):
        """Build and display square label"""
        args = request.args
        self.logger.debug("Args: %s", args)
        sku = args.get("sku", "")
        qr_data = args.get("qr_data", sku)
        temp_sql = """
            CREATE TEMPORARY TABLE IF NOT EXISTS temp_products AS (
                SELECT
                    products.sku, title, color_name
                FROM
                    products
            LEFT JOIN filament ON swatch_id = RIGHT(%s, 3)
                WHERE
                    products.sku = %s
                        OR products.sku = CONCAT(LEFT(%s, 11), '-000')
            );
        """

        product_sku = """
            SELECT 
                sku, title, color_name, 'sku' AS `search_type`
            FROM
                temp_products
            WHERE
                sku = %s
            UNION SELECT
                sku, title, color_name, 'base_sku' AS `search_type`
            FROM
                temp_products
            WHERE
                sku = CONCAT(LEFT(%s, 11), '-000')
                    AND NOT EXISTS( SELECT 
                        1
                    FROM
                        temp_products
                    WHERE
                        sku = %s);
        """
        sql_params = Params.SQL
        db = pymysql.connect(
            db=sql_params.database,
            user=sql_params.username,
            passwd=sql_params.password,
            host=sql_params.server,
            port=3306,
        )
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute(temp_sql, (sku, sku, sku))
        cursor.execute(product_sku, (sku, sku, sku))
        product = cursor.fetchone()
        cursor.close()
        db.close()
        title = product["title"]
        color = product["color_name"]
        search_type = product["search_type"]
        if search_type == "base_sku":
            title = f"{title} ({color})"

        return make_response(
            render_template("square_product_label.html", qr_data=qr_data.upper(), title=title)
        )


class ShelfLabel(Resource):
    """Endpoints for Shelf Label"""

    logger = logging.getLogger("shelf label")

    def options(self):
        """Return Options for Inflight Browser Request"""
        res = Response()
        res.headers["Access-Control-Allow-Origin"] = "*"
        res.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        res.headers["Content-Type"] = "html"
        return res

    def get(self):
        """Build and display shelf label"""
        args = request.args
        self.logger.debug("Args: %s", args)
        sku = args.get("sku", "")
        qr_data = args.get("qr_data", sku)
        temp_sql = """
            CREATE TEMPORARY TABLE IF NOT EXISTS temp_products AS (
                SELECT
                    products.sku, title, color_name, type
                FROM
                    products
            LEFT JOIN filament ON swatch_id = RIGHT(%s, 3)
                WHERE
                    products.sku = %s
                        OR products.sku = CONCAT(LEFT(%s, 11), '-000')
            );
        """

        product_sku = """
            SELECT 
                sku, title, color_name, type, 'sku' AS `search_type`
            FROM
                temp_products
            WHERE
                sku = %s
            UNION SELECT
                sku, title, color_name, type, 'base_sku' AS `search_type`
            FROM
                temp_products
            WHERE
                sku = CONCAT(LEFT(%s, 11), '-000')
                    AND NOT EXISTS( SELECT 
                        1
                    FROM
                        temp_products
                    WHERE
                        sku = %s);
        """
        sql_params = Params.SQL
        db = pymysql.connect(
            db=sql_params.database,
            user=sql_params.username,
            passwd=sql_params.password,
            host=sql_params.server,
            port=3306,
        )
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute(temp_sql, (sku, sku, sku))
        cursor.execute(product_sku, (sku, sku, sku))
        product = cursor.fetchone()
        cursor.close()
        db.close()
        title = product["title"]
        color = product["color_name"]
        filament_type = product["type"]

        return make_response(
            render_template(
                "shelf_label.html",
                qr_data=qr_data.upper(),
                title=title,
                filament_color=color,
                filament_type=filament_type,
            )
        )
