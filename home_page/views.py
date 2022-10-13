from django.db.models import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView
from monsters.models import DnDMonster, BaseSheet
import random


# Create your views here.
class Index(TemplateView):
    model = BaseSheet
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context: dict = super().get_context_data()
        monsters: list = BaseSheet.objects.all()
        random_monster = random.randint(1, len(monsters))
        last_monster = BaseSheet.objects.get(id=random_monster)
        if last_monster.image:
            print(last_monster.image.url)
        context["monsters"] = monsters
        context['last_monster'] = last_monster
        return context


class About(TemplateView):
    template_name = 'home_page/about.html'
