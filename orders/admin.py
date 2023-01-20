from django.contrib import admin
from .models import Order, OrderItem
from jalali_date.admin import ModelAdminJalaliMixin


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ['order', 'product', 'quantity', 'price', ]
    extra = 1


@admin.register(Order)
class OrderAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'city', 'address', 'user', 'is_paid', 'id', ]
    inlines = [
        OrderItemInline,
    ]


@admin.register(OrderItem)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price', ]
