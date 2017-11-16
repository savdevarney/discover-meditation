import os
from pprint import pformat
import requests
from flask import Flask, request, render_template, session, redirect, jsonify, flash
from jinja2 import StrictUndefined
from eventbrite import Eventbrite

EB_CLIENT_SECRET = os.environ["EB_CLIENT_SECRET"]
EB_OAUTH_TOKEN = os.environ["EB_OAUTH_TOKEN"]
EB_ANONYMOUS_OAUTH_TOKEN = os.environ["EB_ANONYMOUS_OAUTH_TOKEN"]
EB_API_KEY = os.environ["EB_API_KEY"]

app = Flask(__name__)
app.secret_key = 'ABCSECRETDEF'

EVENTBRITE_URL = "https://www.eventbriteapi.com/v3/"

# raise errors if there are undefined variables in Jinja2
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def home_page():
    """ identify user's location and display meditation events nearby """

    # show

    return render_template("home.html")

@app.route('/meditations.json')
def get_meditations():
    """ route for an ajax request to show meditation classes from eventbrite
    API"""

    pass



if __name__ == "__main__":

    app.debug=True
    app.jinja_env.auto_reload=app.debug
    app.run(host="0.0.0.0", port=5000, ssl_context=('cert.pem', 'key.pem'))

    #command line to generate self-signed certificate:
    # openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
    
    # Use the DebugToolbar
    DebugToolbarExtension(app)



    # code from Hackbright lab on searching for afterparties

    # query = request.args.get('query')
    # location = request.args.get('location')
    # distance = request.args.get('distance')
    # measurement = request.args.get('measurement')
    # sort = request.args.get('sort')

    # # If the required information is in the request, look for afterparties
    # if location and distance and measurement:

    #     # The Eventbrite API requires the location.within value to have the
    #     # distance measurement as well
    #     distance = distance + measurement

    #     payload = {'q': query,
    #                'location.address': location,
    #                'location.within': distance,
    #                'sort_by': sort,
    #                }

    #     # For GET requests to Eventbrite's API, the token could also be sent as a
    #     # URL parameter with the key 'token'
    #     headers = {'Authorization': 'Bearer ' + EVENTBRITE_TOKEN}

    #     response = requests.get(EVENTBRITE_URL + "events/search/",
    #                             params=payload,
    #                             headers=headers)
    #     data = response.json()

    #     # If the response was successful (with a status code of less than 400),
    #     # use the list of events from the returned JSON
    #     if response.ok:
    #         events = data['events']

    #     # If there was an error (status code between 400 and 600), use an empty list
    #     else:
    #         flash(":( No parties: " + data['error_description'])
    #         events = []

    #     return render_template("afterparties.html",
    #                            data=pformat(data),
    #                            results=events)

    # # If the required info isn't in the request, redirect to the search form
    # else:
    #     flash("Please provide all the required information!")
    #     return redirect("/afterparty-search")
