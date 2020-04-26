#!/usr/bin/python3

import time
from os import fork
from signal import signal, SIGUSR1, getsignal

def funcUSR1(s, frame):
    pass

def main():
    signal(SIGUSR1, funcUSR1)
    if fork():
        print("Soy el hijo")
        
if __name__ == '__main__':
    main()
