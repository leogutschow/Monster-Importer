function handleMessage(request, sender, sendResponse){
    browser.tabs.query({"url": "https://app.roll20.net/editor/"}).then((tabs) => {
        for (const tab of tabs){
            browser.tabs.sendMessage(tab.id, {message: '!mo ' + request.monster});
        }
    });
}



console.log(browser.tabs);
browser.runtime.onMessage.addListener(handleMessage);