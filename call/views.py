from django.shortcuts import render
from django.views.generic import TemplateView

from carts.cart import Cart
from MyTeam.models import MyTeamModel, UserOstadModel


def CallView(request):
    cart = Cart(request)
    return render(request, 'call/call.html', {'cart': cart})


def StudentView(request):
    cart = Cart(request)
    return render(request, 'call/student.html', {'cart': cart})


def AboutView(request):
    teams = MyTeamModel.objects.all()
    ostads = UserOstadModel.objects.all()
    cart = Cart(request)
    return render(request, 'call/about_we.html', {'teams': teams, 'ostads': ostads, 'cart': cart})
