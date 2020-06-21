import RPi.GPIO as GPIO
import time

servoPIN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 als PWM mit 50Hz
p.start(2.5) # Initialisierung
try:
  p.ChangeDutyCycle(8)
  time.sleep(0.5)
  p.stop();
  GPIO.cleanup()
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
