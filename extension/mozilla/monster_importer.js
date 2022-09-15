const importMonsterBtn = document.getElementById('importMonster');
importMonsterBtn.addEventListener('click', import_monster)
browser.runtime.onMessage.addListener(handleMessage);

function handleMessage(request, sender, sendResponse){
    console.log(sender);
    console.log(request.message)
}

function handleResponse(message){
    console.log(message.response);
}

function handleError(error){
    console.log('Error ${error}');
}

async function import_monster(event){
    if (event){
        event.preventDefault();
    }
    const sending = browser.runtime.sendMessage({
        greeting: "!testeAPI",
    });
    sending.then(handleResponse);
}

