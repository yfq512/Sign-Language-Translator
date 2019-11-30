from __future__ import division

# Our Backend for the App!
# Built with Flask

# Import Flask
import flask
import requests
import os
from flask import send_file

import re
import sys

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import pyaudio
from six.moves import queue

# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms

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
    input = data['user_input']
    return flask.render_template('home.html', same=input)


if __name__ == '__main__':
    app.run(debug=True)
