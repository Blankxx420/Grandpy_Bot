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
            console.log(response)
            let details = JSON.parse(response);
            console.log(details)
            if("sentence" in details){
                const longitude = response.longitude;
                const latitude = response.latitude;
                const wiki_url = response.url;
                const sentence = response.sentence;
                let bot_response = "<div class='chatbox col-12 a text-left'>" + sentence + wiki_url + "</div"
                $('#all-chatbox').append(bot_response)
            }

            // récupéré les variables
            // créer la div bot reponse
            //initialiser la map
            // mettre en form la reponse
            //ajouter la reponse dans la divs avec un retardateur de 500ms


    },
    error:  function(error){
			console.log(error);
	},
    });
});