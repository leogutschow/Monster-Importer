var AddPCAttribute = AddPCAttribute || {};
var AddPCPower = AddPCPower || {};

const generateUUID = (() => {
    let a = 0;
    let b = [];

    return () => {
        let c = (new Date()).getTime() + 0;
        let f = 7;
        let e = new Array(8);
        let d = c === a;
        a = c;
        for (; 0 <= f; f--) {
            e[f] = "-0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz".charAt(c % 64);
            c = Math.floor(c / 64);
        }
        c = e.join("");
        if (d) {
            for (f = 11; 0 <= f && 63 === b[f]; f--) {
                b[f] = 0;
            }
            b[f]++;
        } else {
            for (f = 0; 12 > f; f++) {
                b[f] = Math.floor(64 * Math.random());
            }
        }
        for (f = 0; 12 > f; f++){
            c += "-0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz".charAt(b[f]);
        }
        return c;
    };
})();

const generateRowID = () => generateUUID().replace(/_/g, "Z");

function AddPCAttribute (attr, value, charid) {
    let attrid = "";
    if (attr === "Hit Points") {
        attrid = createObj("attribute", {
            name: attr,
            current: value,
            max: value,
            characterid: charid
        });
    } else {
        attrid = createObj("attribute", {
            name: attr,
            current: value,
            characterid: charid
        });        
    }
    return attrid;
}

// Parser of the JSON sent in the Chat
function json_parse(json){
    let json_parsed = JSON.parse(json);
    return json_parsed;
}

// Returns the XP for the Monster
function get_xp(challenge){
    switch (challenge){
        case "0":
            return 10;
        case "1/8":
            return 25;
        case "1/4":
            return 50;
        case "1/2":
            return 100;
        case "1":
            return 200;
        case "2":
            return 450;
        case "3":
            return 700;
        case "4":
            return 1100;
        case "5":
            return 1800;
        case "6":
            return 2300;
        case "7":
            return 2900;
        case "8":
            return 3900;
        case "9":
            return 5000;
        case "10":
            return 5900;
        case "11":
            return 7200;
        case "12":
            return 8400;
        case "13":
            return 10000;
        case "14":
            return 11500;
        case "15":
            return 13000;
        case "16":
            return 15000;
        case "17":
            return 18000;
        case "18":
            return 20000;
        case "19":
            return 22000;
        case "20":
            return 25000;
        

    }
}

// Returns the modifier for the attibute value
function get_modifier_value(value){
    var mod = 0;
    switch (value) {
        case 1:
            mod = -5;
            return mod;
        case 2:
            mod = -4;
            return mod;
        case 3:
            mod = -4;
            return mod;
        case 4:
            mod = -3;
            return mod;
        case 5:
            mod = -3;
            return mod;
        case 6:
            mod = -2;
            return mod;
        case 7:
            mod = -2;
            return mod;
        case 8:
            mod = -1;
            return mod;
        case 9:
            mod = -1;
            return mod;
        case 10:
            mod = 0;
            return mod;
        case 11:
            mod = 0;
            return mod;
        case 12:
            mod = 1;
            return mod;
        case 13:
            mod = 1;
            return mod;
        case 14:
            mod = 2;
            return mod;
        case 15:
            mod = 2;
            return mod;
        case 16:
            mod = 3;
            return mod;
        case 17:
            mod = 3;
            return mod;
        case 18:
            mod = 4;
            return mod;
        case 19:
            mod = 4;
            return mod;
        case 20:
            mod = 5;
            return mod;
        case 21:
            mod = 5;
            return mod;
        case 22:
            mod = 6;
            return mod;
        case 23:
            mod = 6;
            return mod;
        case 24:
            mod = 7;
            return mod;
        case 25:
            mod = 7;
            return mod;
        case 26:
            mod = 8;
            return mod;
        case 27:
            mod = 8;
            return mod;
        case 28:
            mod = 9;
            return mod;
        case 29:
            mod = 9;
            return mod;
        case 30:
            mod = 10;
            return mod;
    }
}

