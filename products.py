"""Products Function"""
import setup  # pylint: disable=unused-import, wrong-import-order
from flask import request
from flask import jsonify, json
from flask_restful import Resource
from flask_restful import reqparse
import pymysql
from params import Params
import helper_funcs as helpers


class Product(Resource):
    """Product Functions"""

    sql_params = Params.SQL
    db = pymysql.connect(
        db=sql_params.database,
        user=sql_params.username,
        passwd=sql_params.password,
        host=sql_params.server,
        port=3306,
    )

    def get(self):
        """Get Product Data"""
        db = self.db
        # parser = reqparse.RequestParser()  # initialize
        # parser.add_argument("sku", required=True)  # add required argument
        # args = parser.parse_args()  # parse arguments to dictionary
        sku = helpers.get_sku_array('alo-poo-lsn')
        cursor = db.cursor(pymysql.cursors.DictCursor)
        sql = "CALL get_products(%s, %s, %s)"
        cursor.execute(sql, (sku["base_sku"],'%', '%'))
        results = cursor.fetchone()
        results = json.dumps(results, default=str)
        response = jsonify(results)
        # response.headers.add("Access-Control-Allow-Origin", "*")
        # response.mimetype = "application/json"
        cursor.close()
        db.close()
        return {'response': response}, 200, {"Access-Control-Allow-Origin": "*"}
