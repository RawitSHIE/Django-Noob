
from django.contrib import admin
from polls.models import Dayoff



class DayoffAdmin(admin.ModelAdmin):
    list_display = ['id','create_by','reason','date_start','date_end','approve_status']
    list_filter = ['create_by', 'date_start', 'date_end', 'approve_status']
    fieldsets = (
        ('ข้อมูลการลา', {
            'fields': ['create_by', 'reason', 'date_start', 'date_end', 'type' ]
        }),
        ('การอนุมัติ', {
            'fields': ['approve_status', ]
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['create_by', 'reason', 'type', 'date_start', 'date_end']
        else:
            return ['approve_status']


admin.site.register(Dayoff, DayoffAdmin)