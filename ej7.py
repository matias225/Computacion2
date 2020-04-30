#!/usr/bin/python3

from time import sleep
from os import fork, kill, getpid, getppid
from signal import pause, signal, SIGUSR1


def funcUSR1(s, frame):
    pass


def main():
    signal(SIGUSR1, funcUSR1)
    if fork():
        total = 10
        pid = fork()
        if pid:
            print("Padre PID: "+str(getpid()))
            while total:
                pause()
                kill(pid, SIGUSR1)
                total = total - 1
            sleep(2)
            exit()
        else:
            while total:
                pause()
                sleep(0.1)
                print("Soy el hijo2 con PID: "+str(getpid())+": pong\n")
                total = total - 1
            exit()
    else:
        for a in range(10):
            print("Soy el hijo1 con PID: "+str(getpid())+": ping")
            ppid = getppid()
            kill(ppid, SIGUSR1)
            sleep(5)
        exit()


if __name__ == "__main__":
    main()
