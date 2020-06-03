# This program binds itself to a specific address and port
# and will listen for incoming TCP communications.

#!/usr/bin/env python3

import socket

SRV_ADDR = input("Server IP: ")
SRV_PORT = int(input("Server port: "))

# Create a new socket using a default family socket (AF_INET)
# that uses TCP and the default socket type connection-oriented
# (SOCK,STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Socket configuration
s.bind((SRV_ADDR, SRV_PORT))
s.listen(1)
print("Server started! Waiting for connections...")
# Accept incoming connections
# connection => the socket object to send/recieve data
# address => contains client address bound to the socket
connection, address = s.accept()
print("Client connected with address: ", address)
while 1:
	data = connection.recv(1024)
	if not data: 
		break
	# sendall() continues to send data from bytes until
	# either all data has been sent or an error occurs.
	# None is returned on success.
	connection.sendall(b'--Message Recieved--\n')
	print(data.decode('utf-8'))
connection.close()