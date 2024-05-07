"""Zoho Books Webhooks"""
import setup  # pylint: disable=unused-import, wrong-import-order
import logging
from multiprocessing import Process
from flask import request, Response
from flask_restful import Resource
import notif

# from flask_restful import reqparse
import pymysql
from params import Params
import helper_funcs as helpers

logging.basicConfig(
    filename="kumpe3d-api.log",
    filemode="a",
    format="%(asctime)s: [%(name)s] [%(levelname)s] %(message)s",
    level=Params.log_level(),
)
logger = logging.getLogger("zoho")


class Zoho(Resource):
    """Product Functions"""
    logger = logging.getLogger("zoho")
    def post(self):
        """Get Product Data"""
        sql_params = Params.SQL
        db = pymysql.connect(
            db=sql_params.database,
            user=sql_params.username,
            passwd=sql_params.password,
            host=sql_params.server,
            port=3306,
        )
        cursor = db.cursor(pymysql.cursors.DictCursor)
        logger.debug("start get")
        json_args = request.get_json(force=True)
        self.logger.debug("JSON ARGS: %s", json_args)
        sales_order = json_args["salesorder"]
        items = sales_order['line_items']
        po_number = sales_order['reference_number']
        salesorder_number = sales_order['salesorder_number']
        salesorder_id = sales_order['salesorder_id']
        zoho_cust_id = sales_order['customer_id']
        email = sales_order['contact_person_details'][0]["email"]
        shipping_address = sales_order['shipping_address']

        orders_sql = """
                    INSERT INTO `Web_3dprints`.`orders`
                        (`idcustomers`,
                        `distributor_id`,
                        `po_number`,
                        `so_number`,
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
                        `notes`,
                        `sales_channel`,
                        `last_updated_by`)
                    VALUES
                        (0,
                        (SELECT iddistributors FROM Web_3dprints.distributors where zoho_cust_id = %s),
                        %s,
                        %s,
                        "",
                        "",
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        3,
                        'purchase_order',
                        %s,
                        'Distributor',
                        'ZohoBooks');
        """
        orders_values = (
            zoho_cust_id,
            po_number,
            salesorder_number,
            shipping_address['attention'],
            email,
            shipping_address['address'],
            shipping_address['street2'],
            shipping_address['city'],
            shipping_address['state_code'],
            shipping_address['zip'],
            shipping_address['country_code'],
            sales_order['sub_total'],
            sales_order['tax_total'],
            sales_order['shipping_charge'],
            sales_order['discount_total'],
            sales_order['total'],
            sales_order['date'],
            sales_order['notes']
        )
        try:
            cursor.execute(orders_sql, orders_values)
            db.commit()
        except:
            pass
        order_id = cursor.lastrowid

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

        for item in items:
            item_values = (
                order_id,
                item["sku"],
                item["name"],
                item["rate"],
                item["quantity"],
                0,
            )
            try:
                cursor.execute(items_sql, item_values)
                db.commit()
            except:
                pass
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
                3,
                f"Zoho Sales Order #{salesorder_number}",
            )
            try:
                cursor.execute(history_sql, history_values)
                db.commit()
                db.close()
            except:
                pass
            notif_thread = Process(target=notif.new_order, args=(order_id,))
            notif_thread.daemon = True
            notif_thread.start()


        return (
            {"response": "response", "status_code": 200},
            200,
            {"Access-Control-Allow-Origin": "*"},
        )
