#!/usr/bin/python

import sys
import getopt
import subprocess as sp
import datetime

def getOptions():
    try:
        (opts, arg) = getopt.getopt(sys.argv[1:], 'c:f:l:', [])
        return opts
    except getopt.GetoptError as error:
        print('Wrong Option: '+str(error))
        exit()

def executor(options):
    options = getOptions()
    for (opts, arg) in options:
        if opts == '-c':
            command = arg
        if opts == '-f':
            output_file = open(arg, "a")
        if opts == '-l':
            log_file = open(arg, "a")

    process = sp.Popen([command], stdout = output_file, stderr = sp.PIPE, shell = True, universal_newlines=True)
    err = process.communicate()[1]

    if err:
        log_file.write(str(datetime.datetime.now())+" "+str(err)+"\n")
    else:
        log_file.write(str(datetime.datetime.now())+ ". Comando "+command+" ejecutado correctamente\n")
        output_file.write("\n")

    log_file.close()
    output_file.close()

executor(getOptions)
