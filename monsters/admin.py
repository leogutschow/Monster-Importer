from django.contrib import admin
from django.contrib.admin import TabularInline
from django.forms import TextInput, Textarea
from .models import Monster, Action, SpecialTraits, Skill
from django.db import models


# Register your models here.
class SkillInline(admin.StackedInline):
    model = Skill
    extra = 0
    can_delete = True
    min_num = 0


class ActionInline(admin.TabularInline):
    model = Action
    extra = 0
    can_delete = True
    min_num = 1
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '15'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 40})}
    }


class SpecialTraitsInline(admin.TabularInline):
    model = SpecialTraits
    extra = 0
    can_delete = True
    min_num = 0


class MonsterAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'ac', 'hp', 'challenge'
    )
    inlines = [ActionInline, SpecialTraitsInline, SkillInline]


admin.site.register(Monster, MonsterAdmin)



