from django.shortcuts import render
from django.views.generic import FormView, RedirectView
from django.contrib.auth.views import LoginView, LogoutView


# Create your views here.
class Login(LoginView):
    pass


class Logout(LogoutView):
    pass


class Register(FormView):
    pass
