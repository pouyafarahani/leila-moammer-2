from django.contrib.auth.models import AbstractUser
from django.db import models
from config.settings import AUTH_USER_MODEL


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=11)


class HistoryModel(models.Model):
    STATUS_CHOICES = (
        ('درحال رسیدگی', 'درحال رسیدگی'),
        ('محصول ارسال شده است', 'محصول ارسال شده است'),
    )
    get_total_price = models.PositiveIntegerField(blank=True, null=True)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)

    status = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True, blank=True, default='درحال رسیدگی')
    Datetime = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'user: {self.user.username}/ {self.product}/ {self.status}'
