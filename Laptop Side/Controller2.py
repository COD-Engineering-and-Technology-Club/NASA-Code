#!/usr/bin/python3

import XboxController
import time
import socket

"""Packet Meanings:
	DR = Drive
	ST = Steer(Actuator)
	AU = Auger
	TI = Tilt(Actuators)
	SL = BallsScrew Slide
	CO = Conveyor"""

if __name__ == '__main__':
	
	HOST='192.168.1.125'
	PORT=9500
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	

	xboxCont = XboxController.XboxController(
		controllerCallBack = None,
		joystickNo = 0,
		deadzone = 0.5,
		scale = 1,
		invertYAxis = True)

	def ltxCall(val):
        #steer the robot
        #I'm assuming that the val is just a one or a zero
		"""pwm takes val from -1 to 1
		and changes it from 1 to 100
		for GPIO ChangeDutyCycle"""
		pwm = (val + 1)/.02
		pwm = round(pwm,0)
		if pwm > 90:
			pwm = 90.0
		elif pwm < 10:
			pwm = 10.0

		msg = "ST"+str(pwm)
		print(msg)
		data = msg.encode()
		s.send(data)
		return 0

	def ltyCall(val):
        #drive
		pwm = (val + 1)/.02
		pwm = round(pwm,0)
		if pwm > 90:
			pwm = 90.0
		elif pwm < 10:
			pwm = 10.0

		msg = "DR"+str(pwm)
		print(msg)
		send = msg.encode()
		s.send(send)
		return 0
	
	def rtxCall(val):
        #BallScrew Slide
                pwm = (val)/.02
		pwm = round(pwm,0)
		if pwm > 90:
			pwm = 90.0
		elif pwm < 10:
			pwm = 10.0
		msg = "SL"+str(pwm)
		print(msg)
		send = msg.encode()
		s.send(send)
		return 0

	def rtyCall(val):
        #BallScrew Slide down?
                pwm = (-1*val + 1)/.02
		pwm = round(pwm,0)
		if pwm > 90:
			pwm = 90.0
		elif pwm < 10:
			pwm = 10.0
		msg = "SL"+str(pwm)
		print(msg)
		send = msg.encode()
		s.send(send)
		return 0

	def rtrCall(val):
        #BallScrew Slide
		pwm = (-1*val + 1)/.02
		pwm = round(pwm,0)
		if pwm > 90:
			pwm = 90.0
		elif pwm < 10:
			pwm = 10.0
		msg = "SL"+str(pwm)
		print(msg)
		send = msg.encode()
		s.send(send)
		return 0

	def ltrCall(val):
        #Ballscrew slide
#                pwm = (val + 1)/.02
#		pwm = round(pwm,0)
#		if pwm > 90:
#			pwm = 90.0
#		elif pwm < 10:
#			pwm = 10.0
#		msg = "SL"+str(pwm)
#		print(msg)
#		send = msg.encode()
#		s.send(send)
		return 0

    def aCall(val):
    #auger
        if val != 0:
            pwm = 90.0
            msg = "AU"+str(pwm)
            print(msg)
            send = msg.encode()
            s.send(send)
            return 0
        #this currently returns nothing if the val is not zero is that correct?
	
	def bCall(val):
    #auger
        if val != 0:
            pwm = 10.0
            msg = "AU"+str(pwm)
            print(msg)
            send = msg.encode()
            s.send(send)
            return 0
    
	def xCall(val):
    #conveyor
        if val != 0:
            pwm = 90.0
            msg = "CO"+str(pwm)
            print(msg)
            send = msg.encode()
            s.send(send)
            return 0
    
	def yCall(val):        
		return 0
    
	def lbCall(val):
    #tilt
        if val != 0:
            pwm = 10.0
            msg = "TI"+str(pwm)
            print(msg)
            send = msg.encode()
            s.send(send)
		return 0
    
	def rbCall(val):
    #tilt
        if val != 0:
            pwm = 90.0
            msg = "TI"+str(pwm)
            print(msg)
            send = msg.encode()
            s.send(send)
		return 0
    
	def bckCall(val):        
		return 0
    
	def strCall(val):        
		return 0
    
	def xbCall(val):        
		return 0





##links buttons to the above functions
    
	xboxCont.setupControlCallback(xboxCont.XboxControls.LTHUMBX, ltxCall)
	xboxCont.setupControlCallback(xboxCont.XboxControls.LTHUMBY, ltyCall)
#	xboxCont.setupControlCallback(xboxCont.XboxControls.RTHUMBX, rtxCall)
	xboxCont.setupControlCallback(xboxCont.XboxControls.RTHUMBY, rtyCall)
	xboxCont.setupControlCallback(xboxCont.XboxControls.A, aCall)
	xboxCont.setupControlCallback(xboxCont.XboxControls.B, bCall)
	xboxCont.setupControlCallback(xboxCont.XboxControls.X, xCall)
	xboxCont.setupControlCallback(xboxCont.XboxControls.Y, yCall)
	xboxCont.setupControlCallback(xboxCont.XboxControls.LB, lbCall)
	xboxCont.setupControlCallback(xboxCont.XboxControls.RB, rbCall)
	xboxCont.setupControlCallback(xboxCont.XboxControls.BACK, bckCall)
	xboxCont.setupControlCallback(xboxCont.XboxControls.START, strCall)
	xboxCont.setupControlCallback(xboxCont.XboxControls.XBOX, xbCall)
#	xboxCont.setupControlCallback(xboxCont.XboxControls.RTRIGGER, rtrCall)
#	xboxCont.setupControlCallback(xboxCont.XboxControls.LTRIGGER, ltrCall)

##tests...

	try:
		xboxCont.start()
		print("WEEOOOHWEEEOHH")
		#How long you want before it asks for new info from xbox
		while True:
			time.sleep(.05)

	except KeyboardInterrupt:
		print("User cancelled")
	except:
		print("Unexpected error: "), sys.exc_info()[0]
		raise
	finally:
		xboxCont.stop()
		exit(0)
		s.close()
