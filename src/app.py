#!/usr/bin/env python3

from flask import Flask, request, jsonify
from flask.logging import default_handler
import logging
import os

app = Flask(__name__)

def lang(input):
    if input == "es":
        return "Hola"
    else:
        return "Hello"

# Configure logging as needed
app.config["LOG_LEVEL"] = os.environ.get("DEBUG")
log = logging.getLogger('werkzeug')
if app.config["LOG_LEVEL"]:
    log.setLevel(logging.DEBUG)
else:
    log.setLevel(logging.ERROR)

@app.route('/<name>', methods=["GET", "POST"])
def hello_world(name):

    # See if we are requesting a language arg
    if 'lang' in request.args:
        greeting = lang(request.args['lang']);
    else:
        greeting = lang(None);

    data = f"{greeting} {name}!"

    # Parse for the accept header to be type application/json if it exists
    try:
        accept_header = request.headers['Accept']
    except KeyError:
        # Default to none if our header is not found
        accept_header = None

    # Our response depends on the method
    if request.method == 'GET':
        # Configure your response based on what we got
        if accept_header == "application/json":
            return jsonify(msgs=[data])
        else:
            return f"{data}"
    else:
        # Homework problem did not define how we wanted to handle a POST,
        # defaulting to returning hello world for now
        return f"<p>{greeting} {name}</p>"
