from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import RegisterForm
from .models import CustomUser, HistoryModel


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = RegisterForm
    list_display = ['username', 'password', 'phone']


admin.site.register(HistoryModel)
