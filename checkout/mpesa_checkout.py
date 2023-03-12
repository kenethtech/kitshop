import base64
import datetime
from kitshop import settings
import requests
import json


def mpesa_payment(phone_number, amount, access_token):
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": f"Bearer {access_token}"}
    request = {
        "BusinessShortCode": settings.MPESA_SHORTCODE,
        "Password":get_password(),
        "Timestamp": get_timestamp(),
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": settings.MPESA_SHORTCODE,
        "PhoneNumber": phone_number,
        "CallBackURL": settings.CALLBACK_URL,
        "AccountReference": "MPESA Payment Gateway",
        "TransactionDesc": "Testing Lipa Na M-pesa"

    }
    response = requests.post(api_url, json=request, headers=headers)
    return json.loads(response.text)
def get_password():
    timestamp = get_timestamp()
    business_short_code = settings.MPESA_SHORTCODE
    passkey = settings.MPESA_PASSKEY
    raw_password = f"{business_short_code}{passkey}{timestamp}"
    password = base64.b64encode(raw_password.encode())
    return password.decode('utf-8')

def get_timestamp():
    return datetime.datetime.now().strftime('%Y%m%d%H%M%S')