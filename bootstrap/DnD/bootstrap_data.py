import json
import os
import requests
from django.utils.text import slugify
import re
import sys

PARENT_PATH = sys.path.append('../Monster-Importer')
from MonsterImporter.settings import MEDIA_ROOT


"""
A module that reads the JSON in the bootstrap folder and creates 
another JSON formatted to be loaded in the DB
"""


def load_dnd_monsters():
    with open(r'bootstrap/DnD/srd_5e_monsters.json', 'r') as dnd_json_file:
        json_monsters = json.load(dnd_json_file)
        monster_all = []
        basesheet_all = []
        all_actions = []
        all_legendary = []
        all_skills = []
        all_traits = []
        all_reactions = []
        all_trait_spells = []
        all_savings = []
        reaction_count: int = 1
        action_count: int = 1
        skill_count: int = 1
        traits_count: int = 1
        legendary_count: int = 1
        trait_spell_count: int = 1
        saving_count: int = 1
        for num, monster in enumerate(json_monsters):
            base_sheet = {}
            monster_dict = {}
            name = monster['name']
            size, race, alignment = parse_meta(monster['meta'])
            armor, armor_class = parse_armor(monster['Armor Class'])
            if not armor_class:
                armor_class = ' '
            hp, hp_dices = parse_hp(monster['Hit Points'])
            movement = monster['Speed']
            strength = int(monster['STR'])
            dexterity = int(monster['DEX'])
            constitution = int(monster['CON'])
            intelligence = int(monster['INT'])
            wisdom = int(monster['WIS'])
            charisma = int(monster['CHA'])
            senses = monster['Senses']
            languages = monster['Languages']
            challenge = monster['Challenge'].split(' ')[0]
            img_link = f'images/monsters/DnD5e/{name}.jpg'
            senses = monster['Senses']

            # Creating the dictionaries before some Attributes that
            # some Monsters may not have
            base_sheet = {
                'model': 'monsters.basesheet',
                'pk': num + 1,
                'fields': {
                    'name': name, 'size': size, 'race': race, 'challenge': challenge, 'ac': armor, 'ac_type': armor_class, 'hp': hp,
                    'hp_dices': hp_dices, 'movement': movement, 'strength': strength, 'dexterity': dexterity,
                    'constitution': constitution, 'intelligence': intelligence, 'wisdom': wisdom,
                    'charisma': charisma, 'game': 'DND5E', 'home_brew': False,
                    'slug': slugify(f'DND5E {name}'), 'image': img_link
                }
            }
            monster_dict = {
                'model': 'monsters.dndmonster',
                'pk': num + 1,
                'fields': {
                    'basesheet_ptr_id': num + 1, 'alignment': alignment,
                    'description': 'Placeholder', 'senses': senses, 'languages': languages,
                }
            }
            if 'Damage Resistances' in monster:
                monster_dict['fields']['damage_resistances'] = monster['Damage Resistances']
            if 'Damage Immunities' in monster:
                monster_dict['fields']['damage_immunities'] = monster['Damage Immunities']
            if 'Condition Immunities' in monster:
                monster_dict['fields']['condition_immunities'] = monster['Condition Immunities']

            # Getting Saving Throws:
            if 'Saving Throws' in monster:
                savings_list = monster['Saving Throws'].split(', ')
                for saving in savings_list:
                    attr, bonus = saving.split(' +')
                    saving_dict = {}
                    saving_dict = {
                        'model': 'monsters.dndsavingthrows',
                        'pk': saving_count,
                        'fields': {
                            'attr': attr, 'bonus': bonus, 'monster': num + 1
                        }
                    }
                    saving_count += 1
                    all_savings.append(saving_dict)

            # Getting the Skills
            if 'Skills' in monster:
                skills: list = monster['Skills'].split(', ')
                for skill_num, skill in enumerate(skills):
                    skill_monster = {}
                    skill = skill.split(' +')
                    skill_monster = {
                        'model': 'monsters.dndskill',
                        'pk': skill_count,
                        'fields': {
                            'modifier': skill[1], 'monster_id': num + 1, 'skill_name': skill[0]

                        }
                    }
                    all_skills.append(skill_monster)
                    skill_count += 1

            # Getting the Actions, traits, Reactions and Legendary Actions
            with open('bootstrap/DnD/easy_to_parse_monsters.json', 'r') as monster_abilities:
                abilities_from_json = json.load(monster_abilities)

                for abilities in abilities_from_json:
                    # Getting the Actions
                    if not 'actions' in abilities:
                        continue
                    if monster['name'] != abilities['name']:
                        continue
                    actions = abilities['actions']
                    for action in actions:
                        is_attack = False
                        # Getting the attack bonus
                        if action['attack_bonus'] != 0:
                            attack_bonus = action['attack_bonus']
                        else:
                            attack_bonus = None

                        # Getting the Damage Dices, if it has
                        if 'damage_dice' in action:
                            damage_dice = action['damage_dice']
                            is_attack = True
                        else:
                            damage_dice = None

                        # Getting the Damage Bonus, if it has
                        if 'damage_bonus' in action:
                            damage_dice = f"{damage_dice} + {action['damage_bonus']}"

                        single_action_dict = {}
                        single_action_dict = {
                            'model': 'monsters.dndaction',
                            'pk': action_count,
                            'fields': {
                                'monster_id': num + 1, 'action_name': action['name'], 'action_description': action['desc'],
                                'attack': attack_bonus, 'hit_dice': damage_dice, 'is_attack': is_attack
                            }
                        }
                        action_count += 1
                        all_actions.append(single_action_dict)

                    # Getting Legendary Actions
                    # Getting the Base Legendary Action, the description and uses of it
                    if 'Legendary Actions' in monster:
                        legendary_action = monster['Legendary Actions'].split('</p>')
                        legendary_base = legendary_action[0][3:-1]
                        legendary_dict = {}
                        legendary_dict = {
                            'model': 'monsters.dndlegendaryaction',
                            'pk': legendary_count,
                            'fields': {
                                'monster_id': num + 1,
                                'legendary_name': 'BASE',
                                'legendary_description': legendary_base
                            }
                        }
                        legendary_count += 1
                        all_legendary.append(legendary_dict)

                    # Getting the actual Legendary Actions
                    if 'legendary_actions' in abilities:
                        legendary_actions = abilities['legendary_actions']
                        for legendary_action in legendary_actions:
                            legendary_dict = {}
                            legendary_dict = {
                                'model': 'monsters.dndlegendaryaction',
                                'pk': legendary_count,
                                'fields': {
                                    'monster_id': num + 1,
                                    'legendary_name': legendary_action['name'], 'legendary_description': legendary_action['desc']
                                }
                            }
                            legendary_count += 1
                            all_legendary.append(legendary_dict)

                    # Getting the Ractions
                    if 'reactions' in abilities:
                        reaction_monster: list = abilities['reactions']
                        for reaction in reaction_monster:
                            reaction_dict: dict = {
                                'model': 'monsters.dndreaction',
                                'pk': reaction_count,
                                'fields': {
                                    'monster': num + 1, 'reaction_name': reaction['name'],
                                    'reaction_description': reaction['desc']
                                }
                            }
                            all_reactions.append(reaction_dict)
                            reaction_count += 1

                    # Getting Traits
                    if 'special_abilities' in abilities:
                        traits = abilities['special_abilities']
                        trait_dict = {}
                        for trait in traits:
                            trait_dict = {}
                            trait_dict = {
                                'model': 'monsters.dndspecialtraits',
                                'pk': traits_count,
                                'fields': {
                                    'monster': num + 1, 'specialtrait_name': trait['name'],
                                    'specialtrait_description': trait['desc']
                                }
                            }
                            if 'Spellcasting' in trait['name'] and not 'Innate' in trait['name']:
                                spell_per_trait, count = parse_spellcasting(description=trait['desc'],
                                                   trait_pk=traits_count,
                                                   count=trait_spell_count)
                                trait_spell_count = trait_spell_count + count
                                for spell_trait in spell_per_trait:
                                    all_trait_spells.append(spell_trait)
                                trait_dict['fields']['spellcasting'] = True
                            traits_count += 1

                            all_traits.append(trait_dict)

            basesheet_all.append(base_sheet)
            monster_all.append(monster_dict)
            print(f'{name} has been loaded')

    monster_json_file = open(r'bootstrap/DnD/all_monsters.json', 'w')
    json.dump(monster_all, monster_json_file)
    basesheet_json = open(r'bootstrap/DnD/all_basesheet.json', 'w')
    json.dump(basesheet_all, basesheet_json)
    skills_json_file = open(r'bootstrap/DnD/all_skills.json', 'w')
    json.dump(all_skills, skills_json_file)
    trait_json = open(r'bootstrap/DnD/all_traits.json', 'w')
    json.dump(all_traits, trait_json)
    actions_json = open(r'bootstrap/DnD/all_actions.json', 'w')
    json.dump(all_actions, actions_json)
    legendary_json = open(r'bootstrap/DnD/all_legendary.json', 'w')
    json.dump(all_legendary, legendary_json)
    reaction_file = open(r'bootstrap/DnD/all_reactions.json', 'w')
    json.dump(all_reactions, reaction_file)
    trait_spells_file = open(r'bootstrap/DnD/all_trait_spells.json', 'w')
    json.dump(all_trait_spells, trait_spells_file, indent=4)
    saving_file = open(r'bootstrap/DnD/all_savings.json', 'w')
    json.dump(all_savings, saving_file)


