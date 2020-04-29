#!/usr/bin/python3

import time
from os import fork, wait, kill, getpid
from signal import pause, signal, SIGUSR1, SIGINT, SIGTERM, getsignal

def funcUSR1(s, frame):
    print("Señal USR1 de padre recibida")


def funcINT(s, frame):
    print("El usuario interrumpio el proceso padre. Cerrando...")
    pid = getpid()
    killSon(pid)
    time.sleep(2)
    exit()


def killSon(pid):
    spid = pid+1
    kill(spid, 9)


def son():
    while True:
        print("Hijo esperando...")
        pause()


def main():
    signal(SIGUSR1, funcUSR1)
    signal(SIGINT, funcINT)
    pid = fork()
    if pid == 0:
        print("Iniciado proceso hijo "+str(getpid()))
        son()
    else:
        print("Soy el padre, PID: "+str(getpid())) 
        for a in range(10):
            time.sleep(5)
            kill(pid, SIGUSR1)
        time.sleep(1)
        print("Padre mata al hijo...")
        kill(pid, 15)
        print("Padre terminando...")
        

if __name__ == '__main__':
    main()
