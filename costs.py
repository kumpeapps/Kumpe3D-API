"""Get Costs"""
import setup  # pylint: disable=unused-import, wrong-import-order
import pymysql
from params import Params


def get_filament_cost(grams: int, swatch_id: str) -> float:
    """Get Filament Cost"""
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
        SELECT 
            ROUND(IFNULL(cost_per_g, 0.021), 3) AS cost_per_g
        FROM
            Web_3dprints.filament
        WHERE 1 = 1
            AND swatch_id = %s;
    """
    cursor.execute(sql, (swatch_id))
    filament = cursor.fetchone()
    cursor.close()
    db.close()
    filament_cost = filament["cost_per_g"] * grams
    return round(filament_cost, 3)


def get_product_costs(sku: str) -> float:
    """Get Product Costs"""
    base_sku = sku[:11]
    swatch_id = sku[-3:]
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
        SELECT 
            IFNULL(filament_usage, 0) AS filament_usage,
            addl_cost
        FROM
            Web_3dprints.products
        WHERE 1=1
            AND sku = %s;
    """
    cursor.execute(sql, (base_sku))
    product = cursor.fetchone()
    cursor.close()
    db.close()
    filament_cost = get_filament_cost(product["filament_usage"], swatch_id)
    product_cost = product["addl_cost"] + filament_cost
    return round(product_cost, 2)
