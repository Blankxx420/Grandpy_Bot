$('#ask-question').on('click', function(){
    console.log("Tu as cliqué sur le bouton !")
    const questionText = $('#question-value').val()
    console.log("La question posée est :", questionText)
    let questions = "<div class='chatbox col-12 asker text-right'>" + questionText + '<img src="../static/Images/user_avatar.png" class="float-right" alt="user_avatar" width="50">' + "</div>"
    $('#all-chatbox').append(questions)
    $.ajax({
    data: {'question': questionText},
    type: 'POST',
    url: '/question',
    dataType: 'text',
    success: function (response){
            console.log(response);
    },
    error:  function(error){
			console.log(error);
	},
    });
});

