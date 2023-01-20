from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext as _


# Create your models here.
class Product(models.Model):
    title = models.CharField(_('title'), max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(_('price'), default=0)
    image = models.ImageField(_('Image'), blank=True, upload_to='product/product_cover')

    datetime_create = models.DateTimeField(_('time product create'), default=timezone.now)
    datetime_edit = models.DateTimeField(_('time product edit'), auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.pk])


class Comment(models.Model):
    PRODUCT_STARS = [
        ('1', 'very Bad'),
        ('2', 'Bad'),
        ('3', 'Normal'),
        ('4', 'Good'),
        ('5', 'very Good'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    datetime_create = models.DateTimeField(auto_now_add=True)

    text = models.TextField('نظر', blank=False, null=False)

    def __str__(self):
        return self.text