def load_traits():
    pass


def parse_spellcasting(description: str, trait_pk: int, count: int):
    only_spells = description.split('• ')[1:]
    internal_count = 0
    internal_list = []
    for spells in only_spells:
        spells = spells.split(': ')[1:][0]
        if re.search(r'\n', spells):
            spells = re.sub(r'\n', '', spells)
        for spell in spells.split(', '):
            with open('bootstrap/DnD/spells.json', 'r') as spells_json:
                spells_all = json.load(spells_json)
                for db_spell in spells_all:
                    if db_spell['name'].lower() != spell:
                        continue
                    index = spells_all.index(db_spell)
                    trait_spell = {}
                    trait_spell = {
                        'model': 'monsters.dndspecialtraits_dnd_spells',
                        'pk': count + internal_count,
                        'fields': {
                            'dndspecialtraits_id': trait_pk, 'dndspells_id': index + 1
                        }
                    }
                    internal_count += 1
                    internal_list.append(trait_spell)
    return internal_list, internal_count


def load_dndspells():
    with open(r'bootstrap/DnD/spells.json', 'r') as spells_json_raw:
        spells_json = json.load(spells_json_raw)
        spell_list: list = []
        for num, spell in enumerate(spells_json):
            spell_dict = {}
            school = ''
            match spell['school']:
                case 'evocation':
                    school = 'EVO'
                case 'conjuration':
                    school = 'CON'
                case 'necromancy':
                    school = 'NEC'
                case 'illusion':
                    school = 'ILL'
                case 'abjuration':
                    school = 'ABJ'
                case 'transmutation':
                    school = 'TRA'
                case 'divination':
                    school = 'DIV'
                case 'enchantment':
                    school = 'ENC'
            if spell['level'] == 'cantrip':
                level = 'C'
            else:
                level = spell['level']
            if 'materials_needed' in spell['components']:
                materials_needed = spell['components']['materials_needed'][0]
            else:
                materials_needed = None
            spell_dict = {
                'model': 'spells.dndspells',
                'pk': num + 1,
                'fields': {
                    'spell_name': spell['name'],
                    'range': spell['range'],
                    'ritual': spell['ritual'],
                    'school': school,
                    'duration': spell['duration'],
                    'spell_description': spell['description'],
                    'level': level,
                    'casting_time': spell['casting_time'],
                    'verbal': spell['components']['verbal'],
                    'somatic': spell['components']['somatic'],
                    'material': spell['components']['material'],
                    'materials_needed': materials_needed,

                }
            }
            spell_list.append(spell_dict)
            print(f"{spell['name']} loaded")
        spell_json_file = open(r'bootstrap/DnD/all_spells.json', 'w')
        json.dump(spell_list, spell_json_file)


