from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from itertools import chain
from django.forms import inlineformset_factory
from django.views.generic import DetailView, ListView, CreateView
from .models import DnDMonster, DnDAction, DnDSpecialTraits, BaseSheet, DnDSkill, \
    DnDLegendaryAction, DnDSavingThrows, DndReaction, Tor20Monster, Tor20MeleeAction, \
    Tor20RangedAction
from .forms import FormDndMonster, FormDnDAction, FormMonster, FormDndTrait, FormDnDSkill, \
    FormDnDLegendaryAction, FormDnDSavingThrow, FormDnDReaction, FormTor20Monster, FormTor20BaseAttack
from authentications.models import Profile


# Create your views here.
class MonsterDetail(DetailView):
    template_name: str = 'monsters/monster.html'
    model = DnDMonster

    def get_object(self, queryset=None):
        base_sheet = BaseSheet.objects.get(slug=self.kwargs['slug'])
        match base_sheet.game:
            case 'DND5E':
                monster = DnDMonster.objects.get(pk=base_sheet.pk)
                return monster
            case 'TOR20':
                monster = Tor20Monster.objects.get(pk=base_sheet.pk)
                return monster

    def get_context_data(self, **kwargs):
        context: dict = super().get_context_data()
        monster = self.get_object()
        context['monster'] = monster
        # Transforming the monster in a Dict so it can be passed as a JSON object in the Template and adding the Actions
        # and Special Traits to the Dict
        return context


class MonsterList(ListView):
    paginate_by = 20
    template_name: str = 'monsters/monster_list.html'
    model = BaseSheet


    def get_context_data(self, *, object_list=None, **kwargs):
        self.object_list = super().get_queryset()
        context = super().get_context_data()
        dndmonsters = list(DnDMonster.objects.all())
        tor20monsters = list(Tor20Monster.objects.all())
        context['monsters'] = list(chain(dndmonsters, tor20monsters))
        return context

    def get_queryset(self):
        dndmonsters = list(DnDMonster.objects.all())
        tor20monsters = list(Tor20Monster.objects.all())
        return list(chain(dndmonsters, tor20monsters))

    def get(self, request, *args, **kwargs):
        monster_name_query = request.GET.get('monster_name')
        monster_ac_query = request.GET.get('monster_ac')
        monster_challenge_query = request.GET.get('monster_challenge')
        monster_game_query = request.GET.get('monster_game')
        qs = self.model.objects.all()
        context = self.get_context_data()
        # Adding some Logic to Query in the List
        if monster_name_query != '' and monster_name_query is not None:
            qs = qs.filter(name__icontains=monster_name_query)
        if monster_ac_query != '' and monster_ac_query is not None:
            qs = qs.filter(ac__iexact=monster_ac_query)
        if monster_challenge_query != '' and monster_challenge_query is not None:
            qs = qs.filter(challenge__iexact=monster_challenge_query)
        if monster_game_query != '' and monster_challenge_query is not None:
            if monster_game_query != 'ALL':
                qs = qs.filter(game__iexact=monster_game_query)
        context['monsters'] = qs
        return render(request, template_name=self.template_name, context=context)


