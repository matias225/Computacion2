#!/usr/bin/python3

import time
from os import fork, wait, kill, getpid
from signal import pause, signal, SIGUSR1, SIGTERM, getsignal

def funcUSR1(s, frame):
    print("Señal USR1 recibida")
    exit()

def son():
    while True:
        print("Hijo esperando")
        pause()

def main():
    signal(SIGUSR1, funcUSR1)
    pid = fork()
    print(pid)
    if pid:
        print("Soy el hijo "+str(pid))
        son()
        #kill(pid, SIGTERM)
        
if __name__ == '__main__':
    main()
