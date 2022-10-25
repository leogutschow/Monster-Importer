from django.shortcuts import render, reverse, redirect, HttpResponseRedirect
from .forms import RegisterForm, ProfileEditForm, ChangeUserForm, ChangePassword
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile, Notification
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, DetailView
from monsters.models import BaseSheet


# Create your views here.
class Login(LoginView):
    template_name = 'authentications/login.html'
    next_page = 'home:home_page'


class Logout(LogoutView):
    next_page = 'home:home_page'
    success_url_allowed_hosts = 'home:home_page'


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

    def post(self, request, slug):
        user = User.objects.get(username=Profile.objects.get(slug=slug).user)
        change_user = ChangeUserForm(request.POST, instance=user)

        if change_user.is_valid():
            cleaned_data = change_user.cleaned_data
            user.username = cleaned_data.get('username')
            user.email = cleaned_data.get('email')
            user.first_name = cleaned_data.get('first_name')
            user.last_name = cleaned_data.get('last_name')
            user.save(update_fields=['username', 'email', 'first_name', 'last_name'])
            return redirect('auth:profile', slug)

        print(request.POST)
        change_password = ChangePassword(data=request.POST, user=user)
        print(change_password)
        print(change_password.is_valid())

        if request.POST.get('notification_id'):
            notification = Notification.objects.get(id=request.POST.get('notification_id'))
            notification.seen = True
            notification.save()
            text = notification.message
            return JsonResponse({'notification': text}, status=200)

        if change_password.is_valid():
            user.password = change_password.cleaned_data.get('new_password1')
            user.save(update_fields=['password'])
            return redirect('auth:profile', slug)
        else:
            messages.add_message(self.request, messages.ERROR, f'{change_password.errors}')
            return redirect('auth:profile', slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        profile = Profile.objects.get(user=self.get_object().user)
        monsters = BaseSheet.objects.filter(created_by=profile)
        user_form = ChangeUserForm(instance=self.request.user)
        password_form = ChangePassword(self.request.user)
        profile_form = ProfileEditForm(self.request.GET)
        context['password_form'] = password_form
        context['user_form'] = user_form
        context['profile_form'] = profile_form
        context['profile'] = profile
        context['monsters'] = monsters
        if profile.user == self.request.user:
            notifications = Notification.objects.filter(to_profile=profile)
            context['notifications'] = notifications
        return context
