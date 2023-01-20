from django.contrib import admin
from .models import Product, Comment
from jalali_date.admin import ModelAdminJalaliMixin


class CommentProduct(admin.TabularInline):
    model = Comment
    fields = ['text', 'user',  'product', ]


@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'price', ]
    inlines = [
        CommentProduct,
    ]


@admin.register(Comment)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['user', ]
