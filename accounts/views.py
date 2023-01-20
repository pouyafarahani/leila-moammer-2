from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from carts.cart import Cart
from .forms import RegisterForm
from .models import HistoryModel


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home:home')
        else:
            return render(request, 'registration/signup.html', {'forms': form})
    else:
        form = RegisterForm()
    return render(request, 'registration/signup.html')


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        redirect(request, 'home/home.html')

    else:
        pass


@login_required()
def ProfileView(request):
    cart = Cart(request)
    user = HistoryModel.objects.filter(user=request.user)
    return render(request, 'account/profile.html', {'cart': cart, 'clients': user})