//Adds the Attributes, just to be prettier in the event function
function set_attributes(monster, characterid){
    let str = AddPCAttribute("strength", value=monster.strength, characterid);


    let dex = AddPCAttribute("dexterity", value=monster.dexterity, characterid);
    let init_bonus = AddPCAttribute("initiative_bonus", value=get_modifier_value(monster.dexterity), characterid);
    let con = AddPCAttribute("constitution", value=monster.constitution, characterid);
    let int = AddPCAttribute("intelligence", value=monster.intelligence, characterid);
    let wis = AddPCAttribute("wisdom", value=monster.wisdom, characterid);
    let cha = AddPCAttribute("charisma", value=monster.charisma, characterid);

    if (monster.game == 'DND5E'){
        let str_mod = AddPCAttribute("strength_mod", value=get_modifier_value(monster.strength), characterid);
        let dex_mod = AddPCAttribute("dexterity_mod", value=get_modifier_value(monster.dexterity), characterid);
        let con_mod = AddPCAttribute("constitution_mod", value=get_modifier_value(monster.constitution), characterid);
        let int_mod = AddPCAttribute("intelligence_mod", value=get_modifier_value(monster.intelligence), characterid);
        let wis_mod = AddPCAttribute("wisdom_mod", value=get_modifier_value(monster.wisdom), characterid);
        let cha_mod = AddPCAttribute("charisma_mod", value=get_modifier_value(monster.charisma), characterid);
    }

}

// Adds the actions in the monster sheet
function add_action(action, character){
    const newID = generateRowID();
    let action_name = AddPCAttribute(`repeating_npcaction_${newID}_name`, `${action.action_name}`, character.id);
    let action_description =  AddPCAttribute(`repeating_npcaction_${newID}_description`, `${action.action_description}`, character.id);

    // Checking if the actions is an attack
    if(action.is_attack){
        let attack_flag = AddPCAttribute(`repeating_npcaction_${newID}_attack_flag`, "on", character.id);
        let attack_tohit = AddPCAttribute(`repeating_npcaction_${newID}_attack_tohit`,`${action.attack}`, character.id);
        let attack_damage = AddPCAttribute(`repeating_npcaction_${newID}_attack_damage`, `${action.hit_dice}`, character.id);
        let rollbase = AddPCAttribute(`repeating_npcaction_${newID}_rollbase`, "@{wtype}&{template:npcatk} {{attack=1}} @{damage_flag} @{npc_name_flag} {{rname=[@{name}](~repeating_npcaction_npc_dmg)}} {{rnamec=[@{name}](~repeating_npcaction_npc_crit)}} {{type=[^{attack-u}](~repeating_npcaction_npc_dmg)}} {{typec=[^{attack-u}](~repeating_npcaction_npc_crit)}} {{r1=[[@{d20}+(@{attack_tohit}+0)]]}} @{rtype}+(@{attack_tohit}+0)]]}} @{charname_output}", character.id);
        let damage_flag = AddPCAttribute(`repeating_npcaction_${newID}_damage_flag`, "{{damage=1}} {{dmg1flag=1}} ", character.id);
        let attack_onhit = AddPCAttribute(`repeating_npcaction_${newID}_attack_onhit`, `${action.hit_dice} damage`, character.id);
        let attack_tohitrange = AddPCAttribute(`repeating_npcaction_${newID}_attack_tohitrange`, `+${action.attack}`, character.id);

        return {name: action_name,
                description: action_description,
                attackflag: attack_flag,
                tohit: attack_tohit,
                attack_damage: attack_damage,
                rollbase: rollbase,
                damage_flag: damage_flag,
                onhit: attack_onhit,
                tohit_range: attack_tohitrange
        };
    }
    return {action_name: action_name, action_description: action_description};
}

// Get the spellcasting ability
function get_spellcasting_ability(spellcasting_mod){
    switch (spellcasting_mod){
        case 'STR':
            return 'strength_mod';
        case 'DEX':
            return 'dexterit_mody';
        case 'CON':
            return 'constitution_mod';
        case 'INT':
            return 'intelligence_mod';
        case 'WIS':
            return 'wisdom_mod';
        case 'CAR':
            return 'charisma_mod';
    }
}

