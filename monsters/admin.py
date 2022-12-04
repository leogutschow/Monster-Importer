from django.contrib import admin
from django.contrib.admin import TabularInline
from django.forms import TextInput, Textarea
from .models import *
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


class DndReactionInline(admin.TabularInline):
    model = DndReaction
    extra = 0
    can_delete = True
    min_num = 0


class DnDMonsterAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'ac', 'hp', 'challenge', 'game'
    )
    search_fields = (
        'name', 'game'
    )
    inlines = [DnDActionInline, DnDSpecialTraitsInline, DnDSkillInline, DndSavingThrowsInline, DndReactionInline]


class Tor20SkillInline(admin.StackedInline):
    model = Tor20Skill
    extra = 0
    min_num = 0
    can_delete = True


class Tor20GenericActionInline(admin.TabularInline):
    model = Tor20GenericAction
    extra = 0
    min_num = 0
    can_delete = 0
    can_delete = True


class Tor20MeleeActionInline(admin.TabularInline):
    model = Tor20MeleeAction
    extra = 0
    min_num = 0
    can_delete = 0
    can_delete = True


class Tor20RangedActionInline(admin.TabularInline):
    model = Tor20RangedAction
    extra = 0
    min_num = 0
    can_delete = True


class Tor20MonsterAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'ac', 'hp', 'challenge', 'game'
    )
    search_fields = (
        'name', 'game'
    )
    inlines = [Tor20SkillInline, Tor20GenericActionInline, Tor20MeleeActionInline, Tor20RangedActionInline, ]


class PathFinderSkillInline(admin.TabularInline):
    model = PathFinderSkill
    extra = 0
    min_num = 0
    can_delete = True


class PathFinderSpecialAbilityInline(admin.TabularInline):
    model = PathFinderSpecialAbility
    extra = 0
    min_num = 0
    can_delete = True


class PathFinderOffenseInline(admin.TabularInline):
    model = PathFinderOffense
    extra = 0
    min_num = 0
    can_delete = True


class PathFinderMonsterAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'ac', 'hp', 'challenge', 'game'
    )
    search_fields = (
        'name', 'game'
    )
    inlines = [PathFinderOffenseInline, PathFinderSkillInline, PathFinderSpecialAbilityInline, ]


class CoCSpecialPowerInline(admin.TabularInline):
    model = CoCSpecialPowers
    extra = 0
    min_num = 0
    can_delete = True


class CoCMoveInline(admin.TabularInline):
    model = CoCMove
    extra = 0
    min_num = 0
    can_delete = True


class CoCSkillInline(admin.TabularInline):
    model = CoCSkill
    extra = 0
    min_num = 0
    can_delete = 0


class CoCMonsterAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'hp', 'type', 'game'
    )
    search_fields = (
            'name', 'game'
    )
    inlines = [CoCMoveInline, CoCSpecialPowerInline, CoCSkillInline]


admin.site.register(Tor20Monster, Tor20MonsterAdmin)
admin.site.register(DnDMonster, DnDMonsterAdmin)
admin.site.register(PathFinderMonster, PathFinderMonsterAdmin)
admin.site.register(CoCMonster, CoCMonsterAdmin)
admin.site.unregister(Group)
admin.site.site_header = "Monster Importer Admin"



