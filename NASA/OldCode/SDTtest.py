#this code successfully works to press the button once and have it
#trigger the LED
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

xboxCont=XboxController.XboxController(
	controllerCallBack = None,
	deadzone = 30,
	joystickNo = 0,
	scale = 100,
	invertYAxis = True)


"""def c1Callback(value):
	if(value > 8000):
                pwm = 100
        elif(value > 6000):
                pwm = 90
        elif(value > 4000):
                pwm = 80
        elif(value > 2000):
                pwm = 60
        elif(value > 0):
                pwm = 50
        elif(value > -2000):
                pwm = 40
        elif(value > -4000):
                pwm = 30
        elif(value > -6000):
                pwm = 20
        elif(value > -8000):
                pwm = 10
        else:
		pwm=0
	c1.start(pwm)
	time.sleep(1)
	c1.stop(pwm)"""
def c1Callback(value):
	c1.start(100)
"""xboxCont.setupControlCallback(
	xboxCont.XboxControls.LTHUMBX,
	c1Callback)"""
xboxCont.setupControlCallback(
	xboxCont.XboxControls.A,
	c1Callback)
xboxCont.start()
while True:
	time.sleep(.1)

xboxCont.stop()

