# Our Backend for the App!
# Built with Flask

# Import Flask
import flask
import requests
import os
from flask import send_file

# Create the application
app = flask.Flask(__name__)

# serving home.html
@app.route('/', methods=['GET'])
def serve_page():
    return flask.render_template('home.html')

# process query
@app.route('/process_query', methods=['POST'])
def process_query():
    data = flask.request.form  # is a dictionary
    location = data['user_input']
    return flask.render_template('home.html', same=location)


if __name__ == '__main__':
    app.run(debug=True)
