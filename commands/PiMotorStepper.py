import boards.PiMotor as PiMotor
import time
import RPi.GPIO as GPIO

m1 = PiMotor.Stepper("STEPPER1")

def forward(delay, rotations):
	m1.forward(delay, rotations)