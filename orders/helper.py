import requests
import json

from django.http import HttpRequest

from carts.cart import Cart


MERCHANT = '17cd493d-318f-493d-830c-824abb60d16b'
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
email = 'pouyafarahanj@gmail.com'
mobile = '989301151298'

CallbackURL = 'http://localhost:8000/verify'


def send_request_to_zarinapl(request: HttpRequest, order_id: int) -> tuple[ZP_API_STARTPAY, str]:
    cart = Cart(request)
    amount = cart.get_total_price()
    description = f"شماره سفارش: {order_id}"
    req_data = {
        "merchant_id": MERCHANT,
        "amount": amount,
        "callback_url": CallbackURL,
        "description": description,
        "metadata": {"mobile": mobile, "email": email}
    }
    req_header = {"accept": "application/json",
                  "content-type": "application/json'"}
    req = requests.post(url=ZP_API_REQUEST, data=json.dumps(
        req_data), headers=req_header)
    authority = req.json()['data']['authority']
    if len(req.json()['errors']) == 0:
        return ZP_API_STARTPAY.format(authority=authority), authority
    else:
        e_code = req.json()['errors']['code']
        e_message = req.json()['errors']['message']
        raise Exception(f"Error code: {e_code}, Error Message: {e_message}")
