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

print(port)
print(protocol)
print(pathfile)


def createFile(pathfile):
    file = pathfile
    if not os.path.exists(file):
        f = open(file, "w")
    return


def createSocket(port, protocol):
    port = port
    prot = protocol
    if prot == 'tcp':
        print('Protocolo TCP')
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        host = ""
        serversocket.bind((host, port))
        serversocket.listen(5)
        clientsocket, addr = serversocket.accept()
        while True:
            data = clientsocket.recv(1024)
            print("Address: %s " % str(addr))
            print("Recibido: "+data.decode("ascii"))
            msg = input('Enter message to send : ')
            clientsocket.send(msg.encode('ascii'))
    elif prot == 'udp':
        print('Protocolo UPD')
    else:
        print('Protocolo ingresado no válido')


createFile(pathfile)
createSocket(port, protocol)
# Ejemplo
# createFile('/tmp/temp.txt')
