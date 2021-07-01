import {Map} from "./map.js";

$('#ask-question').on('click', function(){  // get event from user

    const questionText = $('#question-value').val() //get the value of the user input

    let questions = "<div class='chatbox col-12 asker text-right'>" //creating div for chatbox
        + questionText + '<img src="../static/Images/user_avatar.png"' +
        ' class="float-right" alt="user_avatar" width="50">'
        + "</div>"

    $('#all-chatbox').append(questions) //adding the div in index.html

    // Creating ajax call for backend and send question of user
    $.ajax({
    data: {'question': questionText},
    type: 'POST',
    url: '/question',
    dataType: 'text',
    success: function (response){
            let details = JSON.parse(response);

            console.log(details)

            if("sentence" in details){
                //get the data from response
                const longitude = details.longitude;
                const latitude = details.latitude;
                const wiki_url = details.url;
                const sentence = details.sentence;

                let bot_r_url = "<a href=" + wiki_url + ">" + "plus d'infos"  + "</a>" //creating link div

                let bot_response = "<div class='chatbox col-12 answerer text-left'>"+
                    '<img src="../static/Images/logo_robot.png" alt="avatar" width="50">' // create bot response
                    + sentence+ "\n" + bot_r_url + "</div>"

                new Map(longitude, latitude) //create the map

                $("#all-chatbox").append(bot_response) // adding the Bot response in chat

            }
    },
    error:  function(error){
			console.log(error);
	},
    });
});