import boards.PiMotor as PiMotor
import time
import RPi.GPIO as GPIO

m1 = PiMotor.Stepper("STEPPER1")
m2 = PiMotor.Stepper("STEPPER2")

def m1Forward(delay, rotations):
	m1.forward(delay, rotations)

def m1Backward(delay, rotations):
	m1.backward(delay, rotations)

def m2Forward(delay, rotations):
	m2.forward(delay, rotations)

def m2Backward(delay, rotations):
	m2.backward(delay, rotations)