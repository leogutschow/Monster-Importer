from django.contrib import admin
from .models import Action


# Register your models here.
class ActionAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name'
    ]


admin.site.register(Action, ActionAdmin)
