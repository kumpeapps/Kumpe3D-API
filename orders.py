"""Cart Function"""
import setup  # pylint: disable=unused-import, wrong-import-order
import logging
from flask import request, Response
from flask_restful import Resource
import pymysql
from salestax import Arkansas as ar
from params import Params
import helper_funcs as helpers
from cart import get_cart

logging.basicConfig(
    filename="kumpe3d-api.log",
    filemode="a",
    format="%(asctime)s: [%(name)s] [%(levelname)s] %(message)s",
    level=Params.log_level(),
)


# TODO:
class Checkout(Resource):
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

    def post(self):
        """Get Checkout Data"""
        self.logger.debug("start get checkout data")
        args = request.args
        self.logger.debug(args)
        json_args = request.get_json(force=True)
        try:
            session_id = args["session_id"]
        except KeyError:
            self.logger.error("session_id missing")
            return (
                {"error": "session_id query parameter is required", "status_code": 422},
                422,
                {"Access-Control-Allow-Origin": "*"},
            )
        try:
            user_id = int(args["user_id"])
        except (KeyError, ValueError):
            self.logger.warning("user_id missing")
            user_id = 0

        response = build_checkout_data(session_id, user_id, json_args, args)
        return (
            {"response": response, "status_code": 200},
            200,
            {"Access-Control-Allow-Origin": "*"},
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
        single_record = args.get("single_record", 0)

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
        if single_record:
            response = cursor.fetchone()
        else:
            response = cursor.fetchall()
        cursor.close()
        db.close()
        self.logger.debug(response)
        return (
            {"response": response, "status_code": 200},
            200,
            {"Access-Control-Allow-Origin": Params.base_url},
        )


class Taxes(Resource):
    """Endpoints for Taxes"""

    logger = logging.getLogger("Taxes")

    def options(self):
        """Return Options for Inflight Browser Request"""
        res = Response()
        res.headers["Access-Control-Allow-Origin"] = "*"
        res.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        return res

    def get(self):
        """Get Tax Rates"""
        args = request.args
        self.logger.debug(args)
        address = args["address"]
        city = args["city"]
        state = args["state"]
        zip_code = args["zip"]

        try:
            subtotal = float(args["subtotal"])
        except (KeyError, TypeError, ValueError):
            subtotal = 0

        response = get_taxes(address, city, state, zip_code, subtotal)

        return (
            {"response": response, "status_code": 200},
            200,
            {"Access-Control-Allow-Origin": "*"},
        )


def get_taxes(
    address: str, city: str, state: str, zip_code: str, subtotal: float
) -> dict:
    """Get Taxes"""
    if state == "AR":
        response = ar.get(address, city, zip_code)
    else:
        response = {
            "is_state_taxable": False,
            "is_county_taxable": False,
            "is_city_taxable": False,
        }

    try:
        subtotal = float(subtotal)
    except (KeyError, TypeError, ValueError):
        subtotal = 0

    if response["is_state_taxable"]:
        state_tax = subtotal * helpers.percent_to_float(response["state_tax_rate"])
        response["state_tax"] = round(state_tax, 2)

    if response["is_city_taxable"]:
        city_tax = subtotal * helpers.percent_to_float(response["city_tax_rate"])
        response["city_tax"] = round(city_tax, 2)

    if response["is_county_taxable"]:
        county_tax = subtotal * helpers.percent_to_float(response["county_tax_rate"])
        response["county_tax"] = round(county_tax, 2)

    return response


def build_checkout_data(
    session_id: str, user_id: int, json_args: dict, args: dict
) -> dict:
    """Build Checkout Data"""
    first_name = json_args.get("fName", "")
    last_name = json_args.get("lName", "")
    company = json_args.get("company", "")
    address = json_args.get("address", "")
    address2 = json_args.get("address2", "")
    city = json_args.get("city", "")
    state = json_args.get("state", "")
    zip_code = json_args.get("zip", "")
    comments = json_args.get("comments", "")
    shipping_address = {
        "fName": first_name,
        "lName": last_name,
        "company": company,
        "address": address,
        "address2": address2,
        "city": city,
        "state": state,
        "zip": zip_code,
        "comments": comments,
    }

    cart = get_cart(session_id, user_id)
    taxes = get_taxes(address, city, state, zip_code, cart["subtotal"])
    state_tax = taxes.get("state_tax", 0)
    county_tax = taxes.get("county_tax", 0)
    city_tax = taxes.get("city_tax", 0)
    paypal_transaction_id = args.get("paypal_transaction_id", "")
    tax_total = state_tax + county_tax + city_tax
    shipping_total = 10
    grand_total = cart["subtotal"] + shipping_total + tax_total
    response = {
        "shippingAddress": shipping_address,
        "cart": cart,
        "taxes": taxes,
        "taxTotal": tax_total,
        "shippingCost": shipping_total,
        "grandTotal": grand_total,
        "paypalTransactionID": paypal_transaction_id,
    }
    return response
