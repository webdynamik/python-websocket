import RPi.GPIO as GPIO
import time
servoPIN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50)

def penOff():
  p.start(10)
  p.ChangeDutyCycle(8)
  p.stop()
  time.sleep(0.5)

def penOn():
  p.start(8)
  p.ChangeDutyCycle(10)
  p.stop()
  time.sleep(0.5)
