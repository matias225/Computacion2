#!/usr/bin/python3

import socket
import getopt
import sys
import os

def getOptions():
    try:
        (opts, arg) = getopt.getopt(sys.argv[1:], 'p:h:t:', [])
        return opts
    except getopt.GetoptError as error:
        print('Wrong argument: '+str(error))
        exit()

options = getOptions()
for (opts, arg) in options:
    if opts == '-p':
        port = int(arg)
    if opts == '-h':
        host = arg
    if opts == '-t':
        protocol = arg


def createSocket(host, port):
    host = host
    port = port
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print("Failed to create socket")
        exit()
    s.connect((host, port))
   # time = s.recv(1024).decode()
    time = s.recv(1024)
    try:
        print("Time: ",time.decode())
    except UnicodeDecodeError:
        print("Error at decoding server response")


if __name__ == "__main__":
    if protocol == 'tcp':
        print('Protocolo TCP:')
        createSocket(host, port)
