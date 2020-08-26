#!/usr/bin/python3

from multiprocessing import Process as proc, Lock
from getopt import getopt, GetoptError
from sys import argv, path
from socket import socket, AF_INET, SOCK_STREAM


def client(clientSocket, addr, serverSocket, l):
    while True:
        data = clientSocket.recv(1024)
        print("Address: %s " % str(addr))
        msg = data.decode('ascii')
        print("Recibido: "+msg)
        if msg == 'ABRIR':
            resp = 'Ingrese un nombre de archivo...'
            clientSocket.send(resp.encode('ascii'))
            clientResp = clientSocket.recv(1024)
            filename = clientResp.decode('ascii')
            fd = open(filename, 'a')
            fd.flush()
            fileisopen = 1
            msg = 'Desea hacer algo mas con el archivo?'
            clientSocket.send(msg.encode('ascii'))
        if fileisopen == 1:
            if msg == 'CERRAR':
                l.acquire()
                fd.close()
                l.release()
                msg = 'Archivo cerrado'
                clientSocket.send(msg.encode('ascii'))
            if msg == 'AGREGAR':
                print('Recibido agregar')
                resp = 'Ingrese el texto que desea agregar:'
                clientSocket.send(resp.encode('ascii'))
                clientresp = clientSocket.recv(1024)
                l.acquire()
                fd = open(filename, 'a')
                fd.write('\n'+clientresp.decode('ascii'))
                fd.flush()
                l.release()
                msg = 'Desea hacer algo mas con el archivo?'
                clientSocket.send(msg.encode('ascii'))
            '''
            if msg == 'LEER':
                fd = open(filename, 'r')
                # Lista con las lineas leidas
                lines = fd.readlines()    
                fd.close()
                # Junto todas las lineas en un solo mensaje
                readedlines = ''.join(lines)
                clientSocket.send(readedlines.encode('ascii'))
            '''
        else:
            clientSocket.send('Debe abrir un archivo primero...'.encode('ascii'))
        if msg == 'exit':
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
    l = Lock()
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((host, port))
    serverSocket.listen(5)
    print('Server waiting for clients...')
    while True:
        clientSocket, addr = serverSocket.accept()
        p = proc(target=client,args=(clientSocket,addr,serverSocket,l))
        p.start()


if __name__ == "__main__":
    createSocketTCP(port)