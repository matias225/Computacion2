#!/usr/bin/python3

import sys
import time
from getopt import getopt, GetoptError
from os import fork, getpid, getppid, kill
from signal import signal, SIGUSR2, SIGKILL, pause


def funcUSR2(s, frame):
    print("Soy el PID "+str(getpid())+", recibí la señal "+str(s)+" de mi padre PID "+str(getppid())+"\n")
    exit()


def getArg():
    try:
        (opts, arg) = getopt(sys.argv[1:], 'p:', ["process="])
        return opts
    except GetoptError as error:
        print('Wrong Option: '+str(error)+'.')
        exit()


def son():
    print("Hijo esperando...")
    pause()


def getProcess(opts):
    for (opt, arg) in opts:
        if opt == '-p' or opt == "--process":
            if arg.isdigit():
                process = int(arg)
                return process
            else:
                print('Wrong Argument: "'+str(arg)+'" is not a digit.')
                exit()


def forking(numProcess):
    signal(SIGUSR2, funcUSR2)
    for a in range(numProcess):
        pid = fork()
        if pid:
            print("Padre PID: "+str(getpid())+". \nCreando proceso hijo: "+str(pid))
            time.sleep(1)
            kill(pid, SIGUSR2)
            time.sleep(2)
        else:
            son()


def main():
    numProcess = getProcess(getArg())
    if numProcess:
        forking(numProcess)
    else:
        print('Please use -p or --process with an argument...')
        exit()


if __name__ == "__main__":
    main()
