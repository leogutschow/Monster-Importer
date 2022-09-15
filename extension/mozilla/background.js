const roll20Id = "";
const monsterImporterId = "";

function handleMessage(request, sender, sendResponse){
    browser.tabs.sendMessage(2, {message: request.greeting});
}

console.log(browser.tabs);
browser.runtime.onMessage.addListener(handleMessage);