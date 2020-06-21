import RPi.GPIO as GPIO
import time
servoPIN = 21

def penOff():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(servoPIN, GPIO.OUT)
  p = GPIO.PWM(servoPIN, 50)
  p.start(10)
  p.ChangeDutyCycle(8)
  p.stop()
  time.sleep(0.5)
  GPIO.cleanup()

def penOn():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(servoPIN, GPIO.OUT)
  p = GPIO.PWM(servoPIN, 50)
  p.start(8)
  p.ChangeDutyCycle(10)
  p.stop()
  time.sleep(0.5)
  GPIO.cleanup()
