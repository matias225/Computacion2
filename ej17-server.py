#!/usr/bin/python3

from multiprocessing import Process as p
import socket
import getopt
import sys

def child(clientsocket, addr, serversocket):
    while True:
        data = clientsocket.recv(1024)
        print("Address: %s " % str(addr))
        msg = data.decode("ascii")
        print("Recibido: "+msg)
        resp = msg[::-1]
        clientsocket.send(resp.encode('ascii'))
        if data.decode('ascii') == 'exit':
            serversocket.close()
            break


def getOptions():
    try:
        (opts, arg) = getopt.getopt(sys.argv[1:], 'p:', [])
        return opts
    except getopt.GetoptError as error:
        print('Wrong Option: '+str(error))
        exit()


options = getOptions()
for (opts, arg) in options:
    if opts == '-p':
        port = int(arg)


def createSocket(port):
    port = port
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    host = ""
    serversocket.bind((host, port))
    serversocket.listen(5)
    print('Server waiting for clients...')
    while True:
        clientsocket, addr = serversocket.accept()
        print(str(addr))
        process = p(target=child, args=(clientsocket,addr,serversocket))
        process.start()

createSocket(port)
