from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView
from .forms import FormRequest
from .models import Request
from django.core.mail import send_mail


# Create your views here.
class NewRequest(FormView):
    template_name = 'client_requests/new_request.html'
    form_class = FormRequest

    def form_valid(self, form):
        context = self.get_context_data()
        user = None
        request = context['form']
        if request and hasattr(request, 'client'):
            user = request.client
        cleaned_data = form.cleaned_data
        client_request = Request.objects.create(
            client=user,
            request_type=cleaned_data['request_type'],
            request_title=cleaned_data['request_title'],
            request_text=cleaned_data['request_text']
        )
        client_request.save()

        send_mail(subject=cleaned_data['request_type'],
                  from_email=user.email,
                  recipient_list=['leogusalles@gmail.com'],
                  message=cleaned_data['request_text'])

        print("request enviada")
        return redirect('home:home_page')
