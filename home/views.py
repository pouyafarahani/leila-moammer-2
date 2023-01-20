from django.shortcuts import render
from carts.cart import Cart
from MyTeam.models import MyTeamModel, UserOstadModel


def HomeView(request):
    cart = Cart(request)
    teams = MyTeamModel.objects.all()
    ostad = UserOstadModel.objects.all()
    return render(request, 'home/home.html', {'teams': teams, 'ostads': ostad, 'cart': cart})
