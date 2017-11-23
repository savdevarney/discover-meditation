// currently using JS directly in home.html.  Can't yet get this module to load

const ebUrl = "https://www.eventbriteapi.com/v3";
const ebSearch = "/events/search";
const ebToken = "/?token=QH7DGFM5HFFYPBGZOCZO";
const q = "&q=meditation";
const sort_by = "&sort_by=best";
let pageNumber = 1;
let page = `&page=${pageNumber}`;
let str;

function showClasses(results) {
    let events = results['events']; // an array of event objects
    let meditations = events.map(function(event) {
        let title = event['name']['text'];
        let url = event['url'];
        let dateTime = event['start']['local'];
        return `
        <div class='class-tile'>
            <a href='${url}' target="_blank"> ${title}</a>
        </div>
        `; 
    });
    for (i = 0; i < meditations.length; i++) {
        $('#classes').append(meditations[i]);
    }
};

function getClasses() {
    page = `&page=${pageNumber}`;
    let query = ebUrl + ebSearch + ebToken + q + page + sort_by;
    if (str) {
        query += "&" + str;
        };
    console.log(`query is: ${query}`); 
    $.get(query, showClasses);
};

function getLocation(event) {
    event.preventDefault();
    str = $('form').serialize();
    $('#classes').empty();
    pageNumber = 1;
    getClasses();
};

$('#location').on('click', getLocation);

getClasses();

// infinite scrolling and paginating

console.log(`window.scrollTop is: ${($(window).scrollTop())}
    window.height is: ${($(window).height())}
    document.height is: ${($(document).height())}`);

$(window).scroll(()=> {
    if(($(window).scrollTop() + $(window).height()) === ($(document).height())){
        pageNumber++;
        console.log(`pageNumber is now: ${pageNumber}`);
        getClasses();
        console.log(`page has scrolled. 
            Window.scrollTop is: ${($(window).scrollTop())} 
            window.height is: ${($(window).height())}
            document.height is: ${($(document).height())}`);
        }
});


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