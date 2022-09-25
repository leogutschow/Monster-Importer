from django import forms
from .models import ForumComment, Forum


class FormForumComment(forms.ModelForm):
    class Meta:
        model = ForumComment
        fields = ('comment', )
        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'form-control'
            }),
        }


class FormForum(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ('title', 'text',)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control'
            }),
        }
