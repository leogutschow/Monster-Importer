from django import forms
from .models import DevLogComment


class DevLogCommentForm(forms.ModelForm):
    class Meta:
        model = DevLogComment
        fields = ('commentary',)
        widgets = {
            'commentary': forms.Textarea(attrs={
                'class': 'form-control'
            }),
        }

