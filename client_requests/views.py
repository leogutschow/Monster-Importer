from django.views.generic import CreateView
from .models import Request
from .forms import FormRequest


# Create your views here.
class NewRequest(CreateView):
    template_name = 'client_requests/new_request.html'
    model = Request
    form_class = FormRequest