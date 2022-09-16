function handleMessage(request, sender, sendResponse){
    browser.tabs.query({"url": "https://app.roll20.net/editor/"}).then(getRoll20Tab);
}

function getRoll20Tab(tabs){
    for (const tab of tabs){
        browser.tabs.sendMessage(tab.id, {message: "!testeAPI --mi"});
    }
}


console.log(browser.tabs);
browser.runtime.onMessage.addListener(handleMessage);