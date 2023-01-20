from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpRequest
from django.contrib import messages
from django.db import transaction

from carts.cart import Cart
from .forms import OrderForms
from .models import OrderItem
from accounts.models import HistoryModel
from .helper import send_request_to_zarinapl
import logging


@transaction.atomic
def Check_is_valid(request: HttpRequest) -> HttpResponse:
    cart = Cart(request)
    if request.method == 'POST':
        order = OrderForms(request.POST)
        if order.is_valid():
            order_new = order.save(commit=False)
            order_new.user = request.user
            order_new.save()
            for item in cart:
                product = item['product_obj']
                OrderItem.objects.create(
                    order=order_new,
                    product=product,
                    quantity=item['quantity'],
                    price=product.price
                )
            request.user.first_name = order_new.first_name
            request.user.last_name = order_new.last_name
            request.user.save()
            try:
                redirect_url, authority = send_request_to_zarinapl(request, order_id=order_new.id)
                order_new.authority = authority
                order_new.save()
                return redirect(redirect_url)
            except Exception as e:
                logging.error(e)
                response = HttpResponse("خطایی در سفارش پیش آمده است.")
                response.status_code = 406
                return response
        else:
            error = messages.error(request, 'فرم کامل نیست')
            return render(request, 'bank/check_in.html', {'error': error})
    else:
        return render(request, 'home/home.html')
