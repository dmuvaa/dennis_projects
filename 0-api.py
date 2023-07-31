#!/usr/bin/python3

"""Imports Modules"""

from flask import Flask
import jsonify
from flask import render_template
from flask import make_response
import session

app = Flask(__name__)

@app.route('/')
def hello():
    return "Dennis"

@app.route('hello/den')
def hello(name):
    return 'Hello ' + name + '!'

@app.route('/test')
@app.route('/test', methods=['GET', 'POST'])
@app.route('/test', methods=['PUT'])


if __name__ = '__main__':
    app.run(debug=True)
