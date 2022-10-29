import pandas as pd
import json
import os
from django.utils.text import slugify


def load_monsters():
    all_attacks = []
    all_monsters = []
    all_skills = []
    all_abilities = []
    feat_monsters = []
    data = open(r'bootstrap/data/data.json', 'r')
    monsters_json = json.load(data)
    monster = 1
    skill_count = 1
    attack_counter = 1
    special_ability_counter = 1

    for key, value in monsters_json.items():

        base_sheet = {
            'model': 'monsters.basesheet',
            'pk': 328 + monster,
            'fields': {
                'name': value['title1'],
                'size': value['size'],
                'race': parse_value(value.get('race')),
                'challenge': parse_attr(value['CR']),
                'ac': value['AC']['AC'],
                'ac_type': 'None',
                'hp': value['HP']['HP'],
                'hp_dices': value['HP']['long'],
                'movement': parse_value(value['speeds']),
                'strength': parse_attr(value['ability_scores']['STR']),
                'dexterity': parse_attr(value['ability_scores']['DEX']),
                'constitution': parse_attr(value['ability_scores']['CON']),
                'intelligence': parse_attr(value['ability_scores']['INT']),
                'wisdom': parse_attr(value['ability_scores']['WIS']),
                'charisma': parse_attr(value['ability_scores']['CHA']),
                'slug': slugify(f"PAF1e {value['title1']}"),
                'game': 'PAF1e',
                'home_brew': False,
                'description': value['desc_long'],
                'image': f"images/monsters/PathFinder1e/{value['title1']}.jpg"
            }
        }
        # Getting Relation Feats Monsters
        feats = None
        if value.get('feats') is not None:
            feats = parse_feats(value.get('feats'))

        pf_monster = {
            'model': 'monsters.pathfindermonster',
            'fields': {
                'basesheet_ptr_id': base_sheet['pk'],
                'monster_class': parse_value(value.get('classes')),
                'monster_alignment': value.get('alignment'),
                'aura': parse_auras(value.get('auras')),
                'ac_mod': parse_ac_mod(value.get('AC')),
                'type': value['type'],
                'subtype': parse_value(value.get('subtypes')),
                'init': value['initiative']['bonus'],
                'senses': parse_value(value.get('senses')),
                'damage_reduction': parse_dr(value.get('DR')),
                'weaknesses': parse_value(value.get('weakness')),
                'fortitude': value['saves']['fort'],
                'reflex': value['saves']['ref'],
                'will': value['saves']['will'],
                'save_mods': value['saves'].get('other'),
                'feats': feats,
                'spell_domain': parse_value(value.get('domain')),
                'immune': parse_value(value.get('immunities'))[:255],
                'resist': parse_value(value.get('resistances')),
                'spell_resistence': parse_sr(value.get('SR')),
                'space': parse_value(value.get('space')),
                'reach': parse_value(value.get('reach')),
                'base_attack': value['BAB'],
                'combat_maneuver_bonus': parse_value(value.get('CMB')),
                'combat_maneuver_defence': parse_value(value.get('CMD')),
                'languages': parse_value(value.get('languages')),
                'special_qualities': parse_value(value.get('special_qualities')),
                'environment': parse_ecology(value.get('ecology'), 'environment'),
                'organization': parse_ecology(value.get('ecology'), 'organization'),
                'treasure': parse_ecology(value.get('ecology'), 'treasure_type')
            }
        }

        # Getting the Attacks
        if value.get('attacks') is not None:
            for attack_key, attack_value in value.get('attacks').items():
                if attack_key == 'melee':
                    for attack in attack_value:
                        for attr in attack:
                            multiple = False
                            count = 0
                            if attr.get('bonus'):
                                count = len(attr.get('bonus'))
                                if count > 1:
                                    multiple = True
                            attack_melee = {
                                'model': 'monsters.pathfinderoffense',
                                'pk': attack_counter,
                                'fields': {
                                    'monster': base_sheet['pk'],
                                    'name': attr.get('attack'),
                                    'type': attack_key[0].capitalize(),
                                    'attack': parse_attack_bonus(attr.get('bonus')),
                                    'effect': parse_attack_effects(attr.get('entries'), 'effect'),
                                    'crit_range': parse_attack_effects(attr.get('entries'), 'crit_range'),
                                    'multiple': multiple,
                                    'damage': parse_attack_effects(attr.get('entries'), 'damage'),
                                    'count': count
                                }
                            }
                            all_attacks.append(attack_melee)
                            attack_counter += 1
                if attack_key == 'ranged':
                    for attack in attack_value:
                        for attr in attack:
                            multiple = False
                            count = 0
                            if attr.get('bonus'):
                                count = len(attr.get('bonus'))
                                if count > 1:
                                    multiple = True
                            attack_ranged = {
                                'model': 'monsters.pathfinderoffense',
                                'pk': attack_counter,
                                'fields': {
                                    'monster': base_sheet['pk'],
                                    'name': attr.get('attack'),
                                    'type': attack_key[0].capitalize(),
                                    'attack': parse_attack_bonus(attr.get('bonus')),
                                    'effect': parse_attack_effects(attr.get('entries'), 'effect'),
                                    'crit_range': parse_attack_effects(attr.get('entries'), 'crit_range'),
                                    'multiple': multiple,
                                    'damage': parse_attack_effects(attr.get('entries'), 'damage'),
                                    'count': count
                                }
                            }
                            all_attacks.append(attack_ranged)
                            attack_counter += 1

        # Getting the skills
        if value.get('skills') is not None:
            for skill_key, skill_value in value.get('skills').items():
                if skill_key == '_racial_mods':
                    for racial_key, racial_value in skill_value.items():
                        if type(racial_value) is not str:
                            for bonus, _ in racial_value.items():
                                new_skill = {
                                    'model': 'monsters.pathfinderskill',
                                    'pk': skill_count,
                                    'fields': {
                                        'monster': base_sheet['pk'],
                                        'skill': racial_key,
                                        'skill_bonus': racial_value.get(bonus),
                                        'racial_mod': True
                                    }
                                }
                                skill_count += 1
                                all_skills.append(new_skill)
                    continue
                new_skill = {
                    'model': 'monsters.pathfinderskill',
                    'pk': skill_count,
                    'fields': {
                        'monster': base_sheet['pk'],
                        'skill': skill_key,
                        'skill_bonus': skill_value.get('_'),
                        'racial_mod': False
                    }
                }
                skill_count += 1
                all_skills.append(new_skill)

        # Getting Special Abilites
        if value.get('special_abilities') is not None:
            for ability_name, ability_description in value.get('special_abilities').items():
                new_ability = {
                    'model': 'monsters.pathfinderspecialability',
                    'pk': special_ability_counter,
                    'fields': {
                        'monster': base_sheet['pk'],
                        'name': ability_name,
                        'description': ability_description
                    }
                }
                all_abilities.append(new_ability)
                special_ability_counter += 1
        monster += 1
        all_monsters.append(base_sheet)
        all_monsters.append(pf_monster)

    pf_monsters_file = open(r'bootstrap/PF/json/pf_monsters.json', 'w')
    json.dump(all_monsters, pf_monsters_file)
    # feat_monsters_file = open(r'bootstrap/PF/json/feat_monsters.json', 'w')
    # json.dump(all_feat_monsters, feat_monsters_file)
    # skill_json = open(r'bootstrap/PF/json/pf_skills.json', 'w')
    # json.dump(all_skills, skill_json)
    attack_json = open(r'bootstrap/PF/json/pf_attacks.json', 'w')
    json.dump(all_attacks, attack_json)
    # feat_json = open(r'bootstrap/PF/json/feat_monsters.json', 'w')
    # json.dump(feat_monsters, feat_json)
    abilities_json = open(r'bootstrap/PF/json/pf_abilities.json', 'w')
    json.dump(all_abilities, abilities_json)


