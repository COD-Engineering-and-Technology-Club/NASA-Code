
import socket

 
HOST='192.168.1.144'
PORT=9001
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


go = 'true'
while go == 'true':
	data = s.recv(20)
	print (data)
s.close()

exit(0)
