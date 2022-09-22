from django.shortcuts import render, redirect
from django.views.generic import UpdateView, ListView
from django.utils import timezone
from django.contrib import messages
from .models import DevLog, DevLogComment
from .forms import DevLogCommentForm
from authentications.models import Profile


# Create your views here.
class DevLogDetail(UpdateView):
    template_name = 'devlogs/devlog_update.html'
    model = DevLog
    form_class = DevLogCommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        devlog = self.get_object()
        commentaries = DevLogComment.objects.filter(devlog=devlog)
        context['devlog'] = devlog
        context['commentaries'] = commentaries
        return context

    def form_valid(self, form):
        data = form.cleaned_data
        author = Profile.objects.get(user=self.request.user)
        comment = DevLogComment.objects.create(
            devlog=self.object,
            author=author,
            commentary=data['commentary'],
            created_at=timezone.now()
        )
        comment.save()
        return redirect('devlogs:update_devlog', self.object.slug)


class DevLogList(ListView):
    template_name = 'devlogs/devlogs_list.html'
    model = DevLog

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        devlogs = DevLog.objects.all()
        context['devlogs'] = devlogs
        return context