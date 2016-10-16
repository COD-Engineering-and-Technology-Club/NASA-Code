import socket
import RPi.GPIO as GPIO
import time

if __name__ == '__main__':
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(16, GPIO.OUT)
	GPIO.setup(20, GPIO.OUT)
	GPIO.setup(21, GPIO.OUT)
	#this pwm setup might change to start button initializtion
	c1 = GPIO.PWM(16, 50)
	c2 = GPIO.PWM(20, 50)
	c3 = GPIO.PWM(21, 50)

	HOST='192.168.1.144'
	PORT=9500
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))	

	while True:
        	data = s.recv(10)
        	info = data.decode()
		if info[0:2] == 'DR':
			pwm = info[2:5]
			c1.ChangeDutyCycle(pwm)
		if info[0:2] == 'ST':
			pwm = info[2:5]
			c2.ChangeDutyCycle(pwm)
		if info[0:2] == 'AU':
			pwm = info[2:5]
			c3.ChangeDutyCycle(pwm)
        
	try:
		while True:
			time.sleep(.5)
		c1.start(0)
        	c2.start(0)
        	c3.start(0)		
	finally:
		s.close()
		exit(0)
