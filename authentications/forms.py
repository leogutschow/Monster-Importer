from django.contrib.auth.models import User
from . models import Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm, UsernameField
from django import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        print(kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class ChangePassword(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))


class ChangeUserForm(UserChangeForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = None
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'image', 'motto'
        )
        widgets = {
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'motto': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }