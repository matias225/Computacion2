#!/usr/bin/python3

from sys import argv, exit
from getopt import getopt, GetoptError
from socket import socket, AF_INET, SOCK_STREAM
from multiprocessing import Process
from threading import Thread


threading = False
multiprocessing = False


def getOptions():
    if len(argv[1:]) == 0:
        print('Por favor ingrese: -p seguido del puerto, -t si quiere usar threading o -m si quiere usar multiprocessing')
        exit()
    try:
        (opts, arg) = getopt(argv[1:], 'p:tm', [])
        return opts
    except GetoptError as error:
        print('Wrong option: '+str(error))
        exit()

options = getOptions()
for (opts, arg) in options:
    if opts == '-p':
        port = int(arg)
    if opts == '-t':
        threading = True
    if opts == '-m':
        multiprocessing = True


def serverMultiprocessing(port):
    port = port
    host = ''
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((host, port))
    serverSocket.listen(5)
    print("Server escuchando...")
    while True:
        clientSocket, addr = serverSocket.accept()
        p = Process(target=hash,args=(clientSocket,addr))
        p.start()


def serverThreading(port):
    port = port
    host = ''
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((host, port))
    serverSocket.listen(5)
    print("Server escuchando...")
    while True:
        clientSocket, addr = serverSocket.accept()
        th = Thread(target=hash,args=(clientSocket,addr))
        th.start()


def hash():    
    #calcular hash en python


if __name__ == "__main__":
    #createSocketTCP(port)
    print(port, threading, multiprocessing)
    if multiprocessing:
        serverMultiprocessing()
    if threading:
        serverThreading()
    