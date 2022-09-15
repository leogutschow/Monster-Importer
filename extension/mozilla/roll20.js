const chat = document.getElementById("textchat-input");
const txt = chat.getElementsByTagName("textarea")[0];
const btn = chat.getElementsByTagName("button")[0];
const speakingas = document.getElementById("speakingas");
browser.runtime.onMessage.addListener(handleMessage);

function handleMessage(request, sender, sendResponse){
    console.log(request.message);
    const message = request.message;
    postChatMessage(message);
}

function handleResponse(message){
    console.log(message.response);
}

function handleError(error){
    console.log('Error ${error}');
}

function sendSelfID(){
    const sending = browser.runtime.sendMessage({
        greeting: "Greeting from the content script",
    });
    sending.then(handleResponse);
}

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

//window.Campaign.characters.create({name: "Leonardo"});