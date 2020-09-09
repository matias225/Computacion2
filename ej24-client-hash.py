#!/usr/bin/python3

from sys import argv, exit
from getopt import getopt, GetoptError
from socket import socket, AF_INET, SOCK_STREAM


def getOptions():
    if len(argv[1:]) == 0:
        print('Por favor ingrese: -p seguido del puerto, -h seguido del host, -c seguido de una cadena entre '', --hash seguido del hash')
        exit()
    try:
        (opts, arg) = getopt(argv[1:], 'p:h:c:', ['hash='])
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
    if opts == '-c':
        string = arg
    if opts == '--hash':
        hash_function = arg


def createSocketTCP(port, host, hash_function, string):
    try:
        clientSocket = socket(AF_INET, SOCK_STREAM)
    except error:
        print("Failed to create socket")
        exit()
    clientSocket.connect((host, port))
    sendMsg(clientSocket, hash_function, string)


def sendMsg(clientSocket, hash_function, string):
    msg = hash_function+'.'+string
    clientSocket.send(msg.encode('ascii'))
    data = clientSocket.recv(1024)
    msg = data.decode('ascii')
    print('El hash '+hash_function+' de la cadena "'+string+'" es: \n'+msg)


if __name__ == "__main__":
    createSocketTCP(port, host, hash_function, string)
    