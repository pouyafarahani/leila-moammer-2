import requests
import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from accounts.models import HistoryModel
from orders.models import Order
from carts.cart import Cart

MERCHANT = '17cd493d-318f-493d-830c-824abb60d16b'
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
email = 'pouyafarahanj@gmail.com'
mobile = '989301151298'
CallbackURL = 'http://localhost:8000/verify'


def verify(request):
    cart = Cart(request)
    amount = cart.get_total_price()
    t_status = request.GET.get('Status')
    t_authority = request.GET['Authority']
    order = Order.objects.get(authority=t_authority)
    if not order:
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
                order.is_paid = True
                order.save()
                for his in cart:
                    product = his['product_obj']
                    HistoryModel.objects.create(
                        user=request.user,
                        quantity=his['quantity'],
                        product=product,
                        get_total_price=product.price
                    )
                cart.clear()
                messages.success(request, 'خرید شما با موفقیت انجام شد')
                return redirect('accounts:profile')
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


@login_required()
def Check_in(request):
    order = Order.objects.all()
    cart = Cart(request)
    return render(request, 'bank/check_in.html', {'cart': cart, 'order': order})
