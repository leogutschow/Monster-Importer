from django.contrib import admin
from .models import Profile, Notification


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    pass


class NotificationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Notification, NotificationAdmin)
admin.site.register(Profile, ProfileAdmin)
