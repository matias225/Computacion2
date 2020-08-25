#!/usr/bin/python3

from getopt import getopt, GetoptError
from socket import socket, AF_INET, SOCK_STREAM
from sys import argv, exit


def createSocketTCP(host, port):
    host = host
    port = port
    try:
        clientSocket = socket(AF_INET, SOCK_STREAM)
    except error:
        print("Failed to create socket")
        exit()
    clientSocket.connect((host, port))
    while True:
        try:
            msg = input(">>> ")
            clientSocket.send(msg.encode('ascii'))        
            if msg == 'exit':
                clientSocket.close()
                break
            #msg = clientSocket.recv(2048)
            #resp = msg.decode('ascii')
            #print('--> '+resp)
        except EOFError:
            break


def getOptions():
    if len(argv[1:]) == 0:
        print('Por favor ingrese -p seguido seguido del puerto y -h seguido del host')
        exit()
    try:
        (opts, arg) = getopt(argv[1:], 'p:h:', [])
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


if __name__ == "__main__":
    createSocketTCP(host, port)