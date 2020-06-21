import RPi.GPIO as GPIO
import time
servoPIN = 21

def penOff():
  GPIO.setup(servoPIN, GPIO.OUT)
  p = GPIO.PWM(servoPIN, 50)
  p.start(10)
  p.ChangeDutyCycle(8)
  p.stop()
  time.sleep(0.5)
  GPIO.clearup()

def penOn():
  GPIO.setup(servoPIN, GPIO.OUT)
  p = GPIO.PWM(servoPIN, 50)
  p.start(8)
  p.ChangeDutyCycle(10)
  p.stop()
  time.sleep(0.5)
  GPIO.clearup()