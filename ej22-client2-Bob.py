#!/usr/bin/python3

from time import sleep
from sys import argv, exit
from socket import socket, AF_INET, SOCK_STREAM
from getopt import getopt, GetoptError


def change(clientSocket):
    while True:
        sendMsg(clientSocket)
        receiveMsg(clientSocket)


def getOptions():
    if len(argv[1:]) == 0:
        print('Por favor ingrese -p seguido seguido del puerto')
        exit()
    try:
        (opts, arg) = getopt(argv[1:], 'p:', [])
        return opts
    except GetoptError as error:
        print('Wrong option: '+str(error))
        exit()

options = getOptions()
for (opts, arg) in options:
    if opts == '-p':
        port = int(arg)


def createSocketTCP(port):
    host = ""
    port = port
    try:
        clientSocket = socket(AF_INET, SOCK_STREAM)
    except error:
        print("Failed to create socket")
        exit()
    clientSocket.connect((host, port))
    change(clientSocket)


def sendMsg(clientSocket):
    while True:
        msg = input("Bob: ")
        if msg == 'cambio':
            clientSocket.send(msg.encode('ascii'))   
            sleep(2)
            break     
        if msg == 'exit':
            clientSocket.send(msg.encode('ascii'))        
            clientSocket.close()
            exit()
        else:
            clientSocket.send(msg.encode('ascii'))


def receiveMsg(clientSocket):
    while True:
        data = clientSocket.recv(1024)
        msg = data.decode('ascii')
        if msg == 'cambio':
            clientSocket.send(msg.encode('ascii'))    
            print("Alice:", msg)
            break
        if msg == 'exit':
            clientSocket.close()
            exit()
        else:           
            print("Alice:", msg)



if __name__ == "__main__":
    createSocketTCP(port)