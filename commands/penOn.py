import RPi.GPIO as GPIO2
import time

servoPIN = 21
GPIO2.setmode(GPIO2.BCM)
GPIO2.setup(servoPIN, GPIO2.OUT)
p = GPIO2.PWM(servoPIN, 50) # GPIO 17 als PWM mit 50Hz
p.start(2.5) # Initialisierung
p.ChangeDutyCycle(8)
time.sleep(0.5)
p.stop();
GPIO2.cleanup()


