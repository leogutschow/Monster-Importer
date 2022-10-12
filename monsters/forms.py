from django.forms import ModelForm
from django import forms
from .models import BaseSheet, DnDMonster, DnDAction, DnDSpecialTraits, DnDSkill, DnDLegendaryAction, \
    DnDSavingThrows, DndReaction, Tor20Monster, Tor20GenericAction, \
    Tor20RangedAction, Tor20MeleeAction, Tor20Skill, PathFinderMonster, games, \
    PathFinderSpecialAbility, PathFinderOffense, PathFinderSkill


class FormMonster(ModelForm):
    class Meta:
        model = BaseSheet
        fields = (
            'game', 'name', 'race', 'size', 'ac', 'ac_type', 'hp', 'hp_dices', 'movement', 'strength',
            'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma', 'slug',
            'home_brew', 'image', 'description',
        )
        widgets = {
            'game': forms.Select(attrs={
                'class': 'form-select form-select-lg'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg'
            }),
            'race': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'size': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'ac': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'ac_type': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'hp': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'hp_dices': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'movement': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'strength': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'dexterity': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'constitution': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'intelligence': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'wisdom': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'charisma': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'slug': forms.HiddenInput(),
            'home_brew': forms.HiddenInput()
        }


class FormDndMonster(ModelForm):
    class Meta:
        model = DnDMonster
        fields = (
            'languages', 'alignment', 'challenge', 'description', 'senses', 'damage_resistances',
            'damage_immunities', 'condition_immunities',
        )
        widgets = {
            'languages': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'alignment': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'challenge': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'senses': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'damage_resistances': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'damage_immunities': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'condition_immunities': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'slug': forms.HiddenInput(),
            'home_brew': forms.HiddenInput()
        }


class FormDnDAction(ModelForm):
    class Meta:
        model = DnDAction
        fields = (
            'monster', 'action_name', 'action_description', 'is_attack', 'weapon_type', 'attack', 'reach', 'hit',
            'hit_dice', 'damage_type',
        )
        widgets = {
            'action_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'action_description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'is_attack': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'weapon_type': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'attack': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'reach': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'hit': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'hit_dice': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'damage_type': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'monster': forms.HiddenInput(),
        }


class FormDndTrait(ModelForm):
    class Meta:
        model = DnDSpecialTraits
        fields = (
            'monster', 'specialtrait_name', 'specialtrait_description', 'spellcasting', 'dnd_spells'
        )
        widgets = {
            'specialtrait_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'specialtrait_description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'spellcasting': forms.CheckboxInput(attrs={
                'class': 'form-check-input col'
            }),
            'dnd_spells': forms.SelectMultiple(attrs={
                'class': 'form-control form-select form-select-sm col'
            }),
            'monster': forms.HiddenInput()
        }


class FormDnDSkill(ModelForm):
    class Meta:
        model = DnDSkill
        fields = (
            'monster', 'skill_name', 'modifier'
        )
        widgets = {
            'monster': forms.HiddenInput(),
            'skill_name': forms.Select(attrs={
                'class': 'form-control'
            }),
            'modifier': forms.NumberInput(attrs={
                'class': 'form-control'
            })
        }


class FormDnDLegendaryAction(ModelForm):
    class Meta:
        model: DnDLegendaryAction
        fields = (
            'monster', 'legendary_name', 'legendary_description'
        )
        widgets = {
            'monster': forms.HiddenInput(),
            'legendary_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'legendary_description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
        }


class FormDnDSavingThrow(ModelForm):
    class Meta:
        model = DnDSavingThrows
        fields = (
            'monster', 'attr', 'bonus'
        )
        widgets = {
            'monster': forms.HiddenInput(),
            'attr': forms.Select(attrs={
                'class': 'form-control'
            }),
            'bonus': forms.NumberInput(attrs={
                'class': 'form-control'
            })
        }


class FormDnDReaction(ModelForm):
    class Meta:
        model = DndReaction
        fields = (
            'monster', 'reaction_name', 'reaction_description'
        )
        widgets = {
            'monster': forms.HiddenInput(),
            'reaction_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'reaction_description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
        }


class FormTor20Monster(ModelForm):
    class Meta:
        model = Tor20Monster
        fields = (
            'description', 'fortitude', 'reflex', 'will', 'level', 'mana', 'equipment', 'treasure',
        )
        widgets = {
            'fortitude': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'reflex': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'will': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'level': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'mana': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'equipment': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'treasure': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }


class FormTor20GenericAction(ModelForm):
    class Meta:
        model = Tor20GenericAction
        fields = (
            'monster', 'action_name', 'action_description', 'action_type',
            'mana_cost'
        )
        widgets = {
            'monster': forms.HiddenInput(),
            'action_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'action_description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'action_type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'mana_cost': forms.NumberInput(attrs={
                'class': 'form-control'
            })
        }


class FormTor20BaseAttack(ModelForm):
    class Meta:
        fields = (
            'monster', 'action_name', 'action_description', 'attack', 'hit'
        )
        widgets = {
            'monster': forms.HiddenInput(),
            'action_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'action_description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'attack': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'hit': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }


class FormPFMonster(ModelForm):
    class Meta:
        model = PathFinderMonster
        fields = (
            'monster_class', 'monster_alignment', 'type', 'subtype', 'init', 'senses',
            'aura', 'ac_mod', 'hp_mod', 'fortitude', 'reflex', 'will', 'save_mods', 'damage_reduction',
            'immune', 'resist', 'spell_resistence', 'weaknesses', 'feats', 'speed_mod', 'space', 'reach',
            'spell_domain', 'base_attack', 'combat_maneuver_bonus', 'combat_maneuver_defence', 'languages',
            'special_qualities', 'environment', 'organization', 'treasure',
        )
        widgets = {
            'monster_class': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'monster_alignment': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'type': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'subtype': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'init': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'senses': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'aura': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'ac_mod': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'hp_mod': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'fortitude': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 0
            }),
            'reflex': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 0
            }),
            'will': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 0
            }),
            'save_mods': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'damage_reduction': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'immune': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'resist': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'spell_resistence': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'weaknesses': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'feats': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'speed_mod': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'space': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'reach': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'spell_domain': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'base_attack': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'combat_maneuver_bonus': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'combat_maneuver_defence': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'languages': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'special_qualities': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'environment': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'organization': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'treasure': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }


class FormPFSkill(ModelForm):
    class Meta:
        model = PathFinderSkill
        fields = (
            'monster', 'skill', 'skill_bonus', 'racial_mod'
        )
        widgets = {
            'monster': forms.HiddenInput(),
            'skill': forms.Select(attrs={
                'class': 'form-control'
            }),
            'skill_bonus': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'racial_mod': forms.HiddenInput()
        }


class FormPFOffense(ModelForm):
    class Meta:
        model = PathFinderOffense
        fields = (
            'monster', 'name', 'type', 'attack', 'effect', 'crit_range', 'multiple', 'damage', 'count'
        )
        widgets = {
            'monster': forms.HiddenInput(),
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'type': forms.Select(attrs={
                'class': 'form-select form-select-lg'
            }),
            'attack': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'effect': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'crit_range': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'multiple': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'damage': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'count': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 1
            })
        }


class FormPFSpecialAbility(ModelForm):
    class Meta:
        model = PathFinderSpecialAbility
        fields = (
            'monster', 'name', 'description'
        )
        widgets = {
            'monster': forms.HiddenInput(),
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control'
            })
        }
