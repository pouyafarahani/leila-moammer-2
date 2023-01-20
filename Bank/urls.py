from django.urls import path
from . import views

app_name = 'bank'

urlpatterns = [
    path('check-in', views.Check_in, name='check_in'),
    path('check-in/<int:order_id>/', views.Check_in, name='check_in'),
]
