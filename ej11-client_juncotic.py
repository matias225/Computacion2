#!/usr/bin/python3

import socket
from sys import argv, exit

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Failed to create socket")
    exit()

host = argv[1]
port = int(argv[2])

s.connect((host, port))

while(True):
    msg = input("Enter message: ")
    s.send(msg.encode('ascii'))

    msgr = s.recv(1024)

    svresp = msgr.decode('ascii')

    if svresp == '200':
        print("Server reply: OK\n")
    elif svresp == '400':
        print("Server reply: Comando válido, pero fuera de secuencia.\n")
    elif svresp == '405':
        print("Server reply: Cadena nula. Ingrese comando seguido del valor correspondiente.\n")
    elif svresp == '404':
        print("Server reply: Clave erronea. Ingrese la clave correcta.\n")
    elif svresp == '500':
        print("Server reply: Comando inválido. Ingrese un comando válido (hello, email, key, exit).\n")

    if msg == 'exit':
        exit()
        