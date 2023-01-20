from django.urls import path

from .views import ProductListView, Details_view

app_name = 'products'

urlpatterns = [
    path('', ProductListView, name='products'),
    path('<int:pk>/', Details_view, name='product_detail'),
]
