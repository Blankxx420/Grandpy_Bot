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
                const longitude = details.longitude;
                console.log(longitude)
                const latitude = details.latitude;
                console.log(latitude)
                const wiki_url = details.url;
                const sentence = details.sentence;
                let div_map = "<div id='map' style='width: 400px; height: 300px;'>"
                let bot_response = "<div class='chatbox col-12 answerer text-left'>" + "<img src='../static/Images/logo_robot.png' alt='avatar' width='50'>" + sentence + "<a href=" + wiki_url+"> Plus d'infos<a/>" + div_map + "</div"
                $('#all-chatbox').append(bot_response)
                mapboxgl.accessToken = 'pk.eyJ1IjoiYmxhbmt4eCIsImEiOiJja3A1bm40bjYwaWs5MnRxdHdua2JiazNyIn0.iFNN7eAz04uWKAazMhjHQQ';
                var map = new mapboxgl.Map({
                        container: "map",
                        style: 'mapbox://styles/mapbox/streets-v11',
                        center: [longitude, latitude],
                        zoom: 5,
                });
                var marker = new mapboxgl.Marker()
                .setLngLat([longitude, latitude])
                .addTo(map)
            }
    },
    error:  function(error){
			console.log(error);
	},
    });
});