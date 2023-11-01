"""REST API for Kumpe3D"""
import setup  # pylint: disable=unused-import, wrong-import-order
from flask import Flask
from flask_restful import Api
from header_data import HeaderData  # pylint: disable=no-name-in-module
from products import Product, ProductPrice, ProductImages, Filament
from siteparams import SiteParams
from cart import Cart
from orders import Checkout, ZipCodes, Taxes, CheckoutFinal
from shipping import Countries

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

# Get Shopping Cart
api.add_resource(Cart, "/cart")

# Checkout
api.add_resource(Checkout, "/checkout")

# Checkout
api.add_resource(CheckoutFinal, "/checkout-final")

# Filament
api.add_resource(Filament, "/filament")

# ZipCodes
api.add_resource(ZipCodes, "/zipcode")

# Tax Rates
api.add_resource(Taxes, "/taxes")

# Shipping Countries
api.add_resource(Countries, "/shipping/countries")


if __name__ == "__main__":
    app.run(port=8081)  # run our Flask app
