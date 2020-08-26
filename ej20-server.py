#!/usr/bin/python3

from multiprocessing import Process as proc, Lock as l
from getopt import getopt, GetoptError
from sys import argv
from socket import socket, AF_INET, SOCK_STREAM


def client(clientSocket, addr, serverSocket):
    while True:
        data = clientSocket.recv(1024)
        print("Address: %s " % str(addr))
        msg = data.decode('ascii')
        print("Recibido: "+msg)
        if msg == 'ABRIR':
            resp = 'Ingrese un nombre de archivo...'
            clientSocket.send(resp.encode('ascii'))
            clientresp = clientSocket.recv(1024)
            filename = clientresp.decode('ascii')
            fd = open(filename, 'r')
            text = fd.readlines()
            print(filename)
            for i in text:
                print(i)
            #msg = 'Que desea hacer con el archivo?'
            #clientSocket.send(msg.encode('ascii'))
        if msg == 'CERRAR':
            print('Recibido cerrar')
        if msg == 'AGREGAR':
            print('Recibido agregar')
        if msg == 'LEER':
            print('Recibido leer')
        if data.decode('ascii') == 'exit':
            serverSocket.close()
            break


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
    print('Server waiting for clients...')
    while True:
        clientSocket, addr = serverSocket.accept()
        p = proc(target=client,args=(clientSocket,addr,serverSocket))
        p.start()


if __name__ == "__main__":
    createSocketTCP(port)
    print('ABRIR\nCERRAR\nAGREGAR\nLEER')
