"""REST API for Kumpe3D"""
import setup  # pylint: disable=unused-import, wrong-import-order
from flask import request
from flask import jsonify
from flask import Flask
from flask_restful import Api
from header_data import HeaderData
import header_data

# from flask_restful import Resource, Api, reqparse
# import pandas as pd
app = Flask(__name__)
api = Api(app)


# get_my_ip functions
api.add_resource(header_data, "/headerdata")

def get_product():
    pass


if __name__ == "__main__":
    app.run(port=8081, debug=True)  # run our Flask app
