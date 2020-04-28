#!/usr/bin/python3

import getopt
import sys

def getArg():
    try:
        (opts, arg) = getopt.getopt(sys.argv[1:], 'p:', ["process="])
        return opts
    except getopt.GetoptError as error:
        print('Wrong Option: '+str(error)+'.')
        exit()

def getProcess(opts):
    for (opt, arg) in opts:
        if opt == '-p' or opt == "--process":
            if arg.isdigit():
                process = arg
                print(process)
            else:
                print('Wrong Argument: "'+str(arg)+'" is not a digit.')

getProcess(getArg())
