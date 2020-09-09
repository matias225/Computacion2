#!/usr/bin/python3

from sys import argv, exit
from getopt import getopt, GetoptError
from socket import socket, AF_INET, SOCK_STREAM


def getOptions():
    if len(argv[1:]) == 0:
        print('Por favor ingrese: -p seguido del puerto, -h seguido del host, -c seguido del archivo, --hash seguido del hash')
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
        filename = arg
    if opts == '--hash':
        hash_function = arg


def createSocketTCP(port, host, hash_function, filename):
    port = port
    host = host
    try:
        clientSocket = socket(AF_INET, SOCK_STREAM)
    except error:
        print("Failed to create socket")
        exit()
    clientSocket.connect((host, port))


if __name__ == "__main__":
    #print(host, port, filename, hash_function)
    createSocketTCP(port, host, hash_function, filename)
    