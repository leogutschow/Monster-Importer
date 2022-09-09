const gameSelect = document.getElementById('id_game')
gameSelect.addEventListener('change', change_game)

const totalActionNewForms = document.getElementById('id_dndaction_set-TOTAL_FORMS')
const addActionBtn = document.getElementById('addActionBtn')
addActionBtn.addEventListener('click', add_new_action)

const totalTraitNewForms = document.getElementById('id_dndspecialtraits_set-TOTAL_FORMS')
const addTraitBtn = document.getElementById('addTraitBtn')
addTraitBtn.addEventListener('click', add_new_trait)

const totalSkillNewForms = document.getElementById('id_dndskill_set-TOTAL_FORMS')
const addSkillBtn = document.getElementById('addSkillBtn')
addSkillBtn.addEventListener('click', add_new_skill)

const totalLegendaryNewForms = document.getElementById('id_dndlegendaryaction_set-TOTAL_FORMS')
const addLegendaryBtn = document.getElementById('addLegendaryBtn')
addLegendaryBtn.addEventListener('click', add_legendary_action)

const totalSavingNewForms = document.getElementById('id_dndsavingthrows_set-TOTAL_FORMS')
const addSavingBtn = document.getElementById('addSavingBtn')
addSavingBtn.addEventListener('click', add_saving)

const totalReactionNewForms = document.getElementById('id_dndreaction_set-TOTAL_FORMS')
const addReactionBtn = document.getElementById('addReactionBtn')
addReactionBtn.addEventListener('click', add_reaction)

const totalTor20MeleeForms = document.getElementById('id_tor20meleeaction_set-TOTAL_FORMS')
const addReactionBtn = document.getElementById('addTor20MeleeBtn')
addReactionBtn.addEventListener('click', add_new_tor20_action)

function change_game(event){
    if (event){
        event.preventDefault()
    }
    const allGames = document.getElementById('specificGames').childNodes
     allGames.forEach(game => {
        if (game.tagName == 'DIV'){
            console.log(game)
            game.setAttribute('class', 'hidden')
            console.log(game)
        }
    })
    switch (gameSelect.value){
        case 'DND5E':
            const dndForm = document.getElementById('dndMonsterForm')
            dndForm.setAttribute('class', 'container col')

        case 'TOR20':
            const tor20Form = document.getElementById('tor20MonsterForm')
            tor20Form.setAttribute('class', 'container col')
    }
}

function add_new_action(event) {
    if (event){
        event.preventDefault()
    }
    const currentActionsForms = document.getElementsByClassName('action-form')
    const formCopyTarget = document.getElementById('actionList')
    const emptyForm = document.getElementById('emptyActionForm').cloneNode(true)
    emptyForm.setAttribute('class', 'action-form')
    emptyForm.setAttribute('id', `form-${currentActionsForms.length +1}`)
    const regex = new RegExp('__prefix__', 'g')
    emptyForm.innerHTML = emptyForm.innerHTML.replace(regex, currentActionsForms.length)
    totalActionNewForms.setAttribute('value', currentActionsForms.length + 1)
    formCopyTarget.append(emptyForm)
}

function add_new_trait(event){
    if (event){
        event.preventDefault()
    }
    const currentTraitForms = document.getElementsByClassName('trait-form')
    const formCopyTarget = document.getElementById('traitList')
    const emptyForm = document.getElementById('emptyTraitForm').cloneNode(true)
    emptyForm.setAttribute('class', 'trait-form')
    emptyForm.setAttribute('id', `form-${currentTraitForms.length +1}`)
    const regex = new RegExp('__prefix__', 'g')
    emptyForm.innerHTML = emptyForm.innerHTML.replace(regex, currentTraitForms.length)
    totalTraitNewForms.setAttribute('value', currentTraitForms.length + 1)
    formCopyTarget.append(emptyForm)
}

function add_new_skill(event){
     if (event){
        event.preventDefault()
    }
    const currentSkillForms = document.getElementsByClassName('skill-form')
    const formCopyTarget = document.getElementById('skillList')
    const emptyForm = document.getElementById('emptySkillForm').cloneNode(true)
    emptyForm.setAttribute('class', 'skill-form col')
    emptyForm.setAttribute('id', `form-${currentSkillForms.length +1}`)
    const regex = new RegExp('__prefix__', 'g')
    emptyForm.innerHTML = emptyForm.innerHTML.replace(regex, currentSkillForms.length)
    totalTraitNewForms.setAttribute('value', currentSkillForms.length + 1)
    formCopyTarget.append(emptyForm)
}

function add_legendary_action(event){
    if (event){
        event.preventDefault()
    }
    const currentLegendaryForms = document.getElementsByClassName('legendary-form')
    const formCopyTarget = document.getElementById('legendaryList')
    const emptyForm = document.getElementById('emptyLegendaryForm').cloneNode(true)
    emptyForm.setAttribute('class', 'legendary-form')
    emptyForm.setAttribute('id', `form-${currentLegendaryForms.length +1}`)
    const regex = new RegExp('__prefix__', 'g')
    emptyForm.innerHTML = emptyForm.innerHTML.replace(regex, currentLegendaryForms.length)
    totalLegendaryNewForms.setAttribute('value', currentLegendaryForms.length + 1)
    formCopyTarget.append(emptyForm)
}

function add_saving(event){
    if (event){
        event.preventDefault()
    }
    const currentSavingForms = document.getElementsByClassName('saving-form')
    const formCopyTarget = document.getElementById('savingList')
    const emptyForm = document.getElementById('emptySavingForm').cloneNode(true)
    emptyForm.setAttribute('class', 'saving-form col')
    emptyForm.setAttribute('id', `form-${currentSavingForms.length +1}`)
    const regex = new RegExp('__prefix__', 'g')
    emptyForm.innerHTML = emptyForm.innerHTML.replace(regex, currentSavingForms.length)
    totalSavingNewForms.setAttribute('value', currentSavingForms.length + 1)
    formCopyTarget.append(emptyForm)
}

function add_reaction(event){
    if (event){
        event.preventDefault()
    }
    const currentReactionForms = document.getElementsByClassName('reaction-form')
    const formCopyTarget = document.getElementById('reactionList')
    const emptyForm = document.getElementById('emptyReactionForm').cloneNode(true)
    emptyForm.setAttribute('class', 'reaction-form')
    emptyForm.setAttribute('id', `form-${currentReactionForms.length +1}`)
    const regex = new RegExp('__prefix__', 'g')
    emptyForm.innerHTML = emptyForm.innerHTML.replace(regex, currentReactionForms.length)
    totalReactionNewForms.setAttribute('value', currentReactionForms.length + 1)
    formCopyTarget.append(emptyForm)
}

function add_new_tor20_action(event) {
    if (event){
        event.preventDefault()
    }
    const currentTor20MeleeForms = document.getElementsByClassName('melee-form')
    const formCopyTarget = document.getElementById('meleeList')
    const emptyForm = document.getElementById('emptyTor20Melee').cloneNode(true)
    emptyForm.setAttribute('class', 'melee-form')
    emptyForm.setAttribute('id', `form-${currentTor20MeleeForms.length +1}`)
    const regex = new RegExp('__prefix__', 'g')
    emptyForm.innerHTML = emptyForm.innerHTML.replace(regex, currentTor20MeleeForms.length)
    totalTor20MeleeForms.setAttribute('value', currentTor20MeleeForms.length + 1)
    formCopyTarget.append(emptyForm)
}

