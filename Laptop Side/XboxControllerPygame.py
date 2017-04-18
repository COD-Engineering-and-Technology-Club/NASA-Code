#Nasa-bot drive code written in pygame
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