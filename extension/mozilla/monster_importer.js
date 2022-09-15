const importMonsterBtn = document.getElementById('importMonster');
const monsterJson = document.getElementById('monster').innerHTML;
importMonsterBtn.addEventListener('click', import_monster)
browser.runtime.onMessage.addListener(handleMessage);

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
    const sending = browser.runtime.sendMessage({
        greeting: monsterJson,
    });
}

