from django.shortcuts import render
from django.views.generic import UpdateView
from .models import DevLog, DevLogCommentary
from .forms import DevLogCommentaryForm


# Create your views here.
class DevLog(UpdateView):
    template_name = 'devlogs/devlog_update.html'
    model = DevLog
    form_class = DevLogCommentaryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        devlog = self.get_object()
        commentaries = DevLogCommentary.objects.filter(devlog=devlog)
        context['devlog'] = devlog
        context['commentaries'] = commentaries
        return context

