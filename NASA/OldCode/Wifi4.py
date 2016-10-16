#!/usr/bin/python3

import socket


PORT=9500
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', PORT))
s.listen(1)
conn, addr = s.accept()
s.setsockopt(socket.IPPROTO_TCP , socket.TCP_NODELAY , 1 )

if __name__ == '__main__':

	try:
data = s.recv(30)
	send = data.decode()
	print (send)
	if data == b'close':
		go = 'false'

s.close()
exit(0)
