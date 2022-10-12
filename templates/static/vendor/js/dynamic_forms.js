const gameSelect = document.getElementById('id_game');
gameSelect.addEventListener('change', change_game);

const totalActionNewForms = document.getElementById('id_dndaction_set-TOTAL_FORMS');
const addActionBtn = document.getElementById('addActionBtn');
addActionBtn.addEventListener('click', function(event){
    add_new_inlineform('action-form', 'actionList', 'emptyActionForm', totalActionNewForms);
});

const totalTraitNewForms = document.getElementById('id_dndspecialtraits_set-TOTAL_FORMS');
const addTraitBtn = document.getElementById('addTraitBtn');
addTraitBtn.addEventListener('click', function(event){
    add_new_inlineform('trait-form', 'traitList', 'emptyTraitForm', totalTraitNewForms);
});

const totalSkillNewForms = document.getElementById('id_dndskill_set-TOTAL_FORMS');
const addSkillBtn = document.getElementById('addSkillBtn');
addSkillBtn.addEventListener('click', function(event){
    add_new_inlineform('skill-form', 'skillList', 'emptySkillForm', totalSkillNewForms);
});

const totalLegendaryNewForms = document.getElementById('id_dndlegendaryaction_set-TOTAL_FORMS');
const addLegendaryBtn = document.getElementById('addLegendaryBtn');
addLegendaryBtn.addEventListener('click', function(event){
    add_new_inlineform('legendary-form', 'legendaryList', 'emptyLegendaryForm', totalLegendaryNewForms);
});

const totalSavingNewForms = document.getElementById('id_dndsavingthrows_set-TOTAL_FORMS');
const addSavingBtn = document.getElementById('addSavingBtn');
addSavingBtn.addEventListener('click', function(event){
    add_new_inlineform('saving-form', 'savingList', 'emptySavingForm', totalSavingNewForms);
});

const totalReactionNewForms = document.getElementById('id_dndreaction_set-TOTAL_FORMS');
const addReactionBtn = document.getElementById('addReactionBtn');
addReactionBtn.addEventListener('click', function(event){
    add_new_inlineform('reaction-form', 'reactionList', 'emptyReactionForm', totalReactionNewForms);
});

const totalTor20MeleeForms = document.getElementById('id_tor20meleeaction_set-TOTAL_FORMS');
const addTor20MeleeBtn = document.getElementById('addTor20MeleeBtn');
addTor20MeleeBtn.addEventListener('click', function(event){
    add_new_inlineform('melee-form', 'meleeList', 'emptyTor20Melee', totalTor20MeleeForms);
});

const totalTor20RangedForms = document.getElementById('id_tor20rangedaction_set-TOTAL_FORMS');
const addTor20RangedBtn = document.getElementById('addTor20RangedBtn');
addTor20RangedBtn.addEventListener('click', function(event){
    add_new_inlineform('ranged-form', 'rangedList', 'emptyTor20Ranged', totalTor20RangedForms);
})

function change_game(event){
    if (event){
        event.preventDefault();
    }
    const allGames = document.getElementById('specificGames').childNodes;
    allGames.forEach(game => {
        if (game.tagName == 'DIV'){
            game.setAttribute('class', 'hidden');
        }
    })

    switch (gameSelect.value){
        case 'DND5E':
            const dndForm = document.getElementById('dndMonsterForm');
            dndForm.setAttribute('class', 'container col');
            console.log('DND escolhido');
            break;

        case 'TOR20':
            const tor20Form = document.getElementById('tor20MonsterForm');
            tor20Form.setAttribute('class', 'container col');
            console.log('Tor20 escolhido');
            break;

        case 'PAF1e':
            const pf_form = document.getElementById('pfMonsterForm');
            pf_form.setAttribute('class', 'container col');
            console.log('PathFinder escolhido');
            break;
    }
}

function add_new_inlineform(form_class, form_list, emptyFormId, totalForms){
    console.log('Nova Funcao Funcionou!');
    const currentForms = document.getElementsByClassName(form_class);
    const formCopyTarget = document.getElementById(form_list);
    const emptyForm = document.getElementById(emptyFormId).cloneNode(true);
    if (form_class == 'skill-form'){
        emptyForm.setAttribute('class', `${form_class} col`);
    }
    else{
        emptyForm.setAttribute('class', form_class);
    }
    emptyForm.setAttribute('id', `form-${currentForms.length +1}`);
    const regex = new RegExp('__prefix__', 'g');
    emptyForm.innerHTML = emptyForm.innerHTML.replace(regex, currentForms.length);
    totalForms.setAttribute('value', currentForms.length + 1);
    formCopyTarget.append(emptyForm);
}


