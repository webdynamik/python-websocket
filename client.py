import socketio
import RPi.GPIO as GPIO
from boards.PiMotorStepper import forward as PiMotorStepperForward

try:
    sio = socketio.Client()

    @sio.on('connect')
    def on_connect():
        print('connection established')
        sio.emit('hallo', 'PiMotorStepper')
        sio.emit('add-devices', [{
                                    "name": "SMARS",
                                    "type": "smars",
                                    "ip": "x",
                                    "location": '',
                                    "component": "smarsComponent"
                                  }])
        print('--')

    @sio.on('display')
    def on_message(data):
        print('received: ', data)

    @sio.on('get')
    def get(data):
        #fn({status: 1, value: 1, index: data.index})
        print('get: ', data)

    @sio.on('SmarsSet')
    def SmarsSet(data):
        print('set: ', data)
        exec( data+'()');
        
    @sio.on('disconnect')
    def on_disconnect():
        print('disconnected from server')

    sio.connect('http://192.168.178.29:8888')
    sio.wait()
except KeyboardInterrupt:
        stop()
        GPIO.cleanup();
        print('bye bye')

