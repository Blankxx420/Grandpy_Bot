$('#ask-question').on('keypress click', function(){
    console.log("Tu as cliqué sur le bouton !")
    let questionText = $('#question-value').val()
    console.log("La question posée est :", questionText)
    let question = "<div class='chatbox col-12 asker text-right'>" + questionText + '<img src="../static/Images/user_avatar.png" class="float-right" alt="user_avatar" width="50">' + "</div>"
    $('#all-chatbox').append(question)
})

