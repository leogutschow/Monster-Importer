from django.contrib import admin
from .models import DevLog, DevLogComment
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
class DevLogsAdmin(SummernoteModelAdmin):
    summernote_fields = ('devlog_text',)


class CommentariesAdmin(admin.ModelAdmin):
    pass

admin.site.register(DevLog, DevLogsAdmin)
admin.site.register(DevLogComment, CommentariesAdmin)
