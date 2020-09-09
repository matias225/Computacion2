#!/usr/bin/python3

from threading import Thread
from time import sleep
from sys import argv, exit
from socket import socket, AF_INET, SOCK_STREAM
from getopt import getopt, GetoptError


def change(clientSocket, addr):
    print("Conection from address: "+str(addr))
    while True:
        receiveMsg(clientSocket)
        sendMsg(clientSocket)


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
    port = port
    host = ""
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((host, port))
    serverSocket.listen(5)
    print("Alice escuchando...")
    while True:
        clientSocket, addr = serverSocket.accept()
        th = Thread(target=change,args=(clientSocket,addr))
        th.start()


def sendMsg(clientSocket):
    while True:
        msg = input("Alice: ")
        if msg == 'cambio':
            clientSocket.send(msg.encode('ascii')) 
            sleep(1)      
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
            print("Bob:", msg)
            break
        if msg == 'exit':
            exit()
        else:
            print("Bob:", msg)


if __name__ == "__main__":
    th = Thread()
    createSocketTCP(port)
