from django.forms.models import ModelForm
from django import forms
from django.forms import HiddenInput
from .models import Request


class FormRequest(ModelForm):

    class Meta:
        model = Request
        fields = (
            'client', 'request_type', 'request_title', 'request_text'
        )
        widgets = {
            'client': HiddenInput(),
            'request_type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'request_title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'request_text': forms.Textarea(attrs={
                'class': 'form-control'
            }),
        }