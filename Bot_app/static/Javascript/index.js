import { Map } from "./map";
$('#ask-question').on('click', function(){
    const questionText = $('#question-value').val()
    let questions = "<div class='chatbox col-12 asker text-right'>" + questionText + '<img src="../static/Images/user_avatar.png" class="float-right" alt="user_avatar" width="50">' + "</div>"
    $('#all-chatbox').append(questions)
    $.ajax({
    data: {'question': questionText},
    type: 'POST',
    url: '/question',
    dataType: 'text',
    success: function (response){
            let details = JSON.parse(response);
            console.log(details)
            if("sentence" in details){
                const longitude = details.longitude;
                const latitude = details.latitude;
                const wiki_url = details.url;
                const sentence = details.sentence;
                new Map(longitude, latitude)
                Map.add_map()
            }
    },
    error:  function(error){
			console.log(error);
	},
    });
});