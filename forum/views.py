from django.shortcuts import render
from django.views.generic import ListView
from .models import Forum, Category


# Create your views here.
class ForumIndex(ListView):
    template_name = 'forum/index.html'
    model = Category

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        categories = Category.objects.all()
        forums = Forum.objects.none()
        for category in categories:
            all_forums = Forum.objects.all()
            all_forums.filter(category=category)
            forums = forums.union(all_forums)
        context['categories'] = categories
        context['forums'] = forums
        print(forums)
        return context


class ForumCategory(ListView):
    template_name = 'forum/forum_category.html'
