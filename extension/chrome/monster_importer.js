const importMonsterBtn = document.getElementById('importMonster');
const monsterJsonElement = document.getElementById('monster');
let monsterJson = monsterJsonElement.innerHTML;
importMonsterBtn.addEventListener('click', import_monster)
chrome.runtime.onMessage.addListener(handleMessage);

function handleMessage(request, sender, sendResponse){
    console.log(request.message)
}

function handleError(error){
    console.log('Error ${error}');
}

async function import_monster(event){
    if (event){
        event.preventDefault();
    }
    const sending = chrome.runtime.sendMessage({
        monster: monsterJson,
    });
}

