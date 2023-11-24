"""Products Function"""
import setup  # pylint: disable=unused-import, wrong-import-order
import logging
import json
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
logger = logging.getLogger("shippo")


class ShippoWebhook(Resource):
    """Shippo Webhook Functions"""

    def options(self):
        """Return Options for Inflight Browser Request"""
        res = Response()
        res.headers["Access-Control-Allow-Origin"] = "*"
        res.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        return res

    def post(self):
        """ShippoWebhook Post"""
        logger.debug("Start ShippoWebhook POST")
        json_args = request.get_json(force=True)
        data = json_args["data"]
        event = json_args["event"]
        if event == "track_updated":
            tracking_number = data["tracking_number"]
            tracking_status = data["tracking_status"]
            status = tracking_status["status"]
            carrier = data["carrier"]
            update_tracking(tracking_number, status, carrier)
        elif event == "transaction_created":
            metadata = data["metadata"]
            order_id = metadata.replace("Order ", "")
            tracking_number = data["tracking_number"]
            add_tracking_id(tracking_number, order_id)


def update_tracking(tracking_number: str, status: str, carrier: str):
    """Update Tracking Status"""
    sql_params = Params.SQL
    db = pymysql.connect(
        db=sql_params.database,
        user=sql_params.username,
        passwd=sql_params.password,
        host=sql_params.server,
        port=3306,
    )
    status_id = 14
    if status == "Delivered":
        status_id = 15
    cursor = db.cursor(pymysql.cursors.DictCursor)
    update_order_sql = """
            UPDATE `Web_3dprints`.`orders`
            SET
                `status_id` = %s,
                `last_updated_by` = 'shippo_api'
            WHERE `idorders` = (SELECT idorders FROM `Web_3dprints`.`orders__tracking` WHERE tracking_number = %s);
        """
    if status == "Delivered":
        cursor.execute(update_order_sql, (status_id, tracking_number))
    tracking_id_sql = """
            UPDATE `Web_3dprints`.`orders__tracking`
            SET status = %s, courier = %s
            WHERE tracking_number = %s;
        """
    cursor.execute(tracking_id_sql, (status, carrier, tracking_number))
    order_history = """
        INSERT INTO `Web_3dprints`.`orders__history`
            (
                `idorders`,
                `status_id`,
                `notes`,
                `updated_by`
            )
        VALUES
            (
                (SELECT idorders FROM `Web_3dprints`.`orders__tracking` WHERE tracking_number = %s),
                %s,
                %s,
                'ShippoAPI'
            );
    """
    cursor.execute(tracking_id_sql, (tracking_number, status_id, status))
    db.commit()
    db.close()


def add_tracking_id(tracking_number: str, order_id: int):
    """Add Tracking ID and mark order shipped"""
    sql_params = Params.SQL
    db = pymysql.connect(
        db=sql_params.database,
        user=sql_params.username,
        passwd=sql_params.password,
        host=sql_params.server,
        port=3306,
    )
    cursor = db.cursor(pymysql.cursors.DictCursor)
    update_order_sql = """
            UPDATE `Web_3dprints`.`orders`
            SET
                `status_id` = 14,
                `last_updated_by` = 'shippo_api'
            WHERE `idorders` = %s;
        """
    cursor.execute(update_order_sql, (order_id))
    add_tracking_id_sql = """
            INSERT INTO `Web_3dprints`.`orders__tracking`
                (
                    `idorders`,
                    `courier`,
                    `tracking_number`,
                    `tracking_status`
                )
            VALUES
                (
                    %s,
                    'Pending',
                    %s,
                    'Shipped'
                );
        """
    cursor.execute(add_tracking_id_sql, (order_id, tracking_number))
    db.commit()
    db.close()
