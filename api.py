"""REST API for Kumpe3D"""
import setup # pylint: disable=unused-import, wrong-import-order
import ast
from flask import request
from flask import jsonify
from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
app = Flask(__name__)
api = Api(app)

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    response = jsonify({'ip': request.environ['HTTP_X_FORWARDED_FOR'], 'environ': request})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(port=8081,debug=True)  # run our Flask app