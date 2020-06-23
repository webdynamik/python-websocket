from commands.Drawbot import stop, left, right, top, down, leftTop, rightTop, leftDown, rightDown
import config
import socketio 
import os

try:
    sio = socketio.Client()

    @sio.on('connect')
    def on_connect():
        print('connection established')
        sio.emit('setOnline', config.motors)

    @sio.on('sayHello')
    def on_say_hello():
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
        print('-> stop')
        stop();

    @sio.on('motor')
    def Motor(data):
        print('set Motor to: ', data)

        if data['direction'] == 'down' :
            down(data['delay'],data['rotations']);
        elif data['direction'] == 'left' :
            left(data['delay'],data['rotations']);
        elif data['direction'] == 'leftDown' :
            leftDown(data['delay'],data['rotations']);
        elif data['direction'] == 'leftTop' :
            leftTop(data['delay'],data['rotations']);
        elif data['direction'] == 'right' :
            right(data['delay'],data['rotations']);
        elif data['direction'] == 'rightDown' :
            rightDown(data['delay'],data['rotations']);
        elif data['direction'] == 'rightTop' :
            rightTop(data['delay'],data['rotations']);
        elif data['direction'] == 'top' :
            top(data['delay'],data['rotations']);

        
    @sio.on('disconnect')
    def on_disconnect():
        print('disconnected from server')

    sio.connect('http://192.168.178.29:8888')
    sio.wait()

except KeyboardInterrupt:
        print('bye bye')

