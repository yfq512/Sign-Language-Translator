# Our Backend for the App!
# Built with Flask

# Import Flask
import flask
import requests
import os
from flask import send_file

PEOPLE_FOLDER = os.path.join('static')

# Create the application
app = flask.Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

API_URL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?inputtype=textquery&locationbias=ipbias&fields=formatted_address,name,rating&"

# serving find.html
@app.route('/', methods=['GET'])
def serve_page():
    return flask.render_template('find.html')

# process query
@app.route('/process_query', methods=['POST'])
def process_query():
    data = flask.request.form  # is a dictionary
    location = data['some_location']
    requestString = formRequest(location)
    responses = makeGET(requestString)["candidates"]
    filename = os.path.join(app.config['UPLOAD_FOLDER'], "Mr Goose! copy.png")
    return flask.render_template('find.html', same=location)


def formRequest(input):
    return API_URL + "key={k}&input={i}".format(k=readKey(), i=input)


def makeGET(input):
    response = requests.get(input)
    if response:
        return response.json()
    else:
        return "Error GETting that URL. Check to see if it is well-formed?"


def readKey():
    # fetches key from secrets.findplacefromtext
    f = open("secrets.txt", "r")
    contents = f.read()
    return contents.strip()


if __name__ == '__main__':
    app.run(debug=True)
