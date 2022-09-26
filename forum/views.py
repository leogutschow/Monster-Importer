from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, CreateView
from authentications.models import Profile, Notification
from .models import Forum, Category, ForumComment
from .forms import FormForumComment, FormForum


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
        category = Category.objects.get(slug=self.kwargs['slug'])
        forum_comments = ForumComment.objects.filter(forum=self.get_object()).order_by('created_at')
        context['comments'] = forum_comments
        context['category'] = category
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        data = form.cleaned_data
        comments = ForumComment.objects.filter(forum=self.get_object()).values('author')
        profiles = Profile.objects.filter(user__in=comments)
        for profile in profiles:
            if profile.user == self.request.user:
                continue
            notification = Notification.objects.create(
                to_profile=profile,
                type='FC',
                message="Someone has commented in a post you follow! Go check it out!",
            )
            notification.save()
        new_comment = ForumComment.objects.create(
            author=Profile.objects.get(user=self.request.user),
            forum=self.get_object(),
            comment=data['comment'],
        )
        new_comment.save()
        messages.add_message(self.request, messages.SUCCESS, "Comment posted with Success!")
        return redirect('forum:forum', context['category'].slug, self.get_object().pk)


class ForumCreate(LoginRequiredMixin, CreateView):
    template_name = 'forum/forum_create.html'
    model = Forum
    form_class = FormForum

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.get(slug=self.kwargs['slug'])
        context['category'] = category
        context['comment'] = FormForumComment
        return context

    def form_valid(self, form):
        data = form.cleaned_data
        context = self.get_context_data()
        forum = Forum.objects.create(
            author=Profile.objects.get(user=self.request.user),
            title=data['title'],
            category=context['category'],
            created_at=timezone.now(),
            published=True,
        )
        forum.save()
        comment = ForumComment.objects.create(
            author=Profile.objects.get(user=self.request.user),
            forum=forum,
            comment=self.request.POST['comment'],
        )
        comment.save()
        messages.add_message(self.request, messages.SUCCESS, 'Your Forum has been posted!')
        return redirect('forum:forum', context['category'].slug, forum.pk)

