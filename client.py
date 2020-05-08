import config
import socketio
from commands.PiMotorStepper import m1Forward as PiMotorStepperForward, m1Backward as PiMotorStepperBackward, m2Forward as PiMotorStepper2Forward, m2Backward as PiMotorStepper2Backward

try:
    sio = socketio.Client()

    @sio.on('connect')
    def on_connect():
        print('connection established')
        print(motors)
        sio.emit('setOnline', motors)

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

