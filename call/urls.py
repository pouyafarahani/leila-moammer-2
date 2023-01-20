from django.urls import path
from django.views.generic import TemplateView
from .views import AboutView, CallView, StudentView

app_name = 'call'

urlpatterns = [
    path('', CallView, name='call'),
    path('about-us/', AboutView, name='about'),
    path('honarjo/', StudentView, name='student'),
]
