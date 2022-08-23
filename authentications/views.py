from django.shortcuts import render, reverse, redirect, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import FormView, DetailView


# Create your views here.
class Login(LoginView):
    template_name = 'authentications/login.html'
    success_url = 'home:home_page'


class Logout(LogoutView):
    redirect_field_name = 'home:home_page'


class Register(FormView):
    template_name = 'authentications/register.html'
    form_class = RegisterForm

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            if User.objects.filter(username=cleaned_data['username']).exists():
                return render(request, self.template_name, {
                    'form': self.form_class,
                    'error_message': 'Username already exists'
                })

            elif User.objects.filter(email=cleaned_data['email']).exists():
                return render(request, self.template_name, {
                    'form': self.form_class,
                    'error_message': 'Email already in the database'
                })

            elif cleaned_data['password'] != cleaned_data['password_repeat']:
                return render(request, self.template_name, {
                    'form': self.form_class,
                    'error_message': "Passwords don't match"
                })

            new_user = User.objects.create_user(
                username=cleaned_data['username'],
                email=cleaned_data['email'],
                password=cleaned_data['password']
            )
            new_user.save()

            return HttpResponseRedirect(redirect_to=reverse('home:home_page'))


class Profile(DetailView):
    model = User
