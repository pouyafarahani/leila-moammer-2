import requests
import json

from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from MyTeam.models import RezervOstadModel

MERCHANT = '17cd493d-318f-493d-830c-824abb60d16b'
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
email = 'pouyafarahanj@gmail.com'
mobile = '989301151298'

CallbackURL = 'https://leilamoammer.ir/rezerv-ostad-verify/'


def send_request_to_rezerv_ostad_zarinapl(request: HttpRequest, rezerv_ostad_id: int) -> tuple[ZP_API_STARTPAY, str]:
    amount = 50000
    print('helloiddddddddddddddddd', rezerv_ostad_id)
    description = f"شماره سفارش: {rezerv_ostad_id}"
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


def verifyrezerostad(request):
    amount = 50000
    t_status = request.GET.get('Status')
    t_authority = request.GET['Authority']
    rezerv = RezervOstadModel.objects.get(authority=t_authority)
    if not rezerv:
        response = HttpResponse("I'm a teapot")
        response.status_code = 418
        return response
    if request.GET.get('Status') == 'OK':
        req_header = {"accept": "application/json",
                      "content-type": "application/json'"}
        req_data = {
            "merchant_id": MERCHANT,
            "amount": amount,
            "authority": t_authority,
        }
        req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
        if len(req.json()['errors']) == 0:
            t_status = req.json()['data']['code']
            if t_status == 100:
                rezerv.is_rezerv = True
                rezerv.save()
                messages.success(request, 'رزرو شما با موفقیت ثبت شد')
                return render(request, 'home/home.html')
            elif t_status == 101:
                return HttpResponse('Transaction submitted : ' + str(
                    req.json()['data']['message']
                ))
            else:
                return HttpResponse('Transaction failed.\nStatus: ' + str(
                    req.json()['data']['message']
                ))
        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
    else:
        return HttpResponse('Transaction failed or canceled by user')
