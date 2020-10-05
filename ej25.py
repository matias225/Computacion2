#!/usr/bin/python3

from sys import argv, exit
from getopt import getopt, GetoptError
from multiprocessing import Process, Pipe, current_process
from threading import Thread, current_thread
from time import sleep


def getOptions():
    if len(argv[1:]) == 0:
        print('Por favor ingrese: -p cantidad de procesos, -m número mínimo y -n número máximo')
        exit()
    try:
        (opts, arg) = getopt(argv[1:], 'p:m:n:', [])
        return opts
    except GetoptError as error:
        print('Wrong option: '+str(error))
        exit()

options = getOptions()
for (opts, arg) in options:
    if opts == '-p':
        process = int(arg)
    if opts == '-m':
        minP = int(arg)
    if opts == '-n':
        maxP = int(arg)


def show(a):
    while True:
        sleep(0.1)
        data = a.recv()
        if data == 404:
            print('Thread '+str(current_process().name)+' exiting...')
            break
        print('Thread '+str(current_process().name)+' got '+str(data)+' from process.')
        a.send('OK '+str(data)+' '+str(current_process().name))


def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] for i in range(wanted_parts) ]


def parallelSquares(b, part):
    print('Process '+str(current_thread().getName())+' archivieng list'+ str(part))
    for i in part:
        b.send(i*i)
        print('Process '+str(current_thread().getName())+'got process message: '+str(b.recv()))
        sleep(1)
    b.send(404)


if __name__ == "__main__":
    rang = list(range(minP, maxP))
    process_list = split_list(rang, process)
    for part in process_list:
        a, b = Pipe()
        p = Process(target=parallelSquares, args=(b, part))
        h = Thread(target=show, args=(a,))
        p.start()
        h.start()
