from django.shortcuts import render
from django.views.generic import CreateView
from .forms import FormRequest


# Create your views here.
class NewRequest(CreateView):
    template_name = 'client_requests/new_request.html'
    form_class = FormRequest
