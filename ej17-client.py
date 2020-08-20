#!/usr/bin/python3

from socket import socket, error, AF_INET, SOCK_STREAM
from getopt import getopt, GetoptError
from sys import argv, exit, stdin


def getOptions():
    try:
        (opts, arg) = getopt(argv[1:], 'p:h:', [])
        return opts
    except GetoptError as error:
        print('Wrong Option: '+str(error))
        exit()


options = getOptions()
for (opts, arg) in options:
    if opts == '-p':
        port = int(arg)
    if opts == '-h':
        host = arg


def createSocket(host, port):
    host = host
    port = port
    try:
        s = socket(AF_INET, SOCK_STREAM)
    except error:
        print("Failed to create socket")
        exit()
    s.connect((host, port))
    while True:
        try:
            msg = input(">>> ")
            s.send(msg.encode('ascii'))        
            if msg == 'exit':
                s.close()
                break
            msg = s.recv(2048)
            resp = msg.decode('ascii')
            print('--> '+resp)
        except EOFError:
            break

if __name__ == "__main__":
    createSocket(host, port)
