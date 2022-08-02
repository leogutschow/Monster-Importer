from django.contrib import admin
from django.contrib.admin import TabularInline
from .models import Monster
from actions.models import Action


# Register your models here.
class MonsterAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'ac', 'hp', 'challenge', 'actions'
    )


admin.site.register(Monster, MonsterAdmin)
