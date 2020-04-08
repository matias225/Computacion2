#!/usr/bin/python

import sys
import getopt
import os.path as path

def getOptions():
    (opts, arg) = getopt.getopt(sys.argv[1:], "i:o:", [])
    return opts

def copyPython(names):
    opt = names
    for (opt, arg) in opt:
        if opt == '-i':
            if path.exists(arg):
                origin = arg
            else:
                return print("Origin file doesn't exists")        
        if opt == '-o':
            destination = arg
            if path.exists(destination):
                print("Destination file already exists, its content will be replaced")
            else:
                destinationFile = open(destination, "x")
   
    readFile = open(origin, "r")
    copyLines = readFile.readlines()
    readFile.close()
    destinationFile = open(destination, "w")  
    destinationFile.writelines(copyLines)
    destinationFile.close()

copyPython(getOptions())
