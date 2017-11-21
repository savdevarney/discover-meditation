
let ebUrl = "https://www.eventbriteapi.com/v3"
let ebSearch = "/events/search"
let ebToken = "/?token=QH7DGFM5HFFYPBGZOCZO"
let q = "&q=meditation"
let sort_by = "&sort_by=best"


function showClasses(results) {
    console.log(results);
    let events = results['events']; // an array of event objects
    let meditations = events.map(function(event) {
        let title = event['name']['text'];
        let url = event['url'];
        let dateTime = event['start']['local'];
        return `
        <div class='class-tile'>
            <a href='${url}'> ${title}</a>
        </div>
        `; 
    });
    console.log(meditations)
    $('#classes').empty();
    for (i = 0; i < meditations.length; i++) {
        $('#classes').append(meditations[i]);
    }
};

function getClasses(event) {
    event.preventDefault();
    let str = $('form').serialize();
    let query = ebUrl + ebSearch + ebToken + q + sort_by + "&" + str;
    $.get(query, showClasses);
};

$('#location').on('click', getClasses);

function getAllClasses() {
    let query = ebUrl + ebSearch + ebToken + q + sort_by;
    $.get(query, showClasses);
}

getAllClasses();

/* 
window.onload = function() {
    let startPos;
    let geoSuccess = function(position) {
        startPos = position;
        document.getElementById('startLat').innerHTML = startPos.coords.lattitude;
        document.getElementById('startLon').innerHTML = startPos.coords.longitude;
        console.log(startPos);
    };
    navigator.geolocation.getCurrentPosition(geoSuccess);
};
*/