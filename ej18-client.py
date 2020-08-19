#!/usr/bin/python3

import socket
import getopt
import sys

def getOptions():
    try:
        (opts, arg) = getopt.getopt(sys.argv[1:], 'p:h:t:', [])
        return opts
    except getopt.GetoptError as error:
        print('Wrong argument: '+str(error))
        exit()

options = getOptions()
for (opts, arg) in options:
    if opts == '-p':
        port = int(arg)
    if opts == '-h':
        host = arg
    if opts == '-t':
        protocol = arg


if __name__ == "__main__":
    print(port, host, protocol)