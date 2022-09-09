from django.forms.models import ModelForm
from django.forms import HiddenInput
from .models import Request


class FormRequest(ModelForm):

    class Meta:
        model = Request
        fields = (
            'client', 'request_type', 'request_title', 'request_text'
        )
        widgets = {
            'client': HiddenInput()
        }
