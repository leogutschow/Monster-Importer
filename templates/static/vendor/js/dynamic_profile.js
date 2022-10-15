const notificationsBtn = document.getElementById('myNotificationsBtn');
notificationsBtn.addEventListener('click', change_page);
const monstersBtn = document.getElementById('myMonstersBtn');
monstersBtn.addEventListener('click', change_page);
const profileBtn = document.getElementById('myProfileBtn');
profileBtn.addEventListener('click', change_page);


function change_page(event){
    const allContent = document.getElementById('contentList').childNodes;
    console.log(allContent);
    allContent.forEach(content => {
        if (content.tagName =='DIV'){
            content.setAttribute('class', 'hidden');
        }
    });
    console.log(event.target.id);
    switch (event.target.id){
        case 'myNotificationsBtn':
            const notificationContent = document.getElementById('myNotifications');
            notificationContent.setAttribute('class', '');
            break;

        case 'myMonstersBtn':
            const monstersContent = document.getElementById('myMonsters');
            monstersContent.setAttribute('class', '');
            break
    }
}


$(document).ready(function(){

    var csrf = $('input[name=csrfmiddlewaretoken]').val()

    $(".notification-btn").click(function(){
        this_button = this
        $.ajax({
            url: '',
            type: 'post',
            data: {
                notification_id: $(this_button).val(),
                csrfmiddlewaretoken: csrf
            },
            success: function(response){
                $("#notificationText").text('');
                $("#notificationText").append(
                    `send at: <h6 class="fst-italic">${response.notification_sendat}</h6>
                     <h3>${response.notification_title}</h3>
                      <p>${response.notification_message}</p>`
                );
                $(this_button).removeClass("fw-bold");
                }
            }
        );
    });
});