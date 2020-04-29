#!/usr/bin/python3

import sys
import time
from getopt import getopt, GetoptError
from os import fork, getpid, getppid, kill
from signal import signal, SIGUSR2, SIGKILL, pause


def funcUSR2(s, frame):
    print("Soy el PID "+str(getpid())+", recibí la señal "+str(s)+" de mi padre PID "+str(getppid()))


def getArg():
    try:
        (opts, arg) = getopt(sys.argv[1:], 'p:', ["process="])
        return opts
    except GetoptError as error:
        print('Wrong Option: '+str(error)+'.')
        exit()


def son():
    while True:
        print("Hijo esperando...")
        pause()


def getProcess(opts):
    for (opt, arg) in opts:
        if opt == '-p' or opt == "--process":
            if arg.isdigit():
                process = arg
                return process
            else:
                print('Wrong Argument: "'+str(arg)+'" is not a digit.')
                exit()


def forking(numProcess):
    signal(SIGUSR2, funcUSR2)
    pid = fork()
    if pid:
        print("Padre PID: "+str(getpid()))
        print("Creando proceso: "+str(pid))
        time.sleep(3)
        kill(pid, SIGUSR2)
        time.sleep(3)
        print("Padre matando hijo "+str(pid))
        kill(pid, SIGKILL)
    else:
        son()

#numProcess = getProcess(getArg())
#forking(numProcess)


def main():
    forking(1)


if __name__ == "__main__":
    main()
