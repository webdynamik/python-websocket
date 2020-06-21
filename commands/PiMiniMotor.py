import RPi.GPIO as GPIO
import time
servoPIN = 21
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50)
p.start(8)

def penOff():
  p.ChangeDutyCycle(8)
  time.sleep(0.5)

def penOn():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(servoPIN, GPIO.OUT)
  p = GPIO.PWM(servoPIN, 50)
  p.ChangeDutyCycle(10)
  time.sleep(0.5)