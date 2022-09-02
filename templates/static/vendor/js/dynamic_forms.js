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