import socket

HOST='192.168.1.81'
port=9500
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',port))
s.listen(1)
conn, addr=s.accept()
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
print ('Connected by', addr)
while True:
	msg = input('enter msg: ')
	

	conn.send(msg)
	if (msg == 'close'):
		exit(0)
s.close()