// Adds the traits to the sheet
// There is a bug that just the first trait description don't upload
function add_trait(trait, character){
    const newID = generateRowID();
    let trait_name = AddPCAttribute(`repeating_npctrait_${newID}_name`,`${trait.specialtrait_name}`, character.id);
    let trait_description = AddPCAttribute(`repeating_npctrait_${newID}_description`, `${trait.specialtrait_description}`, character.id);
    if (trait.spellcasting){
        let spellcasting = AddPCAttribute('npcspellcastingflag', value='1', character.id);
        let caster_level = AddPCAttribute('caster_level', `${trait.caster_level}`, character.id);
        let level = AddPCAttribute('level', trait.caster_level, character.id);
        let ability = get_spellcasting_ability(trait.spellcasting_ability);
        let spellcasting_ability = AddPCAttribute('spellcasting_ability', `@{${ability}}+`, character.id);
        let spell_attack_mod = AddPCAttribute('spell_attack_mod', `${trait.spell_attack_mod}`, character.id);
        let globalmagicmod = AddPCAttribute('globalmagicmod', trait.spell_attack_mod, character.id);

        return {name: trait_name,
                description: trait_description,
                spellcasting: spellcasting,
                caster_level: caster_level,
                spellcasting_ability: spellcasting_ability,
                spell_attack_mod: spell_attack_mod,
                level: level,
                globalmagicmod: globalmagicmod,
        };
    }
    return {name: trait_name, description: trait_description};
}

// Adds the skills to the sheet
function add_skill(skill, characterid){
    let new_skill = AddPCAttribute(`npc_${skill.skill_name.toLowerCase()}`, skill.modifier, characterid);
    let skill_flag = AddPCAttribute(`npc_${skill.skill_name.toLowerCase()}_flag`, 2, characterid);
}

function add_legendary(legendary, character){
    const newID = generateRowID();
    let legendary_name = AddPCAttribute(`repeating_npcaction-m_${newID}_name`, `${legendary.legendary_name}`, character.id);
    let legendary_description =  AddPCAttribute(`repeating_npcaction-m_${newID}_description`, `${legendary.legendary_description}`, character.id);
    return {legendary_name: legendary_name, legendary_description: legendary_description};
}

// Adds the saving throws
function add_saving(saving, character){
    let attr_save = AddPCAttribute(`npc_${saving.attr.toLowerCase()}_save`, saving.bonus, character.id);
    let attr_flag = AddPCAttribute(`npc_${saving.attr.toLowerCase()}_save_flag`, 1, character.id);
    let attr_base = AddPCAttribute(`npc_${saving.attr.toLowerCase()}_save_base`, `${saving.bonus}`, character.id);
    return {attr_save: attr_save, attr_flag: attr_flag, attr_base: attr_base};
}

// Adds Reactions
function add_reaction(reaction, character){
    const newID = generateRowID();
    let npcreaction_name = AddPCAttribute(`repeating_npcreaction_${newID}_name`, `${reaction.reaction_name}`, character.id);
    let npcreaction_description = AddPCAttribute(`repeating_npcreaction_${newID}_description`, `${reaction.reaction_description}`, character.id);
    return {reaction_name: npcreaction_name, reaction_description: npcreaction_description};
}

// Parse multiple PF Attacks
function parse_multi_attack(attack_mods){
    return attack_mods.split('/');
}

//Parse PF Feats
function parse_feats(feats){
    return feats.split(', ');
}

