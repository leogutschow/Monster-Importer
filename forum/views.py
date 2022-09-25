from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, UpdateView
from .models import Forum, Category, ForumComment
from .forms import FormForumComment


# Create your views here.
class ForumIndex(ListView):
    template_name = 'forum/index.html'
    model = Category

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        categories = Category.objects.all()
        context['categories'] = categories
        return context


class ForumCategory(ListView):
    template_name = 'forum/forum_category.html'
    model = Forum

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        category = Category.objects.get(slug=self.kwargs['slug'])
        forums = Forum.objects.filter(category=category)
        context['category'] = category
        context['forums'] = forums
        return context


class ForumInside(UpdateView):
    template_name = 'forum/forum_detail.html'
    model = Forum
    form_class = FormForumComment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        forum_comments = ForumComment.objects.filter(forum=self.get_object()).order_by('created_at')
        context['comments'] = forum_comments
        return context
