from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView
from django.contrib import messages
from MonsterImporter import settings
from authentications.models import Profile
from .forms import FormRequest
from .models import Request
from django.core.mail import send_mail


# Create your views here.
class NewRequest(FormView):
    template_name = 'client_requests/new_request.html'
    form_class = FormRequest

    def form_valid(self, form):
        context = self.get_context_data()
        user = self.request.user
        request = context['form']
        if request and hasattr(request, 'client'):
            user = request.client
        cleaned_data = form.cleaned_data
        client_request = Request.objects.create(
            client=Profile.objects.get(user=user),
            request_type=cleaned_data['request_type'],
            request_title=cleaned_data['request_title'],
            request_text=cleaned_data['request_text']
        )
        client_request.save()
        send_mail(subject=cleaned_data['request_title'],
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=['leogusalles@hotmail.com'],
                  message=cleaned_data['request_text'])
        messages.add_message(self.request, messages.SUCCESS,
                             "Your request has been sent to our admins. Wait for it to be reviewd")
        return redirect('home:home_page')
