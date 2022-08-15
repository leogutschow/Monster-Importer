from django.forms import ModelForm
from django import forms
from .models import BaseSheet, DnDMonster, DnDAction


class FormMonster(ModelForm):

    class Meta:
        model = BaseSheet
        fields = (
            'game', 'name', 'race', 'size', 'ac', 'ac_type', 'hp', 'hp_dices', 'movement', 'strength',
            'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma', 'languages', 'slug',
            'home_brew',
        )
        widgets = {
            'slug': forms.HiddenInput(),
            'home_brew': forms.HiddenInput()
        }


class FormDndMonster(ModelForm):

    class Meta:
        model = DnDMonster
        fields = (
            'game', 'name', 'race', 'size', 'ac', 'ac_type', 'hp', 'hp_dices', 'movement', 'strength',
            'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma', 'languages', 'slug',
            'home_brew', 'alignment', 'challenge', 'description', 'image', 'senses', 'damage_resistances',
            'damage_immunities', 'condition_immunities',
        )

        widgets = {
            'slug': forms.HiddenInput(),
            'home_brew': forms.HiddenInput()
        }


class FormAction(ModelForm):
    class Meta:
        model = DnDAction
        fields = (
            'monster', 'name', 'description', 'is_attack', 'weapon_type', 'attack', 'reach', 'hit',
            'hit_dice', 'damage_type',
        )
        widgets = {
            'monster': forms.HiddenInput(),
        }

