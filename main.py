
# Our Backend for the App!
# Built with Flask

# Import Flask
import flask
import requests
import os
from flask import send_file

# Create the application
app = flask.Flask(__name__)

# serving find.html
@app.route('/', methods=['GET'])
def serve_page():
    return flask.render_template('home.html')

# process query
@app.route('/process_query', methods=['POST'])
def process_query():
    data = flask.request.form  # is a dictionary
    input = data['user_input']
    input_in_list = input.split(' ')
    for s,i in enumerate(input_in_list):
        if i.lower() == "hello":
            input_in_list[s] = "static/hello.png"
        if i.lower() == "yes":
            input_in_list[s] = "static/yes.png"
        if i.lower() == "no":
            input_in_list[s] = "static/no.png"
    return flask.render_template('home.html', same=input_in_list, og=input)


if __name__ == '__main__':
    app.run(debug=True)
