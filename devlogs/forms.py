from django import forms
from .models import DevLogCommentary


class DevLogCommentaryForm(forms.ModelForm):
    class Meta:
        model = DevLogCommentary
        fields = ('devlog', 'author', 'commentary', 'created_at', 'updated_at')
        widgets = {
            'devlog': forms.HiddenInput(),
            'author': forms.HiddenInput(),
            'commentary': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'created_at': forms.HiddenInput,
            'updated_at': forms.HiddenInput()
        }

