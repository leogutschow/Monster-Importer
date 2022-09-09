console.log("Aqui é o Script de JS");
console.log("Cristiano Ronaldo criado!");
const chat = document.getElementById("textchat-input");
const txt = chat.getElementsByTagName("textarea")[0];
const btn = chat.getElementsByTagName("button")[0];
const speakingas = document.getElementById("speakingas");

function postChatMessage(message, character = null) {
    let set_speakingas = true;
    const old_as = speakingas.value;
    if (character) {
        character = character.toLowerCase().trim();
        for (let i = 0; i < (speakingas.children.length); i++) {
            if (speakingas.children[i].text.toLowerCase().trim() === character) {
                speakingas.children[i].selected = true;
                set_speakingas = false;
                break;
            }
        }
    }
    if (set_speakingas)
        speakingas.children[0].selected = true;
    const old_text = txt.value;
    txt.value = message;
    btn.click();
    txt.value = old_text;
    speakingas.value = old_as;
}

postChatMessage("Teste Extensão")

console.log("Foi até o final")
//window.Campaign.characters.create({name: "Leonardo"});