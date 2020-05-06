#!/usr/bin/python3

from os import mkfifo, path
from sys import argv

def getString():
    string = argv[1:]
    msg = ' '.join(string)
    return msg


def main():
    msg = getString()
    fPath = '/tmp/fifo'
    if not path.exists(fPath):
        mkfifo(fPath)
    f = open(fPath, 'w')
    f.write(msg)
    f.close()
    

if __name__ == "__main__":
    main()
