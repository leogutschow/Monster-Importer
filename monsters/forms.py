from django.forms import ModelForm
from django import forms
from .models import BaseSheet, DnDMonster, DnDAction, DnDSpecialTraits, games


class FormMonster(ModelForm):
    class Meta:
        model = BaseSheet
        fields = (
            'game', 'name', 'race', 'size', 'ac', 'ac_type', 'hp', 'hp_dices', 'movement', 'strength',
            'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma', 'languages', 'slug',
            'home_brew',
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
            'languages': forms.TextInput(attrs={
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
            'alignment': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'challenge': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'image': forms.FileInput(attrs={
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