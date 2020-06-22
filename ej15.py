#!/usr/bin/python3

import multiprocessing as mp
import sys
import os


def childWritter(w):
    sys.stdin = open(0)
    while True:
        try:
            msg = input()
            w.send(msg)
        except EOFError:
            print("Saliendo...")
            break


def childReader(r):
    while True:
        try:
            msg = r.recv()        
            print("Leyendo(pid:"+str(os.getpid())+"): "+msg)
        except KeyboardInterrupt:
            print("Interrumpido por el usuario")
            break

if __name__ == "__main__":
    r, w = mp.Pipe()
    p1 = mp.Process(target=childWritter, args=(w,))
    p2 = mp.Process(target=childReader, args=(r,))
    p1.start()
    p2.start()
    p1.join()
