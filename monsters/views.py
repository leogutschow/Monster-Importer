from django.shortcuts import render
from django.forms.models import model_to_dict
from django.views.generic import DetailView, ListView
from .models import Monster, Action, SpecialTraits
from django.core.paginator import Paginator


# Create your views here.
class MonsterDetail(DetailView):
    template_name: str = 'monsters/monster.html'
    model: Monster = Monster

    def get_context_data(self, **kwargs):
        context: dict = super().get_context_data()
        monster: Monster = self.get_object()
        context['monster'] = monster
        # Transforming the monster in a Dict so it can be passed as a JSON object in the Template and adding the Actions
        # and Special Traits to the Dict
        monster_dict: dict = model_to_dict(monster)
        monster_dict.pop('image')
        monster_actions: dict = {}
        monster_special_traits: dict = {}
        for num, action in enumerate(Action.objects.filter(monster=monster.pk).values()):
            monster_actions['action' + str(num)] = action
        # Some Monster doesn't have Special Traits
        if len(SpecialTraits.objects.filter(monster=monster.pk).values()) > 0:
            for num, special_trait in enumerate(SpecialTraits.objects.filter(monster=monster.pk).values()):
                monster_special_traits['special_trait' + str(num)] = special_trait
            monster_dict['special_traits'] = monster_special_traits
        monster_dict['actions'] = monster_actions
        context['monster_dict'] = monster_dict

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
        monster_name_query = request.GET.get('monster_name')
        monster_ac_query = request.GET.get('monster_ac')
        monster_challenge_query = request.GET.get('monster_challenge')
        qs = self.model.objects.all()
        context = self.get_context_data()
        # Adding some Logic to Query in the List
        if monster_name_query != '' and monster_name_query is not None:
            qs = qs.filter(name__icontains=monster_name_query)
        if monster_ac_query != '' and monster_ac_query is not None:
            qs = qs.filter(ac__icontains=monster_ac_query)
        if monster_challenge_query != '' and monster_challenge_query is not None:
            qs = qs.filter(challenge__icontains=monster_challenge_query)
        context['monsters'] = qs
        return render(request, template_name=self.template_name, context=context)
