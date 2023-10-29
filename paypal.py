"""PayPal Functions"""
import requests
from params import Params


def get_orders(trasaction_id: str) -> dict:
    """Get Orders"""
    auth = authenticate()
    token = auth["access_token"]
    headers = {
        "Authorization": f"Bearer {token}",
    }

    response = requests.get(
        f"{Params.PayPal.api_url}/v2/checkout/orders/{trasaction_id}",
        headers=headers,
        timeout=30,
    )
    return response.json()


def verify_order(transaction_id: str) -> bool:
    """Verify PayPal Transaction"""
    transaction_data = get_orders(transaction_id)
    status = transaction_data.get("status", "Failed")
    if status == "COMPLETED":
        return True
    else:
        return False


def authenticate() -> dict:
    """Authenticate to Get Bearer Token"""
    data = {
        "grant_type": "client_credentials",
    }

    response = requests.post(
        f"{Params.PayPal.api_url}/v1/oauth2/token",
        data=data,
        auth=(Params.PayPal.client_id, Params.PayPal.secret),
        timeout=30,
    )
    return response.json()
