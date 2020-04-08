#!/usr/bin/python

import sys
import getopt

def getOptions():
    (opts, arg) = getopt.getopt(sys.argv[1:],'m:n:o:', [])
    return opts

def calculator(opts):
    opt = opts
    for (opt, arg) in opt:
        if opt == '-m':
            if arg.isnumeric() or arg[0] == '-' and arg[1:].isnumeric():
                num1 = int(arg)
            else:
                return print("Argument "+arg+" is not a number")
        if opt == '-n':
            if arg.isnumeric() or arg[0] == '-' and arg[1:].isnumeric():
                num2 = int(arg)
            else:
                return print("Argument "+arg+" is not a number")
        if opt == '-o':
            operator = arg

    if operator == 'x':
        res = num1 * num2
        print (str(num1)+" x "+str(num2)+" = "+str(res))            
    elif operator == '+':
        res = num1 + num2
        print (str(num1)+" + "+str(num2)+" = "+str(res))
    elif operator == '-':
        res = num1 - num2
        print (str(num1)+" - "+str(num2)+" = "+str(res))
    elif operator == '/':
        if num2 == 0:
            print ("Division by zero not allowed")
        else:
            res = num1 / num2
            print (str(num1)+" / "+str(num2)+" = "+str(res))
    else: 
        print ("Invalid operator")

calculator(getOptions())
