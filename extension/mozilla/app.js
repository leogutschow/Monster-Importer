console.log("Aqui é o Script de JS");
console.log("Cristiano Ronaldo criado!");
var opened = false
window.open("https://app.roll20.net/editor/");
opened = true
setTimeout(40000)
window.frames.Campaign.characters.create({name: "Leo Teste JS"})

//window.Campaign.characters.create({name: "Leonardo"});