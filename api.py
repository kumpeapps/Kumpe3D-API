"""REST API for Kumpe3D"""
import setup # pylint: disable=unused-import, wrong-import-order
from flask import request
from flask import jsonify
from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
app = Flask(__name__)
api = Api(app)

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200
