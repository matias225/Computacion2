#!/usr/bin/python3

import socket
import getopt
import sys
import os


def getOptions():
    try:
        (opts, arg) = getopt.getopt(sys.argv[1:], 'p:t:f:', [])
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
    if opts == '-f':
        pathfile = arg


def createSocket(port, protocol, pathfile):
    port = port
    prot = protocol
    file = pathfile
    if prot == 'tcp':
        print('Protocolo TCP')
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        host = ""
        serversocket.bind((host, port))
        serversocket.listen(5)
        print('Server waiting for clients...')
        clientsocket, addr = serversocket.accept()
        while True:
            f = open(file, "a")
            data = clientsocket.recv(1024)
            f.write(data.decode("ascii")+'\n')    
            print("Address: %s " % str(addr))
            print("Recibido: "+data.decode("ascii"))
            if data.decode('ascii') == 'exit':
                serversocket.close()
                f.close()
                break
    elif prot == 'udp':
        print('Protocolo UPD')
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        host = ""
        serversocket.bind((host, port))
        while True:
            f = open(file, "a")
            data, addr = serversocket.recvfrom(1024)
            f.write(data.decode("ascii")+'\n')    
            address = addr[0]
            port = addr[1]
            print("Address: %s - Port %d" % (address, port))
            print("Recibido: "+data.decode("ascii"))
            if data.decode('ascii') == 'exit':
                serversocket.close()
                f.close()
                break
    else:
        print('Protocolo ingresado no válido')

createSocket(port, protocol, pathfile) 
