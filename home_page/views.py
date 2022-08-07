from django.db.models import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView
from monsters.models import Monster


# Create your views here.
class Index(TemplateView):
    model = Monster
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context: dict = super().get_context_data()
        monsters: Monster = Monster.objects.all()
        last_monster: Monster = Monster.objects.latest('id')
        context["monsters"]: QuerySet = monsters
        context['last_monster']: Monster = last_monster
        return context


class About(TemplateView):
    template_name = 'home_page/about.html'
