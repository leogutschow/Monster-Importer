const importMonsterBtn = document.getElementById('importMonster');
importMonsterBtn.addEventListener('click', import_monster)
window.addEventListener('storage', storageListener);

async function import_monster(event){
    if (event){
        event.preventDefault();
        if (typeof(Storage) !== "undefined"){
            localStorage.setItem('message', 'Aqui e a mensagem');
            console.log(localStorage.getItem('message'));
        }
    }

}

function storageListener(event){
    alert('Mensagem recebida');
}