def load_images():
    with open(r'bootstrap/DnD/srd_5e_monsters.json', 'r') as dnd_json_file:
        json_monsters = json.load(dnd_json_file)
        for num, monster in enumerate(json_monsters):
            if monster['name'] == 'Succubus/Incubus':
                monster['name'] = 'Succubus and Incubus'
            image = requests.get(monster['img_url'])
            with open(MEDIA_ROOT / rf"media/images/monsters/DnD5e/{monster['name']}.jpg", 'wb') as handler:
                handler.write(image.content)
                print(f"{monster['name']} image loaded")


def parse_actions():
    pass


def parse_meta(meta: str):
    splited_meta = meta.split(', ')
    size = splited_meta[0].split(' ')[0]
    race = splited_meta[0].split(' ')[1]
    alignment = splited_meta[1]
    return size, race, alignment


def parse_hp(hp: str):
    hp_all = hp.split(' ')
    hp_num = hp_all[0]
    hp_dices = join_list(hp_all)[1:-1]
    return int(hp_num), hp_dices


def parse_armor(armor: str):
    if len(armor) <= 3:
        armor_num = armor[:-1]
        return armor_num, None
    armor_all = armor.split(' ')
    armor_num = armor_all[0]
    armor_class = join_list(armor_all)
    if armor_class[0] == '(':
        armor_class = armor_class[1:-1]
    return int(armor_num), armor_class


def join_list(lista: list):
    return ''.join([x + ' ' for x in lista[1:]])[:-1]


if __name__ == '__main__':
    # parse_armor('19 (Natural Armor)')
    # parse_armor('19 ')
    # parse_hp('481 (26d20 + 208)')
    # print(parse_meta('Huge Dragon, chaotic evil'))
    load_dnd_monsters()
    load_dndspells()
    load_images()
