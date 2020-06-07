#!/usr/bin/python3

import os
import socket
import sys

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ""
port = 8200
serversocket.bind((host, port))
serversocket.listen(5)
print('Server waiting for clients...')
clientsocket, addr = serversocket.accept()

while True:
    data = clientsocket.recv(1024)
    print("Address: %s " % str(addr))
    print("Comando recibido: "+data.decode('ascii'))
    if data.decode('ascii') == 'exit':
        clientsocket.send('exit'.encode('ascii'))
        serversocket.close()
        break
    command = data.decode("ascii")+ " > /tmp/out.txt 2> /tmp/error.txt"
    if os.system(command) == 0:
        f = open('/tmp/out.txt','r')
        msg = f.read()
        f.close()
        clientsocket.send('OK\n'.encode('ascii')+msg.encode('ascii'))
    else:
        e = open('/tmp/error.txt','r')
        msgerror = e.read()
        e.close()
        clientsocket.send('ERROR\n'.encode('ascii')+msgerror.encode('ascii'))
