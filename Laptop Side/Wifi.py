#!/usr/bin/python3

#ssh pi@192.168.1.125 sudo python NASA/Wifi.py
import socket

#HOST='192.168.1.144'
PORT=9500
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', PORT))
s.listen(1)
#conn, addr=s.accept()
#s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
#print ('Connected by', addr)

while True:
	conn, addr = s.accept()
	msg = "This is a message"
	conn.send(msg)
#	wait = input("blah")
	if (msg == '1'):
		exit(0)
	conn.close()
	
s.close()

