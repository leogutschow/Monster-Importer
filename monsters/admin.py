from django.contrib import admin
from django.contrib.admin import TabularInline
from django.forms import TextInput, Textarea
from .models import DnDMonster, DnDAction, DnDSpecialTraits, DnDSkill, DnDSavingThrows
from django.db import models
from django.contrib.auth.models import Group


# Register your models here.
class DnDSkillInline(admin.StackedInline):
    model = DnDSkill
    extra = 0
    can_delete = True
    min_num = 0


class DnDActionInline(admin.TabularInline):
    model = DnDAction
    extra = 0
    can_delete = True
    min_num = 1
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '15'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 40})}
    }


class DnDSpecialTraitsInline(admin.TabularInline):
    model = DnDSpecialTraits
    extra = 0
    can_delete = True
    min_num = 0


class DndSavingThrowsInline(admin.TabularInline):
    model = DnDSavingThrows
    extra = 0
    can_delete = True
    min_num = 0


class DnDMonsterAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'ac', 'hp', 'challenge'
    )
    inlines = [DnDActionInline, DnDSpecialTraitsInline, DnDSkillInline, DndSavingThrowsInline]


admin.site.register(DnDMonster, DnDMonsterAdmin)
admin.site.unregister(Group)
admin.site.site_header = "Monster Importer Admin"



