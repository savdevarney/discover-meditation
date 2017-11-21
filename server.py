import os
from pprint import pformat
import requests
from flask import Flask, request, render_template, session, redirect, jsonify, flash
from werkzeug.serving import run_simple
from jinja2 import StrictUndefined
from eventbrite import Eventbrite

# EB_CLIENT_SECRET = os.environ["EB_CLIENT_SECRET"]
# EB_OAUTH_TOKEN = os.environ["EB_OAUTH_TOKEN"]
# EB_ANONYMOUS_OAUTH_TOKEN = os.environ["EB_ANONYMOUS_OAUTH_TOKEN"]
# EB_API_KEY = os.environ["EB_API_KEY"]

app = Flask(__name__)
app.secret_key = 'ABCSECRETDEF'

# EB_URL = "https://www.eventbriteapi.com/v3/"

# raise errors if there are undefined variables in Jinja2
# app.jinja_env.undefined = StrictUndefined

@app.route("/")
def home_page():
    """ identify user's location and display meditation events nearby """

    return render_template("home.html")

if __name__ == "__main__":

    context=('cert.pem', 'key.pem')
    app.debug=True
    app.jinja_env.auto_reload=app.debug
    app.run(host="0.0.0.0", port=5000) #ssl_context='adhoc')

