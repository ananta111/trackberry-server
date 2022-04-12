import urllib.parse
import certifi
from device_control.device_control import *
from threading import Thread
from database.db import initialize_db
from flask import Flask, request, Response
from datetime import datetime
from models.markers import Feature
import os

app = Flask(__name__)

task = SensorTask()

# task
task = SensorTask()

username = urllib.parse.quote(os.environ.get("MONGO_USERNAME"))
pwd = urllib.parse.quote(os.environ.get("MONGO_PASSWORD"))

url = "mongodb+srv://" + username + ":" + pwd + "@cluster0.bxjmr.mongodb.net/track-berry?retryWrites=true&w=majority"

app.config['MONGODB_SETTINGS'] = {
    "host": url,
    "tlsCAFile": certifi.where()
}

initialize_db(app)


def enable_cors(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response



@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/markers", methods=["POST"])
def new_marker():
    body = request.get_json()
    print(body)
    marker = Feature(**body)
    marker.properties.time = str(datetime.utcnow())
    marker.save()
    id = marker.id
    return {'id': str(id)}, 200


@app.route('/markers',  methods=["GET"])
def get_markers():
    markers = Feature.objects().to_json()
    return enable_cors(Response(markers, mimetype="application/json", status=200))


@app.route('/gps/<state>')
def device_control(state):
    if state == "on":
        t = Thread(target=task.run)
        t.start()
        print ("thread started")
        return enable_cors(Response("Sensing Started", status=200))
    if state == "off":
        task.terminate()
        return enable_cors(Response("Sensing Stopped", status=200))


if __name__ == '__main__':
    app.run()
