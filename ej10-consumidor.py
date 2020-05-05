#!/usr/bin/python3

from os import fork, pipe, close, fdopen
from time import sleep

def main():
    r, w = pipe()
    if fork():
        # Padre
        close(r)
        w = fdopen(w, 'w')
        w.write('hola')
        w.close()
        sleep(1)
    else:
        # Hijo
        close(w)    
        r = fdopen(r)
        msg = r.readline()
        print(msg)
        exit()


if __name__ == "__main__":
    main()
