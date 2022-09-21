from django.shortcuts import render
from django.views.generic import UpdateView
from .models import DevLog


# Create your views here.
class DevLog(UpdateView):
    model = DevLog

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        devlog = self.get_object()
        context['devlog'] = devlog
        return context

