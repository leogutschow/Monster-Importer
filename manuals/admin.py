from django.contrib import admin
from .models import Manual


# Register your models here.
class ManualAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'language'
    ]

admin.site.register(Manual, ManualAdmin)
