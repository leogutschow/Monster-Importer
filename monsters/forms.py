from django.forms import ModelForm
from django import forms
from .models import BaseSheet, DnDMonster, DnDAction, games


class FormMonster(ModelForm):
    class Meta:
        model = BaseSheet
        fields = (
            'game', 'name', 'race', 'size', 'ac', 'ac_type', 'hp', 'hp_dices', 'movement', 'strength',
            'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma', 'languages', 'slug',
            'home_brew',
        )
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'race': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'size': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'ac': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'slug': forms.HiddenInput(),
            'home_brew': forms.HiddenInput()
        }


class FormDndMonster(ModelForm):
    class Meta:
        model = DnDMonster
        fields = (
            'alignment', 'challenge', 'description', 'image', 'senses', 'damage_resistances',
            'damage_immunities', 'condition_immunities',
        )
        widgets = {
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
            'monster': forms.HiddenInput(),
        }