class MonsterCreate(CreateView):
    DnDAction_Formset = inlineformset_factory(form=FormDnDAction, model=DnDAction, parent_model=DnDMonster,
                                              min_num=0, extra=0)
    DndTrait_Formset = inlineformset_factory(form=FormDndTrait, model=DnDSpecialTraits, parent_model=DnDMonster,
                                             min_num=0, extra=0)
    DnDSkill_Formset = inlineformset_factory(form=FormDnDSkill, model=DnDSkill, parent_model=DnDMonster,
                                             min_num=0, extra=0)
    DnDLegendary_Formset = inlineformset_factory(form=FormDnDLegendaryAction, model=DnDLegendaryAction,
                                                 parent_model=DnDMonster, min_num=0, extra=0)
    DnDSavingThrow_Formset = inlineformset_factory(form=FormDnDSavingThrow, model=DnDSavingThrows, parent_model=DnDMonster,
                                                   min_num=0, extra=0)
    DnDReaction_Formset = inlineformset_factory(form=FormDnDReaction, model=DndReaction, parent_model=DnDMonster,
                                                min_num=0, extra=0)
    Tor20MeleeAction_Formset = inlineformset_factory(form=FormTor20BaseAttack, model=Tor20MeleeAction,
                                                     parent_model=Tor20Monster, min_num=0, extra=0)
    Tor20RangedAction_Formset = inlineformset_factory(form=FormTor20BaseAttack, model=Tor20RangedAction,
                                                      parent_model=Tor20Monster, min_num=0, extra=0)

    template_name = 'monsters/monster_create.html'
    form_class = FormMonster
    model = BaseSheet
    extra_context = {
        'dndmonster': FormDndMonster,
        'dndaction': DnDAction_Formset(),
        'dndtrait': DndTrait_Formset(),
        'dndskill': DnDSkill_Formset(),
        'dndlegendary': DnDLegendary_Formset(),
        'dndsaving': DnDSavingThrow_Formset(),
        'dndreaction': DnDReaction_Formset(),
        'tor20monster': FormTor20Monster,
        'tor20melee': Tor20MeleeAction_Formset(),
        'tor20ranged': Tor20RangedAction_Formset(),
    }

    def form_valid(self, form):
        data = form.cleaned_data
        monster_data = self.request.POST
        if data['game'] == 'DND5E':
            monster = DnDMonster.objects.create(
                created_by=Profile.objects.get(user=self.request.user),
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
                languages=monster_data.get('languages'),
                game=data['game'],
                home_brew=True,
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
            actions_formset = self.DnDAction_Formset(self.request.POST)
            traits_formset = self.DndTrait_Formset(self.request.POST)
            skills_formset = self.DnDSkill_Formset(self.request.POST)
            legendary_formset = self.DnDLegendary_Formset(self.request.POST)
            saving_formset = self.DnDSavingThrow_Formset(self.request.POST)

            if len(actions_formset) > 0:
                for action_form in actions_formset:
                    if action_form.is_valid():
                        cleaned_data = action_form.cleaned_data
                        action = DnDAction.objects.create(
                            monster=monster,
                            action_name=cleaned_data['action_name'],
                            action_description=cleaned_data['action_description'],
                            is_attack=cleaned_data['is_attack'],
                            attack=cleaned_data['attack'],
                            weapon_type=cleaned_data['weapon_type'],
                            reach=cleaned_data['reach'],
                            hit=cleaned_data['hit'],
                            hit_dice=cleaned_data['hit_dice'],
                            damage_type=cleaned_data['damage_type']
                        )
                        action.save()

            if len(traits_formset) > 0:
                for trait_form in traits_formset:
                    if trait_form.is_valid():
                        cleaned_data = trait_form.cleaned_data
                        trait = DnDSpecialTraits.objects.create(
                            monster=monster,
                            specialtrait_name=cleaned_data['specialtrait_name'],
                            specialtrait_description=cleaned_data['specialtrait_description'],
                            spellcasting=cleaned_data['spellcasting'],
                        )
                        trait.save()
                        if cleaned_data['spellcasting']:
                            for spell in cleaned_data['dnd_spells']:
                                trait.dnd_spells.add(spell)

            if len(skills_formset) > 0:
                for skill_form in skills_formset:
                    if skill_form.is_valid():
                        cleaned_data = skill_form.cleaned_data
                        skill = DnDSkill.objects.create(
                            monster=monster,
                            skill_name=cleaned_data['skill_name'],
                            modifier=cleaned_data['modifier']
                        )
                        skill.save()

            if len(legendary_formset) > 0:
                for legendary in legendary_formset:
                    if legendary.is_valid():
                        cleaned_data = legendary.cleaned_data
                        new_legendary = DnDLegendaryAction.objects.create(
                            monster=monster,
                            legendary_name=cleaned_data['legendary_name'],
                            legendary_description=cleaned_data['legendary_description']
                        )
                        new_legendary.save()

            if len(saving_formset) > 0:
                for saving in saving_formset:
                    if saving.is_valid():
                        cleaned_data = saving.cleaned_data
                        new_saving = DnDSavingThrows.objects.create(
                            monster=monster,
                            attr=cleaned_data['attr'],
                            bonus=cleaned_data['bonus']
                        )
                        new_saving.save()

            return redirect('monster:monster_list')

        if data['game'] == 'TOR20':
            Tor20Monster.objects.create(
                created_by=Profile.objects.get(user=self.request.user),
                name=monster_data.get('name'),
                race=data['race'],
                size=data['size'],
                ac=data['ac'],
                ac_type='None',
                hp=data['hp'],
                hp_dices='None',
                movement=data['movement'],
                strength=data['strength'],
                dexterity=data['dexterity'],
                constitution=data['constitution'],
                intelligence=data['intelligence'],
                wisdom=data['wisdom'],
                charisma=data['charisma'],
                game=data['game'],
                home_brew=True,
                description=monster_data.get('description'),
                image=self.request.FILES.get('image'),
                fortitude=monster_data.get('fortitude'),
                reflex=monster_data.get('reflex'),
                will=monster_data.get('will'),
                level=monster_data.get('level'),
                mana=monster_data.get('mana'),
                equipment=monster_data.get('equipment'),
                treasure=monster_data.get('treasure')
            )

            return redirect('monster:monster_list')

