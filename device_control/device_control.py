import serial, time


class SensorTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self):
        i = 0
        while self._running:
            # ser = serial.Serial('/dev/ttyACM0')
            # ser_bytes = ser.readline()
            print ("Hello " + str(i))
            time.sleep(0.5)
            i += 1
        print("GPS Sensing Stopped")




