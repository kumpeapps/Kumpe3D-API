"""REST API for Kumpe3D"""
import setup  # pylint: disable=unused-import, wrong-import-order
from flask import Flask
from flask import jsonify, request
from flask_restful import Api
from flask_cors import CORS, cross_origin
# from header_data import HeaderData  # pylint: disable=no-name-in-module
# from products import Product

# from flask_restful import Resource, Api, reqparse
# import pandas as pd
app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


# get_my_ip functions
# api.add_resource(HeaderData, "/headerdata")


# api.add_resource(Product, "/headerdata")
@app.route('/headerdata')
@cross_origin
def headerdata():
    """Displays User IP and referrer"""
    response = jsonify(
        {
            "ip": request.environ["HTTP_X_FORWARDED_FOR"],
            "referrer": request.environ["HTTP_REFERER"],
        }
    )
    return response, 201, {"Access-Control-Allow-Origin": "*"}


if __name__ == "__main__":
    app.run(port=8081, debug=True)  # run our Flask app
