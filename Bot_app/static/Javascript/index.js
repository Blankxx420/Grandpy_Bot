$('#ask-question').on('click', function(){
    console.log("Tu as cliqué sur le bouton !")
    const questionText = {question: $('#question-value').val()}
    console.log("La question posée est :", questionText)
    let question = "<div class='chatbox col-12 asker text-right'>" + questionText + '<img src="../static/Images/user_avatar.png" class="float-right" alt="user_avatar" width="50">' + "</div>"
    $('#all-chatbox').append(question)
    $.ajax({
    data: {questionText},
    type: 'POST',
    url: '/question',
    dataType: 'text',
    success: function (response)
            console.log('response');
    },
    error:  function(error){
			console.log('error');
	},
    });
});

