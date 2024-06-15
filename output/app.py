import flask
from flask import Flask
import json

app = Flask("app")


@app.get('/hello_world')
def respond_get_hello_world():
    return flask.Response(response='"Hello world"',
                          status=200,
                          mimetype="",
                          content_type="text/plain")


@app.put('/test')
def respond_get_test():
    return flask.Response(response=json.loads(json.dumps({"Hello": "world"})),
                          status=201,
                          mimetype="",
                          content_type="application/json")
