#!/usr/bin/python3

from threading import Thread, Lock
from time import sleep
from sys import argv, exit
from getopt import getopt, GetoptError
from os import path
from string import ascii_letters


def function(lock, ite, abecedario, n):
    fd = open(filename, 'a')
    letra = abecedario[n]
    lock.acquire()
    for i in range(ite):
        fd.write(letra)
        fd.flush()
        sleep(1)
    lock.release()
    fd.close()


def getOptions():
    if len(argv[1:]) == 0:
        print('No ha ingresado argumentos: por favor ingrese 3 argumentos (-f, -r y -n)')
        exit()
    if len(argv[1:]) == 6:
        try:
            (opts, arg) = getopt(argv[1:], 'n:r:f:', [])
            return opts
        except GetoptError as error:
            print('Wrong option: '+str(error))
            exit()
    else:
        print('Argumentos insuficientes: por favor ingrese 3 argumentos (-f, -r y -n)')
        exit()


options = getOptions()
for (opts, arg) in options:
    if opts == '-n':
        num = int(arg)
    if opts == '-r':
        ite = int(arg)
    if opts == '-f':
        filename = arg


if __name__ == "__main__":
    abecedario = ascii_letters
    if num > 52:
        print('Numero de procesos muy alto, ingrese n menor a 52')
        exit()
    n = 0
    if path.isfile(filename):
        fd = open(filename, 'w')
    lock = Lock()
    for i in range(num):
        Thread(target=function, args=(lock, ite, abecedario, n)).start()
        if n >= 52:
            n = 0
        else: 
            n += 1
    