import config
import socketio 
from commands.Drawbot import stop as DrawbotStop, left as DrawbotLeft, right as DrawbotRight, top as DrawbotTop, down as DrawbotDown, leftTop as DrawbotLeftTop, rightTop as DrawbotRightTop, leftDown as DrawbotLeftDown, rightDown as DrawbotRightDown
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
        DrawbotStop();

    @sio.on('motor')
    def Motor(data):
        print('set Motor to: ', data)

        if data['direction'] == 'down' :
            DrawbotDown(data['delay'],data['rotations']);
        elif data['direction'] == 'left' :
            DrawbotLeft(data['delay'],data['rotations']);
        elif data['direction'] == 'leftDown' :
            DrawbotLeftDown(data['delay'],data['rotations']);
        elif data['direction'] == 'leftTop' :
            DrawbotLeftTop(data['delay'],data['rotations']);
        elif data['direction'] == 'right' :
            DrawbotRight(data['delay'],data['rotations']);
        elif data['direction'] == 'rightDown' :
            DrawbotRightDown(data['delay'],data['rotations']);
        elif data['direction'] == 'rightTop' :
            DrawbotRightTop(data['delay'],data['rotations']);
        elif data['direction'] == 'top' :
            DrawbotTop(data['delay'],data['rotations']);

        
    @sio.on('disconnect')
    def on_disconnect():
        print('disconnected from server')

    sio.connect('http://192.168.178.29:8888')
    sio.wait()

except KeyboardInterrupt:
        print('bye bye')

