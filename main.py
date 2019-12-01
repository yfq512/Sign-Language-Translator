
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
    return flask.render_template('home.html', same=processInput(input_in_list), og=input)

def processInput(input_in_list):
    for s,i in enumerate(input_in_list):
        if "bye" in i.lower():
            input_in_list[s] = "static/bye.jpg"
        if "hello" in i.lower():
            input_in_list[s] = "static/hello.png"
        if "yes" in i.lower():
            input_in_list[s] = "static/yes.png"
        if "no" in i.lower():
            input_in_list[s] = "static/no.png"
        if "please" in i.lower():
            input_in_list[s] = "static/please.png"
        if "thanks" in i.lower():
            input_in_list[s] = "static/thanks.png"
    return input_in_list


if __name__ == '__main__':
    app.run(debug=True)