def parse_dr(dr):
    dr_string = ''
    if dr is None:
        return None
    for dr_item in dr:
        for key, value in dr_item.items():
            if key == 'amount':
                dr_string += f'{value}/'
                continue
            dr_string += f'{value}, '
    return dr_string


def parse_ac_mod(ac_mod_dict):
    ac_mod = ''
    for key, value in ac_mod_dict.items():
        if key == "AC":
            continue
        if key != "components":
            ac_mod += f'{key} {value}, '
            continue
        for component_key, component_value in value.items():
            ac_mod += f'{component_value} {component_key}, '
    return ac_mod


def parse_feats(feats: dict):
    all_feats = ''
    for feat in feats:
        all_feats += f"{feat.get('name')}, "
        return all_feats


def parse_attack_effects(entries, target):
    effect = ''
    if len(entries) == 0:
        return None
    for entry in entries[0]:
        for entry_key, entry_value in entry.items():
            if entry_key == target:
                return entry_value
            if target == 'effect' and entry_key == target:
                effect += f'{entry_value},'
    return effect


def parse_attack_bonus(attack_bonus):
    if attack_bonus is None:
        return None
    if type(attack_bonus) is not list:
        return str(attack_bonus[0])
    if len(attack_bonus) == 1:
        return str(attack_bonus[0])
    return r'/'.join([str(i)for i in attack_bonus])


def parse_ecology(ecology, name):
    try:
        return ecology.get(name)
    except: return None


def parse_attr(attr):
    if attr is not None and type(attr) is not str:
        return attr
    return 0


def parse_sr(sr):
    if sr is None:
        return None
    if type(sr) != int:
        return int(sr[:3])
    return sr


def parse_auras(auras):
    if auras is None:
        return None
    auras_str = ''
    for aura in auras:
        for key, value in aura.items():
            auras_str += f'{value} '
        auras_str += ', '
    return auras_str


def parse_value(attr_value):
    if type(attr_value) != list and type(attr_value) != dict:
        try:
            return attr_value
        except:
            return None

    if type(attr_value) == dict:
        joint_value = ''
        for key, value in attr_value.items():
            if key != 'base':
                joint_value += f'{key} {value}, '
                continue
            joint_value += f'{value}, '
        return joint_value

    try:
        return ', '.join(attr_value)
    except:
        return None


# Load the feats from the CSV file and insert them into a JSON file
def load_feats():
    feats = pd.read_csv(r'bootstrap/PF/raw/Feats_OGL - Feats_OGL Updated 23-03-2014.csv')
    all_feats = []
    for index, row in feats.iterrows():
        feat = {
            'model': 'monsters.pathfinderfeat',
            'pk': index,
            'fields': {
                'name': row['name'],
                'type': row['type'],
                'description': row['description'],
                'prerequisites': row['prerequisites']
            }
        }
        all_feats.append(feat)
    feat_json = open(r'bootstrap/PF/json/feats.json', 'w')
    json.dump(all_feats, feat_json)
    return all_feats


if __name__ == '__main__':
    load_monsters()
    # load_feats()
