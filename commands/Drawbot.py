import boards.PiMotor as PiMotor
import time

m1 = PiMotor.Stepper("STEPPER1")
m2 = PiMotor.Stepper("STEPPER2")

def left(delay, rotations):
	m1.backward(delay, rotations)
	m2.forward(delay, rotations)

def right(delay, rotations):
	m1.forward(delay, rotations)
	m2.backward(delay, rotations)

def top(delay, rotations):
	m1.backward(delay, rotations)
	m2.backward(delay, rotations)

def down(delay, rotations):
	m1.forward(delay, rotations)
	m2.forward(delay, rotations)

def leftTop(delay, rotations):
	m1.backward(delay, rotations)

def rightTop(delay, rotations):
	m2.backward(delay, rotations)

def leftDown(delay, rotations):
	m2.forward(delay, rotations)

def rightDown(delay, rotations):
	m1.forward(delay, rotations)

def stop():
	m1.stop()
	m2.stop()