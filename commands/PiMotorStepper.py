import boards.PiMotor as PiMotor
import time
import RPi.GPIO as GPIO

m1 = PiMotor.Stepper("STEPPER1")
m2 = PiMotor.Stepper("STEPPER2")

def forward(delay, rotations):
	m1.forward(delay, rotations)
	m2.forward(delay, rotations)

def backward(delay, rotations):
	m1.backward(delay, rotations)
	m2.backward(delay, rotations)