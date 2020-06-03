#!/usr/bin/env python3

import socket

SRV_ADDR = input("Server IP: ")
SRV_PORT = int(input("Server port: "))
MESSAGE = input("Message to send: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SRV_ADDR, SRV_PORT))
    s.sendall(MESSAGE.encode())
    data = s.recv(1024)

print('Received', repr(data))