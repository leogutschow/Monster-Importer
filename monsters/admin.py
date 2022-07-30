from django.contrib import admin
from .models import Monster

# Register your models here.
class MonsterAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'ac', 'hp', 'challenge',
    )


admin.site.register(Monster, MonsterAdmin)
