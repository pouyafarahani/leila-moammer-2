"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from azbankgateways.urls import az_bank_gateways_urls

from Bank import views
from MyTeam import rezerv_helper, helper_rezerv_ostad
from MyTeam.views import checkyear, checkmounth, checkrooztime, reserv,checkmounth_team,checkyear_team,checkrooztime_team,reserv_team
from config import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('bankgateways/', az_bank_gateways_urls()),
                  path('', include('home.urls')),
                  path('products/', include('products.urls')),
                  path('call/', include('call.urls')),
                  path('my-team/', include('MyTeam.urls')),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('accounts/', include('accounts.urls')),
                  path('cart/', include('carts.urls')),
                  path('verify/', views.verify, name='verify'),
                  path('rezerv-verify/', rezerv_helper.verifyrezervteam, name='rezerv_verify'),
                  path('rezerv-ostad-verify/', helper_rezerv_ostad.verifyrezerostad, name='rezerv_ostad_verify'),
                  path('bank/', include('Bank.urls')),
                  path('is-valid', include('orders.urls')),
                  path('checkyear', checkyear, name='checkyear'),
                  path('checkmounth', checkmounth, name='checkmounth'),
                  path('checkrooztime', checkrooztime, name='checkrooztime'),
                  path('reserv', reserv, name='reserv'),
                  path('checkyear_team', checkyear_team, name='checkyear_team'),
                  path('checkmounth_team', checkmounth_team, name='checkmounth_team'),
                  path('checkrooztime_team', checkrooztime_team, name='checkrooztime_team'),
                  path('reserv_team', reserv_team, name='reserv_team'),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
