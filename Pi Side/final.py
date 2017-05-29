#!/usr/bin/python3

import socket

PORT=9500
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', PORT))
s.listen(1)
s.setsockopt(socket.IPPROTO_TCP , socket.TCP_NODELAY , 1 )
conn, addr = s.accept()

GPIO.setup(06, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

#this pwm setup might change to start button initializtion
Drive = GPIO.PWM(05, 50)        
Steer = GPIO.PWM(06, 50)
Auger = GPIO.PWM(13, 50)
Slide = GPIO.PWM(19, 50)
Tilt = GPIO.PWM(26, 50)
Convey = GPIO.PWM(21,50)
Drive.start(50)
Steer.start(50)
Auger.start(50)
Slide.start(50)
Tilt.start(50)
Convey.start(0)

augerCount = 1
tiltCount = 1
conveyorCount = 1
while True:
	info = conn.recv(6).decode()
	if info[:2] == 'DR':
		pwm = float(info[2:])
		Drive.ChangeDutyCycle(pwm)
	if info[:2] == 'ST':
		pwm = float(info[2:])
		Steer.ChangeDutyCycle(pwm)
	if info[:2] == 'AU':
		pwm = float(info[2:])
		augerCount = augerCount +1
		if augerCount % 2 == 0:
			Auger.ChangeDutyCycle(pwm)
		else:
			Auger.ChangeDutyCycle(50)				
	if info[:2] == 'SL':
		pwm = float(info[2:])
		Slide.ChangeDutyCycle(pwm)
		
	if info[:2] == 'TI':
		tiltCount = tiltCount + 1
		pwm = float(info[2:])
		if tiltCount % 2 == 0:
			Tilt.ChangeDutyCycle(pwm)
		else:
			Tilt.ChangeDutyCycle(50)
			
			
	if info[:2] == 'CO':
		conveyorCount = conveyorCount + 1
		if conveyorCount %2 == 1:
			Convey.ChangeDutyCycle(90)
		else:
			Convey.ChangeDutyCycle(50)
s.close()
exit(0)
