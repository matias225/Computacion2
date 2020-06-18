#!/usr/bin/python3

import multiprocessing as mp
import sys


def child(r,w,n):
    print("Hijo ", n)
    while True:
        if n == 1:
            sys.stdin = open(0)
            r.close() 
            msg = input()
            print("Hijo envia: "+msg)
            w.send(msg)
        if n == 2:
            w.close()
            print("Hijo recibe: "+r.recv())
    r.close()
    w.close()


if __name__ == "__main__":
    r, w = mp.Pipe()
    p1 = mp.Process(target=child, args=(r,w,1))
    p2 = mp.Process(target=child, args=(r,w,2))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
