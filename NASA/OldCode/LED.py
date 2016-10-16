import XboxController
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
c1=GPIO.PWM(16, 50)
c2=GPIO.PWM(20, 50)
c3=GPIO.PWM(21,50)

c1.start(100)
time.sleep(1)
c1.stop()
c2.start(100)
time.sleep(1)
c2.stop()
c3.start(100)
time.sleep(1)
c3.stop()
c1.start(33)
c2.start(33)
c3.start(33)
time.sleep(3)
c1.stop()
c2.stop()




