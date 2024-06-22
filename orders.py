"""Cart Function"""
import setup  # pylint: disable=unused-import, wrong-import-order
import logging
from multiprocessing import Process
from flask import request, Response
from flask_restful import Resource
import pymysql
from salestax import Arkansas as ar
from params import Params
import helper_funcs as helpers
from cart import get_cart
from email_template import generate_email
import paypal
from send_email import send_email
from costs import get_product_costs
import notif
from label_print_q import print_packing_slip

logging.basicConfig(
    filename="kumpe3d-api.log",
    filemode="a",
    format="%(asctime)s: [%(name)s] [%(levelname)s] %(message)s",
    level=Params.log_level(),
)


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
        self.logger.debug("Args: %s", args)
        json_args = request.get_json(force=True)
        self.logger.debug("JSON ARGS: %s", json_args)
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
        try:
            user_id = int(args["user_id"])
        except (KeyError, ValueError):
            self.logger.warning("user_id missing")
            user_id = 0
        self.logger.debug(session_id)
        response = build_checkout_data(session_id, user_id, json_args, args)
        self.logger.debug(response)
        return (
            {"response": response, "status_code": 200},
            200,
            {"Access-Control-Allow-Origin": "*"},
        )


class CheckoutFinal(Resource):
    """Endpoints for Checkout"""

    logger = logging.getLogger("checkout")

    def options(self):
        """Return Options for Inflight Browser Request"""
        res = Response()
        res.headers["Access-Control-Allow-Origin"] = "*"
        res.headers["Accept"] = "application/json"
        res.headers[
            "Access-Control-Allow-Methods"
        ] = "GET, OPTIONS, POST, PUT, PATCH, DELETE"
        return res

    def post(self):
        """Finalize Checkout"""
        logger = logging.getLogger("checkout-final")
        logger.debug("start finalize checkout (PUT)")

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
        args = request.args
        self.logger.debug("Args: %s", args)
        json_args = request.get_json(force=True)
        logger.debug("JSON ARGS: %s", json_args)
        try:
            data = json_args
            session_id = args["session_id"]
            cart = data["cart"]
            logger.debug("Cart: %s", cart)
        except KeyError:
            logger.error("One or more parameters missing")
            return (
                {
                    "error": "One or more required paramenters are missing.",
                    "status_code": 422,
                },
                422,
                {"Access-Control-Allow-Origin": "*"},
            )
        logger.debug(session_id)

        try:
            user_id = int(data["customerID"])
        except (KeyError, ValueError):
            logger.warning("user_id missing")
            user_id = 0

        orders_sql = """
                    INSERT INTO `Web_3dprints`.`orders`
                        (`idcustomers`,
                        `first_name`,
                        `last_name`,
                        `company_name`,
                        `email`,
                        `street_address`,
                        `street_address_2`,
                        `city`,
                        `state`,
                        `zip`,
                        `country`,
                        `subtotal`,
                        `taxes`,
                        `shipping_cost`,
                        `discount`,
                        `total`,
                        `order_date`,
                        `status_id`,
                        `payment_method`,
                        `paypal_transaction_id`,
                        `paypal_capture_id`,
                        `notes`,
                        `taxable_state`,
                        `taxable_county`,
                        `taxable_city`,
                        `state_tax`,
                        `county_tax`,
                        `city_tax`,
                        `client_ip`,
                        `client_browser`,
                        `referral`)
                    VALUES
                        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, now(), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        if paypal.verify_order(data["ppTransactionID"]):
            order_status = 3
            order_status_name = "Processed"
        else:
            order_status = 2
            order_status_name = "Pending"

        tax_data = data["taxData"]

        orders_values = (
            user_id,
            data["firstName"],
            data["lastName"],
            data["companyName"],
            data["emailAddress"],
            data["address"],
            data["address2"],
            data["city"],
            data["state"],
            data["zip"],
            data["country"],
            data["subtotal"],
            data["taxes"],
            data["shippingCost"],
            data["discount"],
            data["total"],
            order_status,
            data["paymentMethod"],
            data["ppTransactionID"],
            data["ppCaptureID"],
            data["orderNotes"],
            tax_data.get("taxable_state", None),
            tax_data.get("taxable_county", None),
            tax_data.get("taxable_city", None),
            tax_data.get("state_tax", None),
            tax_data.get("county_tax", None),
            tax_data.get("city_tax", None),
            data.get("client_ip", None),
            data.get("browser", None),
            data.get("referral_code", None),
        )
        cursor.execute(orders_sql, orders_values)
        db.commit()
        order_id = cursor.lastrowid
        email_data = {}
        email_data["email_orderid"] = order_id
        email_data["email_date"] = ""
        response = {}
        response["id"] = order_id
        email_data["email_products"] = ""
        email_data["email_name"] = data["firstName"]
        email_data["email_shippingname"] = data["firstName"] + " " + data["lastName"]
        email_data["email_base_url"] = Params.base_url
        if data["companyName"] != "":
            email_data["email_shippingname"] = (
                email_data["email_shippingname"] + "<br>" + data["companyName"]
            )
        email_data["email_address"] = data["address"]
        email_data["email_address2"] = data["address2"]
        if email_data["email_address2"] != "":
            email_data["email_address"] = (
                email_data["email_address"] + "<br>" + email_data["email_address2"]
            )
        email_data["email_city"] = data["city"]
        email_data["email_state"] = data["state"]
        email_data["email_zip"] = data["zip"]
        email_data["email_country"] = data["country"]
        email_data["email_subtotal"] = "$" + f'{data["subtotal"]}'
        email_data["email_taxes"] = "$" + f'{data["taxes"]}'
        email_data["email_shippingcost"] = "$" + f'{data["shippingCost"]}'
        email_data["email_discount"] = "$" + f'{data["discount"]}'
        email_data["email_total"] = "$" + f'{data["total"]}'
        email_data["email_paymentmethod"] = data["paymentMethod"]
        email_data["email_shippingmethod"] = "Flat Rate"
        email_data["email_notes"] = data["orderNotes"]

        items_sql = """
                    INSERT INTO `Web_3dprints`.`orders__items`
                        (`idorders`,
                        `sku`,
                        `title`,
                        `price`,
                        `qty`,
                        `cost`,
                        `customization`)
                    VALUES
                        (%s, %s, %s, %s, %s, %s, '');
        """

        history_sql = """
                    INSERT INTO `Web_3dprints`.`stock`
                        (`sku`,
                        `swatch_id`,
                        `qty`)
                    VALUES
                        (%s, %s, 0 - %s)
                    ON DUPLICATE KEY UPDATE    
                        qty = qty - %s;
        """

        empty_session_sql = (
            "DELETE FROM Web_3dprints.cart__items WHERE session_id = %s;"
        )

        for item in cart:
            item_values = (
                order_id,
                item["sku"],
                item["title"],
                item["price"],
                item["quantity"],
                get_product_costs(item["sku"], item["query_sku"]),
            )
            product_img = item["img_url"]
            product_name = item["title"]
            product_sku = item["sku"]
            product_quantity = item["quantity"]
            product_price = "$" + f'{item["price"]}'
            cursor.execute(items_sql, item_values)
            html_email_items = f"""
                <tr>
                    <td align="left" style="padding:0;Margin:0;padding-left:20px;padding-right:20px;padding-bottom:40px">
                        <!--[if mso]><table style="width:560px" cellpadding="0" cellspacing="0"><tr><td style="width:195px" valign="top"><![endif]-->
                        <table cellpadding="0" cellspacing="0" class="es-left" align="left"
                            style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left">
                            <tr>
                                <td align="left" class="es-m-p20b" style="padding:0;Margin:0;width:195px">
                                    <table cellpadding="0" cellspacing="0" width="100%" role="presentation"
                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                        <tr>
                                            <td align="center" style="padding:0;Margin:0;font-size:0px"><a target="_blank"
                                                    href=""
                                                    style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;text-decoration:underline;color:#6A994E;font-size:16px"><img
                                                        class="adapt-img p_image"
                                                        src="{product_img}"
                                                        alt
                                                        style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;border-radius:10px"
                                                        width="195"></a></td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>
                        <!--[if mso]></td><td style="width:20px"></td><td style="width:345px" valign="top"><![endif]-->
                        <table cellpadding="0" cellspacing="0" class="es-right" align="right"
                            style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:right">
                            <tr>
                                <td align="left" style="padding:0;Margin:0;width:345px">
                                    <table cellpadding="0" cellspacing="0" width="100%"
                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:separate;border-spacing:0px;border-left:1px solid #386641;border-right:1px solid #386641;border-top:1px solid #386641;border-bottom:1px solid #386641;border-radius:10px"
                                        role="presentation">
                                        <tr>
                                            <td align="left" class="es-m-txt-c"
                                                style="Margin:0;padding-left:20px;padding-right:20px;padding-top:25px;padding-bottom:25px">
                                                <h3 class="p_name"
                                                    style="Margin:0;line-height:36px;mso-line-height-rule:exactly;font-family:Raleway, Arial, sans-serif;font-size:24px;font-style:normal;font-weight:normal;color:#386641">
                                                    {product_name}</h3>
                                                <p class="p_description"
                                                    style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:tahoma, verdana, segoe, sans-serif;line-height:24px;color:#4D4D4D;font-size:16px">
                                                    SKU: {product_sku}</p>
                                                <p
                                                    style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:tahoma, verdana, segoe, sans-serif;line-height:24px;color:#4D4D4D;font-size:16px">
                                                    QTY:&nbsp;{product_quantity}</p>
                                                <h3 style="Margin:0;line-height:36px;mso-line-height-rule:exactly;font-family:Raleway, Arial, sans-serif;font-size:24px;font-style:normal;font-weight:normal;color:#386641"
                                                    class="p_price">{product_price} each</h3>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table><!--[if mso]></td></tr></table><![endif]-->
                    </td>
                </tr>
            """
            email_data["email_products"] = (
                email_data["email_products"] + html_email_items
            )
            db.commit()
        history_sql = """
            INSERT INTO `Web_3dprints`.`orders__history`
                (`idorders`,
                `status_id`,
                `notes`,
                `updated_by`)
            VALUES
                (%s, %s, %s, 'checkout');
        """
        history_values = (
            order_id,
            order_status,
            f"{order_status_name} {data['paymentMethod']} Payment",
        )
        cursor.execute(history_sql, history_values)
        cursor.execute(empty_session_sql, session_id)
        db.commit()
        email = generate_email(email_data)
        email_prefix = ""
        if order_status == 3:
            email_thread = Process(
                target=send_email,
                args=(
                    data["emailAddress"],
                    f"{email_prefix}Kumpe3D Order {order_id}",
                    email,
                ),
            )
            email_thread2 = Process(
                target=send_email,
                args=(
                    "orders@kumpe3d.com",
                    f"{email_prefix}Kumpe3D Order {order_id}",
                    email,
                ),
            )
            email_thread2.daemon = True
            email_thread2.start()
            print_packing_slip(order_id)
        else:
            email_thread = Process(
                target=send_email,
                args=(
                    "sales@kumpe3d.com",
                    f"{email_prefix}PENDING Kumpe3D Order {order_id}",
                    email,
                ),
            )
        email_thread.daemon = True
        email_thread.start()

        db.close()
        notif_thread = Process(target=notif.new_order, args=(order_id,))
        notif_thread.daemon = True
        notif_thread.start()
        return (
            {"response": response, "status_code": 201},
            201,
            {"Access-Control-Allow-Origin": "*"},
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
    else:
        response["state_tax"] = 0

    if response["is_city_taxable"]:
        city_tax = subtotal * helpers.percent_to_float(response["city_tax_rate"])
        response["city_tax"] = round(city_tax, 2)
    else:
        response["city_tax"] = 0

    if response["is_county_taxable"]:
        county_tax = subtotal * helpers.percent_to_float(response["county_tax_rate"])
        response["county_tax"] = round(county_tax, 2)
    else:
        response["county_tax"] = 0

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
    email = json_args.get("email", "")
    country = json_args.get("country", "")
    shipping_address = {
        "fName": first_name,
        "lName": last_name,
        "company": company,
        "address": address,
        "address2": address2,
        "city": city,
        "state": state,
        "zip": zip_code,
        "country": country,
        "comments": comments,
        "email": email,
    }

    cart = get_cart(session_id, user_id)
    taxes = get_taxes(address, city, state, zip_code, cart["subtotal"])
    state_tax = taxes.get("state_tax", 0)
    county_tax = taxes.get("county_tax", 0)
    city_tax = taxes.get("city_tax", 0)
    paypal_transaction_id = args.get("paypal_transaction_id", "")
    tax_total = state_tax + county_tax + city_tax
    tax_total = round(tax_total, 2)
    try:
        tax_total = float(tax_total)
    except TypeError:
        tax_total = 0
    if country == "US":
        if cart["subtotal"] > 200:
            shipping_total = 0
        else:
            shipping_total = 10
    elif country == "CA":
        shipping_total = 20
    else:
        shipping_total = 25
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
