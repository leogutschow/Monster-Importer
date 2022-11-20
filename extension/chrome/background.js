function handleMessage(request, sender, sendResponse){
    chrome.tabs.query({"url": "https://app.roll20.net/editor/"}).then((tabs) => {
        for (const tab of tabs){
            chrome.tabs.sendMessage(tab.id, {message: '!mo ' + request.monster});
        }
    });
}



console.log(chrome.tabs);
chrome.runtime.onMessage.addListener(handleMessage);