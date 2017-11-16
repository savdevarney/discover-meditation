import os
from flask import Flask, request, render_template, session, redirect, jsonify, flash
from eventbrite import eventbrite

CLIENT_SECRET = os.environ["CLIENT_SECRET"]
OAUTH_TOKEN = os.environ["OAUTH_TOKEN"]
ANONYMOUS_OAUTH_TOKEN = os.environ["ANONYMOUS_OAUTH_TOKEN"]

app = Flask(__name__)
app.secret_key = 'ABCSECRETDEF'

# raise errors if there are undefined variables in Jinja2
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def show_events():
    """ identify user's location and display meditation events nearby """

if __name__ == "__main__":

    app.debug=True
    app.jinja_env.auto_reload=app.debug
    app.run(host="0.0.0.0", port=5000)
    
    # Use the DebugToolbar
    DebugToolbarExtension(app)
