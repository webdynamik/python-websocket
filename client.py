import socketio
import RPi.GPIO as GPIO
from commands.PiMotorStepper import forward as PiMotorStepperForward, backward as PiMotorStepperBackward
import sys, getopt

try:
    sio = socketio.Client()

    @sio.on('connect')
    def on_connect():
        print('connection established')
        sio.emit('hallo', {"name": "PiMotorStepper", "fingerprint": "PiMotorStepper"})
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

    @sio.on('StepperForward')
    def StepperForward(data):
        print('forward: ', data)
        PiMotorStepperForward(data['delay'],data['rotations']);

    @sio.on('StepperBackward')
    def StepperBackward(data):
        print('backward: ', data)
        PiMotorStepperBackward(data['delay'],data['rotations']);

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

