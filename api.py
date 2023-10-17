"""REST API for Kumpe3D"""
import setup  # pylint: disable=unused-import, wrong-import-order
from flask import Flask
from flask_restful import Api
from header_data import HeaderData  # pylint: disable=no-name-in-module
from products import Product, ProductPrice, ProductImages
from siteparams import SiteParams

# from flask_restful import Resource, Api, reqparse
# import pandas as pd
app = Flask(__name__)
api = Api(app)


# get_my_ip functions
api.add_resource(HeaderData, "/headerdata")

# Get Product info
api.add_resource(Product, "/product")

# Get Product Pricing
api.add_resource(ProductPrice, "/product-price")

# Get Site Params
api.add_resource(SiteParams, "/site-params")

# Get Product Images
api.add_resource(ProductImages, "/product-images")


if __name__ == "__main__":
    app.run(port=8081, debug=True)  # run our Flask app
