from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Monster
from django.core.paginator import Paginator


# Create your views here.
class MonsterDetail(DetailView):
    template_name: str = 'monsters/monster.html'
    model: Monster = Monster

    def get_context_data(self, **kwargs):
        context: dict = super().get_context_data()
        monster = self.get_object()
        context['monster'] = monster
        return context


class MonsterList(ListView):
    template_name: str = 'monsters/monster_list.html'
    model = Monster
    paginas = Paginator(model, 20)

    def get_context_data(self, *, object_list=None, **kwargs):
        self.object_list = super().get_queryset()
        context = super().get_context_data()
        monsters: list = Monster.objects.all()
        context['monsters'] = monsters
        return context

    def get_queryset(self):
        monsters = Monster.objects.all()
        return monsters

    def get(self, request, *args, **kwargs):

        qs = self.model.objects.all()
        monster_name_query = request.GET.get('monster_name')
        context = self.get_context_data()
        if monster_name_query != '' and monster_name_query is not None:
            qs = qs.filter(name__icontains=monster_name_query)
        context['monsters'] = qs
        print(monster_name_query)
        return render(request, template_name=self.template_name, context=context)

