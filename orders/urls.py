from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('check/', views.Check_is_valid, name='check_is_valid'),
]
