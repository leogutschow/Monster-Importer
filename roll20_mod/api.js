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
    let str_mod = AddPCAttribute("strength_mod", value=get_modifier_value(monster.strength), characterid);
    
    let dex = AddPCAttribute("dexterity", value=monster.dexterity, characterid);
    let dex_mod = AddPCAttribute("dexterity_mod", value=get_modifier_value(monster.dexterity), characterid);
    let init_bonus = AddPCAttribute("initiative_bonus", value=get_modifier_value(monster.dexterity), characterid);
    
    let con = AddPCAttribute("constitution", value=monster.constitution, characterid);
    let con_mod = AddPCAttribute("constitution_mod", value=get_modifier_value(monster.constitution), characterid);
    
    let int = AddPCAttribute("intelligence", value=monster.intelligence, characterid);
    let int_mod = AddPCAttribute("intelligence_mod", value=get_modifier_value(monster.intelligence), characterid);
    
    let wis = AddPCAttribute("wisdom", value=monster.wisdom, characterid);
    let wis_mod = AddPCAttribute("wisdom_mod", value=get_modifier_value(monster.wisdom), characterid);
    
    let cha = AddPCAttribute("charisma", value=monster.charisma, characterid);
    let cha_mod = AddPCAttribute("charisma_mod", value=get_modifier_value(monster.charisma), characterid);
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
        
        
        if (monster_json.monster.game === 'DND5E'){
            let Character = createObj("character", {name: monster_json.monster.name});

            let npc = AddPCAttribute("npc", value=1, Character.id);
            let npc_flag = AddPCAttribute("npc_name", value=monster_json.monster.name, Character.id);
            let npc_ac = AddPCAttribute("npc_ac", value=monster_json.monster.ac, Character.id);
            let npc_hp = createObj("attribute", {name:"hp", current:`${monster_json.monster.hp}`, max: `${monster_json.monster.hp}`, characterid: Character.id});
            let npc_hp_formula = AddPCAttribute("npc_hpformula", value=monster_json.monster.hp_dices, Character.id);
            let npc_speed = AddPCAttribute("npc_speed", value=monster_json.monster.movement, Character.id);
            
            set_attributes(monster_json.monster, Character.id);
            
            let ac = AddPCAttribute("npc_ac", value=monster_json.monster.ac, Character.id);
            let ac_type = AddPCAttribute("npc_actype", value=monster_json.monster.ac_type, Character.id);
            let challenge = AddPCAttribute("npc_challenge", value=monster_json.monster.challenge, Character.id);
            let xp = AddPCAttribute("npc_xp", value=get_xp(monster_json.monster.challenge), Character.id);
            let npc_senses = AddPCAttribute("npc_senses", value=monster_json.monster.senses, Character.id);
            let npc_languages = AddPCAttribute("npc_languages", value=monster_json.monster.languages, Character.id);
            let npc_type = AddPCAttribute("npc_type", value=`${monster_json.monster.size} ${monster_json.monster.race}, ${monster_json.monster.alignment}`, Character.id)
            
            
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
            sendChat("Monster-Importer", `/w gm ${monster_json.monster.name} was successfully imported!`);
        
        }
    }
})

sendChat("Monster Importer", "/w gm Monster Importer ready to work! Use the webapp to import a monster or use '!mo -help' to see more options")