from django.contrib import admin
from .models import DndSpells


# Register your models here.
class DnDSpellAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'spell_name', 'school', 'level'
    )


admin.site.register(DndSpells, DnDSpellAdmin)