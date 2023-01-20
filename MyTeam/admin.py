from django.contrib import admin

from jalali_date.admin import ModelAdminJalaliMixin
from .models import UserOstadModel, MyTeamModel, DateTeamModel, RezervTeamModel, RezervOstadModel, DateOstadModel, \
    BokingDate,BokingDate_MyTeam

admin.site.register(MyTeamModel)
admin.site.register(UserOstadModel)
admin.site.register(BokingDate)
admin.site.register(BokingDate_MyTeam)
# admin.site.register(RezervTeamModel)


@admin.register(RezervTeamModel)
class DateTeamAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['name', 'last_name', 'phone', 'is_rezerv']


@admin.register(RezervOstadModel)
class DateTeamAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['khadamat', 'date', 'time', 'name', 'last_name', 'phone', 'is_rezerv']


@admin.register(DateTeamModel)
class DateTeamAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['team', 'time', 'date', 'is_rezerv']


@admin.register(DateOstadModel)
class DateOstadAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['user', 'time', 'date', 'is_rezerv']
