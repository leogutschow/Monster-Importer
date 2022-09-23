from django.shortcuts import render
from django.views.generic import ListView
from .models import Forum


# Create your views here.
class ForumIndex(ListView):
    template_name = 'forum/index.html'
    model = Forum