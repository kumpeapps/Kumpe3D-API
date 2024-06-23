"""K3D Label Printer Print Q"""

import setup  # pylint: disable=unused-import, wrong-import-order
import pymysql
from params import Params


def print_packing_slip(order_id: int):
    """Add Packing Slip to Print Q"""
    sql_params = Params.SQL
    db = pymysql.connect(
        db=sql_params.database,
        user=sql_params.username,
        passwd=sql_params.password,
        host=sql_params.server,
        port=3306,
    )
    cursor = db.cursor(pymysql.cursors.DictCursor)

    sql = """
        INSERT INTO `Automation_PrintQueue`.`kumpe3d_labels`
            (
            `sku`,
            `qr_data`,
            `label_type`,
            `distributor_id`,
            `qty`,
            `enable_print`
            )
        VALUES
            (
            %s,
            %s,
            'packing_slip',
            0,
            1,
            1
            );
    """

    cursor.execute(sql, (order_id, order_id))
    db.commit()
