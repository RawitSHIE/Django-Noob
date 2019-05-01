
from django.contrib import admin
from polls.models import Dayoff



class DayoffAdmin(admin.ModelAdmin):
    list_display = ['id','create_by','reason','date_start','date_end','approve_status']

admin.site.register(Dayoff, DayoffAdmin)