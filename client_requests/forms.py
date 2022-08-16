from django import forms
from .models import Request


class FormRequest(forms.ModelForm):

    class Meta:
        model = Request
        fields: tuple = ('client', 'request_type', 'request_title', 'request_text')

        widgets: dict = {
            'client': forms.HiddenInput(),
        }
