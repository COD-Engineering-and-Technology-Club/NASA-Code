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
	CO = Conveyor
   Callback Funct. Meanings:
	ltx,lty = Left Thumbstick X axis or Y axis
	"""

if __name__ == '__main__':
#establishing socket connections	
	HOST='192.168.1.125'
	PORT=9500
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	
#instantiates the generic xbox Controller settings 
	xboxCont = XboxController.XboxController(
		controllerCallBack = None,
		joystickNo = 0,
		deadzone = 0.5,
#deadzone controls the sensitivity(minimum value the controller should pick up on)
		scale = 1,
#scale controlls map and constrain
#Ex. when scale = 1, takes whatever input from controller and change values to
#something between -1 and 1
		invertYAxis = True)

	def ltxCall(val):
#pwm takes val from -1 to 1
#and changes it from 1 to 100 for GPIO ChangeDutyCycle
#might seem redundant to first set scale to 1, but by default it will consider
#negative values.
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
		return 0

        def aCall(val):
                if val != 0:
                        pwm = 90.0
                        msg = "AU"+str(pwm)
                        print(msg)
                        send = msg.encode()
                        s.send(send)
                        return 0
	
	def bCall(val):
                if val != 0:
                        pwm = 10.0
                        msg = "AU"+str(pwm)
                        print(msg)
                        send = msg.encode()
                        s.send(send)
                        return 0
    
	def xCall(val):
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
                if val != 0:
                        pwm = 10.0
                        msg = "TI"+str(pwm)
                        print(msg)
                        send = msg.encode()
                        s.send(send)
        
		return 0
    
	def rbCall(val):
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

	try:
		xboxCont.start()
		print("WEEOOOHWEEEOHH")
		#How long you want before it asks for new info from xbox
		while True:
			time.sleep(.05)
#exception handling
	except KeyboardInterrupt:
		print("User cancelled")
	except:
		print("Unexpected error: "), sys.exc_info()[0]
		raise
	finally:
		xboxCont.stop()
		exit(0)
		s.close()