//Add PathFinder attack
function add_pf_attack(atk, type, monster){
    const new_id = generateRowID();
    let attack_name = AddPCAttribute(`repeating_npcatk-${type}_${new_id}_atkname`, atk.name, monster.id);
    let attack_multiple = AddPCAttribute(`repeating_npcatk-${type}_${new_id}_multipleatk_flag`, atk.multiple, monster.id);
    let attack_mod;
    let attack_roll;
    let dmg_type = AddPCAttribute(`repeating_npcatk-${type}_${new_id}_dmgtype`, 'Placeholder', monster.id);
    let attack_roll_string = `{{roll=[[1d20cs>@{atkcritrange}+@{atkmod}[MOD]+@{rollmod_attack}[QUERY]]]}}{{critconfirm=[[1d20cs20+@{atkmod}[MOD]+@{rollmod_attack}[QUERY]]]}}{{rolldmg1=[[${atk.damage} + @{rollmod_damage}[QUERY]]]}}{{rolldmg1type=@{dmgtype}}}{{rolldmg1crit=[[(${atk.damage} + ${atk.damage}) + (@{rollmod_damage}[QUERY]*2)]]}}`
    if (atk.multiple){
        let counter = 0
        let attack_multiple = AddPCAttribute(`repeating_npcatk-${type}_${new_id}_multipleatk_flag`, atk.multiple, monster.id);
        const attack_mods = parse_multi_attack(atk.attack);
        for (const mod of attack_mods){
            if (counter == 0){
                attack_mod = AddPCAttribute(`repeating_npcatk-${type}_${new_id}_atkmod`, parseInt(attack_mods[counter]), monster.id);
            }
            else{
                attack_mod = AddPCAttribute(`repeating_npcatk-${type}_${new_id}_atkmod${counter + 1}`, parseInt(attack_mods[counter]), monster.id);
                attack_roll_string += `{{roll${counter}=[[1d20cs>@{atkcritrange}+@{atkmod${counter + 1}}[MOD]+@{rollmod_attack}[QUERY]]]}}{{critconfirm${counter}=[[1d20cs20+@{atkmod${counter + 1}}[MOD]+@{rollmod_attack}[QUERY]]]}}{{roll${counter}dmg1=[[${atk.damage} + @{rollmod_damage}[QUERY]]]}}{{roll${counter}dmg1type=@{dmgtype}}}{{roll${counter}dmg1crit=[[(${atk.damage} + ${atk.damage}) + (@{rollmod_damage}[QUERY]*2)]]}}`
            }
            counter += 1
        }
        attack_roll = AddPCAttribute(`repeating_npcatk-${type}_${new_id}_multipleatk`, attack_roll_string, monster.id);

    }
    else{
        attack_mod = AddPCAttribute(`repeating_npcatk-${type}_${new_id}_atkmod`, parseInt(atk.attack), monster.id);
        attack_roll = AddPCAttribute(`repeating_npcatk-${type}_${new_id}_multipleatk`, `{{roll=[[1d20cs>@{atkcritrange}+@{atkmod}[MOD]+@{rollmod_attack}[QUERY]]]}}{{critconfirm=[[1d20cs20+@{atkmod}[MOD]+@{rollmod_attack}[QUERY]]]}}{{rolldmg1=[[${atk.damage} + @{rollmod_damage}[QUERY]]]}}{{rolldmg1type=@{dmgtype}}}{{rolldmg1crit=[[(${atk.damage} + ${atk.damage}) + (@{rollmod_damage}[QUERY]*2)]]}}`, monster.id);
    }
    let attack_damage_base = AddPCAttribute(`repeating_npcatk-${type}_${new_id}_dmgbase`, atk.damage, monster.id);
    let options_flag = AddPCAttribute(`repeating_npcatk-${type}_${new_id}_options-flag`, '0', monster.id);
    let attack_display = AddPCAttribute(`repeating_npcatk-${type}_${new_id}_atkdisplay`, `${atk.name} +${atk.attack} (${atk.damage})`, monster.id);
    return {
        name: attack_name,
        damage_type: dmg_type,
        multiple: attack_multiple,
        mod: attack_mod,
        damage: attack_damage_base,
        attack_roll: attack_roll,
        options: options_flag
    };

}

//Add PathFinder Feat
function add_pf_feat(feat, monster){
    const new_id = generateRowID();
    let feat_name = AddPCAttribute(`repeating_feats_${new_id}_name`, feat, monster.id);
    let feat_flag = AddPCAttribute(`repeating_feats_${new_id}_options-flag`, 0, monster.id);
    return {
        feat: feat_name,
        options: feat_flag
    }
}

