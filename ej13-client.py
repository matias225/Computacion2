#!/usr/bin/python3

import os
import socket
import sys
import getopt


def getOptions():
    try:
        (opts, arg) = getopt.getopt(sys.argv[1:], 'l:', [])
        return opts
    except getopt.GetoptError as error:
        print('Wrong Option: '+str(error))
        exit()


options = getOptions()
for (opts, arg) in options:
    if opts == '-l':
        log = arg


host = ""
port = 8200

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Failed to create socket")
    exit()

s.connect((host, port))

while True:
    msg = input('> ')
    s.send(msg.encode('ascii'))
    msg = s.recv(2048)
    if msg.decode('ascii') == 'exit':
        s.close()
        print('Cerrando conexión...')
        break
    else:
        print(msg.decode('ascii'))
