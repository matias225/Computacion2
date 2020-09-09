#!/usr/bin/python3

from sys import argv, exit
from getopt import getopt, GetoptError
from socket import socket, AF_INET, SOCK_STREAM
from multiprocessing import Process
from threading import Thread
from hashlib import sha1, sha224, sha256, sha384, sha512, sha3_224, sha3_256, sha3_384, sha3_512


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
    host = ''
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((host, port))
    serverSocket.listen(5)
    print("Server iniciado con multiprocessing, escuchando...")
    while True:
        clientSocket, addr = serverSocket.accept()
        p = Process(target=receiveMsg,args=(clientSocket,addr))
        p.start()


def serverThreading(port):
    host = ''
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((host, port))
    serverSocket.listen(5)
    print("Server iniciado con threading, escuchando...")
    while True:
        clientSocket, addr = serverSocket.accept()
        th = Thread(target=receiveMsg,args=(clientSocket,addr))
        th.start()


def receiveMsg(clientSocket, addr):
    data = clientSocket.recv(1024)
    print("Connection from address: %s " % str(addr))
    msg = data.decode('ascii')
    hash_function, string = msg.split('.',2)
    resp = hash(hash_function, string)
    clientSocket.send(resp.encode('ascii'))
    clientSocket.close()


def hash(hash_function, string):
    if hash_function == 'sha1':     
        return sha1(string.encode()).hexdigest()
    if hash_function == 'sha224':
        return sha224(string.encode()).hexdigest()
    if hash_function == 'sha256':
        return sha256(string.encode()).hexdigest()
    if hash_function == 'sha384':
        return sha384(string.encode()).hexdigest()
    if hash_function == 'sha512':
        return sha512(string.encode()).hexdigest()
    if hash_function == 'sha3_224':
        return sha3_224(string.encode()).hexdigest()
    if hash_function == 'sha3_256':
        return sha3_256(string.encode()).hexdigest()
    if hash_function == 'sha3_384':
        return sha3_384(string.encode()).hexdigest()
    if hash_function == 'sha3_512':
        return sha3_512(string.encode()).hexdigest()
    else:
        return 'Wrong hash function: please use sha1, sha224, sha384, sha512, sha3_224, sha3_256, sha3_384, sha3_512'
        

if __name__ == "__main__":
    if multiprocessing:
        serverMultiprocessing(port)
    if threading:
        serverThreading(port)
    