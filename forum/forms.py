from django import forms
from .models import ForumComment


class FormForumComment(forms.ModelForm):
    class Meta:
        model = ForumComment
        fields = ('comment', )
        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'form-control'
            }),
        }
