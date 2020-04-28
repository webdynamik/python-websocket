import socketio
import RPi.GPIO as GPIO
from commands.PiMotorStepper import m1Forward as PiMotorStepperForward, m1Backward as PiMotorStepperBackward, m2Forward as PiMotorStepper2Forward, m2Backward as PiMotorStepper2Backward
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

    @sio.on('motor')
    def Motor(data):
        print('set Motor to: ', data)
        if data['motor'] == '2' and data['directioin'] == 'forward' :
            PiMotorStepper2Forward(data['delay'],data['rotations']);
        elif data['motor'] == '2' and data['directioin'] == 'backward' :
            PiMotorStepper2Backward(data['delay'],data['rotations']);
        elif data['motor'] == '1' and data['directioin'] == 'backward' :
            PiMotorStepperBackward(data['delay'],data['rotations']);
        else: 
            PiMotorStepperForward(data['delay'],data['rotations']);
        
    @sio.on('disconnect')
    def on_disconnect():
        print('disconnected from server')

    sio.connect('http://192.168.178.29:8888')
    sio.wait()
except KeyboardInterrupt:
        stop()
        GPIO.cleanup();
        print('bye bye')

