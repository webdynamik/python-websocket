import boards.PiMotor as PiMotor
import time
import RPi.GPIO as GPIO

m1 = PiMotor.Stepper("STEPPER1")

def forward():
	m1.forward(0.05,10)  # Delay and rotations