//Add Special Abilities
function add_special_ability(sa, monster){
    const new_id = generateRowID();
    let special_name = AddPCAttribute(`repeating_abilities_${new_id}_name`, sa.name, monster.id);
    let special_description = AddPCAttribute(`repeating_abilities_${new_id}_description`, sa.description, monster.id);
    let special_flag = AddPCAttribute(`repeating_abilities_${new_id}_options-flag`, 0, monster.id);
    return {
        name: special_name,
        description: special_description,
        options: special_flag
    }
}

//Adds Spells
// There is something I can't figure it out to add spells
function add_spell(spell, character){
    let newSpellID = generateRowID();
    let spell_id = AddPCAttribute(`repeating_attack_${newSpellID}_spellid`, generateRowID(), character.id);
    let spell_name = AddPCAttribute(`repeating_attack_${newSpellID}_atkname`, spell.spell_name, character.id);
    let spell_level = AddPCAttribute(`repeating_attack_${newSpellID}_spelllevel`, spell.level, character.id);
    return {
        id: spell_id,
        name: spell_name,
        level: spell_level,
    };
}

//Add Ac Mods
function add_pf_ac_mods(ac_mods, character){
    const ac_mods_parsed = ac_mods.split(',');
    let new_touch;
    let new_flat_footed;
    for (let i = 0; i < ac_mods_parsed.length; i++){
        if (i == 0){
            let touch = ac_mods_parsed[i].split(' ')
            new_touch = AddPCAttribute("ac_touch", touch[1], character.id);
        }
        if (i == 1) {
            let flat_footed = ac_mods_parsed[i].split(' ');
            new_flat_footed = AddPCAttribute("ac_flatfooted", flat_footed[1], character.id);
        }
    }
    return {
        touch: new_touch,
        flat_footed: new_flat_footed
    }
}

//Return PF XP from Monster CRE
function get_pf_xp(cr){
    switch (cr){
        case "1/8":
            return 50;
        case "1/6":
            return 65;
        case "1/4":
            return 100;
        case "1/3":
            return 135;
        case "1/2":
            return 200;
        case "1":
            return 400;
        case "2":
            return 600;
        case "3":
            return 800;
        case "4":
            return 1200;
        case "5":
            return 1600;
        case "6":
            return 2400;
        case "7":
            return 3200;
        case "8":
            return 4800;
        case "9":
            return 6400;
        case "10":
            return 9600;
        case "11":
            return 12800;
        case "12":
            return 19200;
        case "13":
            return 25600;
        case "14":
            return 38400;
        case "15":
            return 51200;
        case "16":
            return 76800;
        case "17":
            return 102400;
        case "18":
            return 153600;
        case "19":
            return 204800;
        case "20":
            return 307200;
        case "21":
            return 409600;
        case "22":
            return 614400;
        case "23":
            return 819200;
        case "24":
            return 1228800;
        case "25":
            return 1638400;
    }
}

