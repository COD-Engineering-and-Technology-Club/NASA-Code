
import socket


HOST='192.168.1.144'
PORT=9500
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((HOST, PORT))


go = 'true'
while go == 'true':
	s.connect((HOST, PORT))
	data = s.recv(10)
	send = data.decode()
	print (send)
	if data == b'close':
		go = 'false'
	s.close

s.close()
exit(0)
