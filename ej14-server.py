#!/usr/bin/python3

import os
import socket
import sys
import multiprocessing as mp


def child(client):
    socket, addr = client
    while True:
        data = socket.recv(1024)
        print("Address: %s " % str(addr))
        print("Comando recibido: "+data.decode('ascii'))
        if data.decode('ascii') == 'exit':
            clientsocket.send('exit'.encode('ascii'))
            serversocket.close()
            break
        command = data.decode("ascii")+ " > /tmp/out.txt 2> /tmp/error.txt"
        if os.system(command) == 0:
            f = open('/tmp/out.txt','r')
            msg = f.read()
            f.close()
            clientsocket.send('OK\n'.encode('ascii')+msg.encode('ascii'))
        else:
            e = open('/tmp/error.txt','r')
            msgerror = e.read()
            e.close()
            clientsocket.send('ERROR\n'.encode('ascii')+msgerror.encode('ascii'))


if __name__ == "__main__":
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ""
    port = 8000
    serversocket.bind((host, port))
    serversocket.listen(5)
    print('Server waiting for clients...')

    while True:
        client = serversocket.accept()
        clientsocket, addr = client 
        p1 = mp.Process(target=child, args=(client,))
        p1.start()
        