from django.contrib import admin
from .models import DevLog
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
class DevLogsAdmin(SummernoteModelAdmin):
    summernote_fields = ('devlog_text',)


admin.site.register(DevLog, DevLogsAdmin)
