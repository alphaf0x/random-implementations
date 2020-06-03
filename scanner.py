#!/usr/bin/env python3

import socket

target = input('Enter the IP address to scan: ')
port_range = input('Enter the port range to scan: ') # ex.range(5-200)

startport = int(port_range.split('-')[0])
endport = int(port_range.split('-')[1])

print('Scanning host', target, 'from port', startport, 'to port', endport)

for port in range(startport,endport):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	status = s.connect_ex((target, port))
	if (status == 0):
		print('*** Port', port,'- OPEN ***')
	else:
		print('Port', port,'- CLOSED')
	s.close()