on("chat:message", function(msg){
    if(msg.type!="api"){
        return;
    }
    if (msg.content.indexOf("!mo")==0){

        let argument = msg.content.substr(4);

        if (argument === "-help"){
            sendChat("Monster-Importer", "/w gm Aqui está um texto de ajuda");
            return;
        }

        let monster_json = json_parse(argument);

        let Character = createObj("character", {name: monster_json.monster.name});

        let npc = AddPCAttribute("npc", value=1, Character.id);
        let npc_flag = AddPCAttribute("npc_name", value=monster_json.monster.name, Character.id);
        let npc_ac = AddPCAttribute("npc_ac", value=monster_json.monster.ac, Character.id);
        let npc_hp = createObj("attribute", {name:"hp", current:`${monster_json.monster.hp}`, max: `${monster_json.monster.hp}`, characterid: Character.id});
        let npc_hp_formula = AddPCAttribute("npc_hpformula", value=monster_json.monster.hp_dices, Character.id);
        set_attributes(monster_json.monster, Character.id);

        if (monster_json.monster.game === 'DND5E'){


            let ac_type = AddPCAttribute("npc_actype", value=monster_json.monster.ac_type, Character.id);
            let challenge = AddPCAttribute("npc_challenge", value=monster_json.monster.challenge, Character.id);
            //let xp = AddPCAttribute("npc_xp", value=get_xp(monster_json.monster.challenge), Character.id);
            let npc_type = AddPCAttribute("npc_type", value=`${monster_json.monster.size} ${monster_json.monster.race}, ${monster_json.monster.alignment}`, Character.id)
            let npc_senses = AddPCAttribute("npc_senses", value=monster_json.monster.senses, Character.id);
            let npc_languages = AddPCAttribute("npc_languages", value=monster_json.monster.languages, Character.id);
            let npc_speed = AddPCAttribute("npc_speed", value=monster_json.monster.movement, Character.id);
            let ac = AddPCAttribute("npc_ac", value=monster_json.monster.ac, Character.id);

            if (monster_json.savings){
                var savings_flag = AddPCAttribute("npc_saving_flag", monster_json.savings.length, Character.id);
                for (const saving of monster_json.savings){
                    let new_saving = add_saving(saving, Character)
                }
            }

            if (monster_json.actions){
                for (const action of monster_json.actions){
                    let new_action = add_action(action, Character);
                }
            }

            if (monster_json.traits){
                for (const trait of monster_json.traits){
                    let new_trait = add_trait(trait, Character);
                    if (trait.spellcasting){
                        for (const spell of trait.dnd_spells){
                            let new_spell = add_spell(spell, Character);
                        }
                    }
                }
            }

            if (monster_json.skills){
                var skill_flag = AddPCAttribute("npc_skills_flag", monster_json.skills.length, Character.id);
                for (const skill of monster_json.skills){
                    let new_skill = add_skill(skill, Character.id);
                }
            }

            if (monster_json.legendary){
                let legendary_flag = AddPCAttribute("npc_mythic_actions", 1, Character.id);
                let legendary_description = AddPCAttribute("npc_mythic_actions_desc", monster_json.legendary[0].legendary_description, Character.id);
                for (const mythic of monster_json.legendary){
                    if (mythic.legendary_name != "BASE"){
                        let new_legendary = add_legendary(mythic, Character);
                    }
                }
            }

            if (monster_json.reactions){
                let reactions_flag = AddPCAttribute("npcreactionsflag", 1, Character.id);
                for (const reaction of monster_json.reactions){
                    let new_reactions = add_reaction(reaction, Character);
                }
            }


            let npc_options = AddPCAttribute("npc_options-flag", value=0, Character.id);
            let ui_flags = AddPCAttribute("ui_flags", value="", Character.id);
            let mancer_status = AddPCAttribute("l1mancer_status", value="completed", Character.id);

        }

        if (monster_json.monster.game === 'PAF1e'){
            let initialize_character = AddPCAttribute("initialize_character-flag", 0, Character.id)

            if (monster_json.special_abilities){
                let special_abilities_flag = AddPCAttribute("special_abilities_flag", 1, Character.id);
                for (const sa of monster_json.special_abilities){
                    let new_special = add_special_ability(sa, Character);
                }
            }

            if (monster_json.monster.race || monster_json.monster.class){
                let race_class;
                if (monster_json.monster.race){
                    race_class += monster_json.monster.race;
                }
                if (monster_json.monster.class){
                    race_class += monster_json.monster.class;
                }
                let race = AddPCAttribute("class", race_class, Character.id);
            }

            if (monster_json.monster.type){
                let type = AddPCAttribute("npc_type", monster_json.monster.type, Character.id);
            }

            let npc_options = AddPCAttribute("options-flag-npc", value="0", Character.id);

            let xp = AddPCAttribute("xp", get_pf_xp(monster_json.monster.challenge), Character.id);

            let hd_roll = AddPCAttribute("hd_roll", monster_json.monster.hp_dices, Character.id);
            let speed = AddPCAttribute("npc_speed", monster_json.monster.movement, Character.id);
            let sr = AddPCAttribute("sr", monster_json.monster.spell_resistence, Character.id);

            let cr = AddPCAttribute("npc_cr", monster_json.monster.challenge, Character.id);
            let initiative = AddPCAttribute("initiative", monster_json.monster.init, Character.id);
            let fortitude = AddPCAttribute("fortitude", monster_json.monster.fortitude, Character.id);
            let reflex = AddPCAttribute("reflex", monster_json.monster.reflex, Character.id);
            let will = AddPCAttribute("will", monster_json.monster.will, Character.id);
            let alignment = AddPCAttribute("npc_alignment", monster_json.monster.monster_alignment, Character.id);

            let space = AddPCAttribute("space", monster_json.monster.space, Character.id);
            let reach = AddPCAttribute("reach", monster_json.monster.reach, Character.id);

            let ac = AddPCAttribute('ac', value=monster_json.monster.ac, Character.id);
            let languages = AddPCAttribute('languages', value=monster_json.monster.languages, Character.id);
            let environment = AddPCAttribute('environment', monster_json.monster.environment, Character.id);
            let treasure = AddPCAttribute('treasure', monster_json.monster.treasure, Character.id);
            let organization = AddPCAttribute('organization', monster_json.monster.organization, Character.id);
            let background = AddPCAttribute('background', monster_json.monster.description, Character.id);

            if (monster_json.monster.ac_mod){
                let ac_mod = add_pf_ac_mods(monster_json.monster.ac_mod, Character);
            }

            if (monster_json.monster.weaknesses){
                let weaknesses = AddPCAttribute("weaknesses", monster_json.monster.weaknesses, Character.id);
            }

            if (monster_json.monster.resist){
                let resist = AddPCAttribute("resist", monster_json.monster.resist, Character.id);
            }

            if (monster_json.monster.senses){
                let senses = AddPCAttribute('senses', value=monster_json.monster.senses, Character.id);
            }

            if (monster_json.monster.immune){
                let senses = AddPCAttribute('immune', value=monster_json.monster.immune, Character.id);
            }

            if (monster_json.monster.base_attack){
                let bab = AddPCAttribute("bab", monster_json.monster.base_attack, Character.id);
            }

            if (monster_json.monster.combat_maneuver_defence){
                let cmd = AddPCAttribute("cmd_mod", monster_json.monster.combat_maneuver_defence, Character.id);
            }

            if (monster_json.monster.combat_maneuver_bonus){
                let cmb = AddPCAttribute("cmb_mod", monster_json.monster.combat_maneuver_bonus, Character.id);
            }

            if (monster_json.offense){
                for (const attack of monster_json.offense){
                    if (attack.type === 'M'){
                        let melee = add_pf_attack(attack, 'melee', Character);
                    }
                    if (attack.type === 'R'){
                        let melee = add_pf_attack(attack, 'ranged', Character);
                    }
                }
            }

            if (monster_json.skills){
                for (const monster_skill of monster_json.skills){
                    let new_skill = AddPCAttribute(`${monster_skill.skill.toLowerCase()}`, monster_skill.skill_bonus, Character.id);
                    let skill_display = AddPCAttribute(`${monster_skill.skill.toLowerCase()}_display`, `+${monster_skill.skill_bonus}`, Character.id);
                    let skill_notes = AddPCAttribute(`${monster_skill.skill.toLowerCase()}_notes`, "", Character.id);
                    let skill_flag = AddPCAttribute(`${monster_skill.skill.toLowerCase()}_flag`, 1, Character.id);
                }
            }

            if (monster_json.monster.feats){
                let feats = parse_feats(monster_json.monster.feats);
                for (const feat of feats){
                    let new_feet = add_pf_feat(feat, Character);
                }
            }


        }
        sendChat("Monster-Importer", `/w gm ${monster_json.monster.name} was successfully imported!`);
    }
})

sendChat("Monster Importer", "/w gm Monster Importer ready to work! Use the webapp to import a monster or use '!mo -help' to see more options")

