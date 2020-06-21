import RPi.GPIO as GPIO
import time
servoPIN = 21

def penOff():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(servoPIN, GPIO.OUT)
  p = GPIO.PWM(servoPIN, 50)
  p.start(2.5)
  p.ChangeDutyCycle(8)
  time.sleep(0.5)
  p.stop();
  GPIO.cleanup()

def penOn():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(servoPIN, GPIO.OUT)
  p = GPIO.PWM(servoPIN, 50)
  p.start(1)
  p.ChangeDutyCycle(10)
  time.sleep(0.5)
  p.stop();
  GPIO.cleanup()
