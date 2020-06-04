#!/usr/bin/python3

import socket
import getopt
from sys import argv, exit, stdin


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


def createSocket(host, port, protocol):
    host = host
    port = port
    protocol = protocol
    if protocol == 'tcp':
        print("Protocolo TCP")
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print("Failed to create socket")
            exit()
        s.connect((host, port))
        while True:
            try:
                msg = input("Enter message to send: ")
                s.send(msg.encode('ascii'))        
                if msg == 'exit':
                    s.close()
                    break
            except EOFError:
                break
    elif protocol == 'udp':
        print("Protocolo UDP")
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except socket.error:
            print("Failed to create socket")
            exit()
        while True:
            msg = input('Enter message to send : ').encode()
            s.sendto(msg, (host, port))
            if msg.decode() == 'exit':
                s.close()
                break
    else:
        print('Protocolo ingresado no válido')

createSocket(host, port, protocol)
