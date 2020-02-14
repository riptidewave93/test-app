#!/usr/bin/env python3

from flask import Flask, request
from flask.logging import default_handler
import logging
import os

app = Flask(__name__)

# Configure logging as needed
app.config["LOG_LEVEL"] = os.environ.get("DEBUG")
log = logging.getLogger('werkzeug')
if app.config["LOG_LEVEL"]:
    log.setLevel(logging.DEBUG)
else:
    log.setLevel(logging.ERROR)

@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == 'GET':
        # Parse for the accept header to be type application/json if it exists
        try:
            accept_header = request.headers['Accept']
        except:
            accept_header = None

        # Configure your response based on what we got
        if accept_header == "application/json":
            return '{"message": "Hello, World"}'
        else:
            return '<p>Hello, World</p>'
    else:
        # Homework problem did not define how we wanted to handle a POST,
        # defaulting to returning hello world for now
        return '<p>Hello, World</p>'
