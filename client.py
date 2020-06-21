import config
import socketio
from commands.PiMotorStepper import m1Stop as PiMotorStepperStop, m2Stop as PiMotorStepper2Stop, m1Forward as PiMotorStepperForward, m1Backward as PiMotorStepperBackward, m2Forward as PiMotorStepper2Forward, m2Backward as PiMotorStepper2Backward
import os

try:
    sio = socketio.Client()

    @sio.on('connect')
    def on_connect():
        print('connection established')
        print(config.motors)
        sio.emit('setOnline', config.motors)

    @sio.on('sayHello')
    def on_say_hello():
        print('on_say_hello')
        print(config.motors)
        sio.emit('setOnline', config.motors)

    @sio.on('pen')
    def pen(data):
        print('-> pen', data)
        if data == 'on' :
            os.system("python commands/penOn.py");
        else:
            os.system("python commands/penOff.py");

    @sio.on('stop')
    def stop(data):
        print('-> stop', data)
        if data['motor'] == '1' :
            PiMotorStepperStop();
        else:
            PiMotorStepper2Stop();

    @sio.on('motor')
    def Motor(data):
        print('set Motor to: ', data)

        if data['motor'] == '2' and data['direction'] == 'forward' :
            PiMotorStepper2Forward(data['delay'],data['rotations']);
        elif data['motor'] == '2' and data['direction'] == 'backward' :
            PiMotorStepper2Backward(data['delay'],data['rotations']);
        elif data['motor'] == '1' and data['direction'] == 'backward' :
            PiMotorStepperBackward(data['delay'],data['rotations']);
        else: 
            PiMotorStepperForward(data['delay'],data['rotations']);
        
    @sio.on('disconnect')
    def on_disconnect():
        print('disconnected from server')

    sio.connect('http://192.168.178.29:8888')
    sio.wait()

except KeyboardInterrupt:
        print('bye bye')

