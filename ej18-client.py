#!/usr/bin/python3

from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM, error
from getopt import getopt, GetoptError
from sys import argv


def getOptions():
    try:
        (opts, arg) = getopt(argv[1:], 'p:h:t:', [])
        return opts
    except GetoptError as error:
        print('Wrong option: '+str(error))
        exit()

options = getOptions()
for (opts, arg) in options:
    if opts == '-p':
        port = int(arg)
    if opts == '-h':
        host = arg
    if opts == '-t':
        protocol = arg


def createSocketTCP(host, port):
    host = host
    port = port
    try:
        s = socket(AF_INET, SOCK_STREAM)
    except error:
        print("Failed to create socket")
        exit()
    s.connect((host, port))
    time = s.recv(1024).decode('utf-8')
    try:
        print("Fecha y hora actual (UTC): "+str(time))
    except UnicodeDecodeError as error:
        print(error)
    

def createSocketUDP(host, port):
    host = host
    port = port
    try:
        serversocket = socket(AF_INET, SOCK_DGRAM) 
    except error:
        print("Failed to create socket")
        exit()
    serversocket.sendto("".encode(), (host, port))
    time = serversocket.recvfrom(1024).decode('utf-8')
    try:
        print("Fecha y hora actual (UTC): "+str(time))
    except UnicodeDecodeError as error:
        print(error)
    

if __name__ == "__main__":
    if protocol == 'tcp':
        # Utilizar el puerto 13 y host time.nist.gov
        print('Protocolo TCP:')
        createSocketTCP(host, port)
    elif protocol == 'udp':
        print('Protocolo UDP:')
        createSocketUDP(host, port)
