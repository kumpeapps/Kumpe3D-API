"""Notification Scripts"""
import setup # pylint: disable=unused-import, wrong-import-order
import http.client
import urllib
from params import Params


def new_order(order_number: int):
    """Send New Order Notification"""
    conn = http.client.HTTPSConnection(Params.Pushover.server)
    conn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
        "token": Params.Pushover.apikey,
        "user": Params.Pushover.orders_group,
        "title": f"New Kumpe3D Order {order_number}",
        "message": f"A new order has been submitted. The order number is {order_number}.",
        "url": f"{Params.base_url}/packing_slip?order_id={order_number}",
        "sound": "aol"
    }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()
new_order("32")