from django.shortcuts import render, redirect, HttpResponse
from django.forms.models import model_to_dict
from django.views.generic import DetailView, ListView, CreateView, TemplateView
from .models import DnDMonster, DnDAction, DnDSpecialTraits, BaseSheet
from django.core.paginator import Paginator
from .forms import FormDndMonster, FormDnDAction, FormMonster


# Create your views here.
class MonsterDetail(DetailView):
    template_name: str = 'monsters/monster.html'
    model: DnDMonster = DnDMonster

    def get_context_data(self, **kwargs):
        context: dict = super().get_context_data()
        monster: DnDMonster = self.get_object()
        context['monster'] = monster
        # Transforming the monster in a Dict so it can be passed as a JSON object in the Template and adding the Actions
        # and Special Traits to the Dict
        monster_dict: dict = model_to_dict(monster)
        monster_dict.pop('image')
        monster_actions: dict = {}
        monster_special_traits: dict = {}
        for num, action in enumerate(DnDAction.objects.filter(monster=monster.pk).values()):
            monster_actions['action' + str(num)] = action
        # Some Monster doesn't have Special Traits
        if len(DnDSpecialTraits.objects.filter(monster=monster.pk).values()) > 0:
            for num, special_trait in enumerate(DnDSpecialTraits.objects.filter(monster=monster.pk).values()):
                monster_special_traits['special_trait' + str(num)] = special_trait
            monster_dict['special_traits'] = monster_special_traits
        monster_dict['actions'] = monster_actions
        context['monster_dict'] = monster_dict

        return context


class MonsterList(ListView):
    template_name: str = 'monsters/monster_list.html'
    model = DnDMonster
    paginas = Paginator(model, 20)

    def get_context_data(self, *, object_list=None, **kwargs):
        self.object_list = super().get_queryset()
        context = super().get_context_data()
        monsters: list = DnDMonster.objects.all()
        context['monsters'] = monsters
        return context

    def get_queryset(self):
        monsters = DnDMonster.objects.all()
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


class MonsterCreate(CreateView):
    template_name = 'monsters/monster_create.html'
    form_class = FormMonster
    model = BaseSheet
    extra_context = {
        'dndmonster': FormDndMonster,
        'dndaction': FormDnDAction
    }

    def form_valid(self, form):
        data = form.cleaned_data
        print(data)
        monster_data = self.request.POST
        print(monster_data)
        if data['game'] == 'DND5E':
            print("Foi do DnD!")
            monster = DnDMonster.objects.create(
                name=monster_data.get('name'),
                race=data['race'],
                size=data['size'],
                ac=data['ac'],
                ac_type=data['ac_type'],
                hp=data['hp'],
                hp_dices=data['hp_dices'],
                movement=data['movement'],
                strength=data['strength'],
                dexterity=data['dexterity'],
                constitution=data['constitution'],
                intelligence=data['intelligence'],
                wisdom=data['wisdom'],
                charisma=data['charisma'],
                languages=data['languages'],
                game=data['game'],
                home_brew='True',
                alignment=monster_data.get('alignment'),
                challenge=int(monster_data.get('challenge')),
                description=monster_data.get('description'),
                image=self.request.FILES.get('image'),
                senses=monster_data.get('senses'),
                damage_resistances=monster_data.get('damage_resistances'),
                damage_immunities=monster_data.get('damage_immunities'),
                condition_immunities=monster_data.get('condition_immunities'),
            )
            monster.save()
            action = DnDAction.objects.create(
                monster=monster,
                action_name=monster_data.get('action_name'),
                action_description=monster_data.get('action_name'),
                is_attack=bool(monster_data.get('is_attack')),
                attack=monster_data.get('attack'),
                weapon_type=monster_data.get('weapon_type'),
                reach=monster_data.get('reach'),
                hit=monster_data.get('hit'),
                hit_dice=monster_data.get('hit_dice'),
                damage_type=monster_data.get('damage_type')
            )
            action.save()

        return redirect('monster:monster_list')
