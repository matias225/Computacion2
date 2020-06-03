#!/usr/bin/python3

import socket
import getopt
from sys import argv, exit

def getOptions():
    try:
        (opts, arg) = getopt.getopt(argv[1:], 'a:t:p:', [])
        return opts
    except getopt.GetoptError as error:
        print('Wrong Option: '+str(error))
        exit()

options = getOptions()
for (opts, arg) in options:
    if opts == '-p':
        port = int(arg)
    if opts == '-t':
        protocol = arg
    if opts == '-a':
        host = arg

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Failed to create socket")
    exit()

s.connect((host, port))

while(True) :
    msg = input('Enter message to send : ')
    #Set the whole string
    s.send(msg.encode('ascii'))
    # receive data from client (data, addr)
    msg = s.recv(1024)
    print('Server reply : ' + msg.decode("ascii"))
