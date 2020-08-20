#!/usr/bin/python3

from multiprocessing import Process, Lock
from getopt import getopt, GetoptError
from sys import argv


def getOptions():
    if len(argv[1:]) == 0:
        print('Por favor ingrese -p seguido de una opcion:\nABRIR\nCERRAR\nAGREGAR\nLEER')
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
        command = arg


if __name__ == "__main__":
    print(command)