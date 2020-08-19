#!/usr/bin/python3

import multiprocessing as mp
import time
import sys
import getopt
import os


def function(lock, ite, abecedario, n):
    fd = open(filename, 'a')
    letra = abecedario[n]
    lock.acquire()
    for i in range(ite):
        fd.write(letra)
        fd.flush()
        time.sleep(1)
    lock.release()
    fd.close()


def getOptions():
    try:
        (opts, arg) = getopt.getopt(sys.argv[1:], 'n:r:f:', [])
        return opts
    except getopt.GetoptError as error:
        print('Wrong argument: '+str(error))
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
    abecedario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    n = 0
    if os.path.isfile(filename):
        fd = open(filename, 'w')
    lock = mp.Lock()
    for i in range(num):
        mp.Process(target=function, args=(lock, ite, abecedario, n)).start()
        if n >= 52:
            n = 0
        else: 
            n += 1
    