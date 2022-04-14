import serial, time, datetime

from models.markers import Feature


class SensorTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self):
        lat, lng = 36.13418509051332, -80.26259050468371
        while self._running:
            data = {"type": "Feature",
             "geometry": {"type": "Point", "coordinates": [lat, lng]},
             "properties": {}
            }
            marker = Feature(**data)
            marker.properties.time = str(datetime.datetime.utcnow())
            marker.save()
            id = marker.id
            time.sleep(2)
            lat -= 0.5
            lng += 0.7
            print("saved ")
        print("GPS Sensing Stopped")




