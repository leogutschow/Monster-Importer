from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Manual


# Create your views here.
class ManualDownload(TemplateView):
    template_name = 'manuals/manuals.html'
    model = Manual

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        manuals = self.model.objects.all()
        context['manuals'] = manuals
        return context