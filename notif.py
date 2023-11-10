"""Notification Scripts"""
import setup  # pylint: disable=unused-import, wrong-import-order
import http.client
import requests
import urllib
from params import Params


def new_order(order_number: int):
    """Send New Order Notification"""
    packing_slip = get_packing_slip(order_number)
    conn = http.client.HTTPSConnection(Params.Pushover.server)
    conn.request(
        "POST",
        "/1/messages.json",
        urllib.parse.urlencode(
            {
                "token": Params.Pushover.apikey,
                "user": Params.Pushover.orders_group,
                "title": f"New Kumpe3D Order {order_number}",
                "message": packing_slip,
                "url": f"{Params.base_url}/packing_slip?order_id={order_number}",
                "html": 1,
                "url_title": "View Packing Slip",
                "sound": "aol",
            }
        ),
        {"Content-type": "application/x-www-form-urlencoded"},
    )
    conn.getresponse()

def get_packing_slip(order_number: int):
    url = f"{Params.base_url}/packing_slip?order_id={order_number}"
    r = requests.get(url, timeout= 30)
    return r.content