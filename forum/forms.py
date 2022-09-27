from django import forms
from .models import ForumComment, Forum
from django_summernote.widgets import SummernoteWidget


class FormForumComment(forms.ModelForm):
    class Meta:
        model = ForumComment
        fields = ('comment', )
        widgets = {
            'comment': SummernoteWidget(),
        }


class FormForum(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ('title', )
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }
