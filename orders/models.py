from django.db import models
from django.urls import reverse

from config import settings


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)

    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=12, null=False, blank=False)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=700, null=True, blank=True)
    time = models.DateTimeField(auto_now=True)
    authority = models.CharField(max_length=128, null=True, blank=True, unique=True)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('order:check_is_valid_id', args=[self.id])


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='item')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='order_item')
    quantity = models.PositiveIntegerField(default=1, null=False, blank=False)
    price = models.PositiveIntegerField(null=False, blank=False)

    def __str__(self):
        return f'OrderItem {self.id}: {self.product} x {self.quantity} (price:{self.price}'

