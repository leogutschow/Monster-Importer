from django.shortcuts import render, reverse, redirect, HttpResponseRedirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, DetailView
from monsters.models import BaseSheet


# Create your views here.
class Login(LoginView):
    template_name = 'authentications/login.html'
    success_url = 'home:home_page'


class Logout(LogoutView):
    redirect_field_name = 'home:home_page'


class Register(FormView):
    template_name = 'authentications/register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        if form.is_valid():
            if User.objects.filter(username=cleaned_data['username']).exists():
                return render(self.request, self.template_name, {
                    'form': self.form_class,
                    'error_message': 'Username already exists'
                })
            print(cleaned_data)
            if cleaned_data['password1'] != cleaned_data['password2']:
                return render(self.request, self.template_name, {
                    'form': self.form_class,
                    'error_message': "Passwords don't match"
                })
            new_user = User.objects.create_user(
                username=cleaned_data['username'],
                email=cleaned_data['email'],
                password=cleaned_data['password1']
            )
            new_user.save()

            new_profile = Profile.objects.create(
                user=new_user
            )
            new_profile.save()

            messages.add_message(self.request, messages.SUCCESS, "Your profile has been created!")
            return HttpResponseRedirect(redirect_to=reverse('home:home_page'))


class ProfileView(DetailView, LoginRequiredMixin):
    model = Profile
    template_name = 'accounts/profile_detail.html'
    login_url = 'auth:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        profile = Profile.objects.get(user=self.get_object().user)
        monsters = BaseSheet.objects.filter(created_by=profile)
        context['profile'] = profile
        context['monsters'] = monsters
        return context
