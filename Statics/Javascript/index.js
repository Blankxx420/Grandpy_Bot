$('ask-question').on('click', function(){
    console.log("Tu as cliqué sur le bouton !")
    let questionText = $('#question-value').val()
    console.log("La question posée est :", questionText)
    let question = "<div class='chatbox col-12 asker text-rigth'>" + questionText + "</div>"
    $('#all-chatbox').append(question)
}

