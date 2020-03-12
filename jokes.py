from flask import Flask, request, url_for
import requests
import json
import random

app = Flask(__name__)
@app.route('/')
def hello():
    return "lmao"

@app.route('/getJokes', methods=['GET'])
def request():
    jokesdic = 'http://api.icndb.com/jokes/random/'
    joke = requests.get(jokesdic)
    # jokes = []
    # for i in (0,10):
    #     jokes.append(json.loads(joke.text), ['value'])

    return json.loads(joke.text)['value']

if __name__ == "__main__":
    app.run(debug=True)