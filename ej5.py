#!/usr/bin/python

import sys
import getopt
from os import fork, getpid, getppid, _exit

def getArg():
    try:
        (opts, arg) = getopt.getopt(sys.argv[1:], 'n:', [])
        return opts
    except getopt.GetoptError as error:
        print('Wrong Option: '+str(error))
        exit()

def forking(opts):
    for (opt, arg) in opts:
        if opt == '-n':
            try: 
                n = int(arg)
            except ValueError:
                print("Argument is not a number")
                exit(0)
    for a in range(n):
        if not fork():
            print("Soy el proceso "+str(getpid())+", mi padre es "+str(getppid()))
            _exit(0)

forking(getArg())
