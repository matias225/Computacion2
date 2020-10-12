#!/usr/bin/python3

from sys import argv, exit
from getopt import getopt, GetoptError
from multiprocessing import Pool
from time import sleep
from os import getpid


def getOptions():
    if len(argv[1:]) == 0:
        print('Por favor ingrese: -p cantidad de procesos, -m número mínimo y -n número máximo')
        exit()
    try:
        (opts, arg) = getopt(argv[1:], 'p:m:n:', [])
        return opts
    except GetoptError as error:
        print('Wrong option: '+str(error))
        exit()


def getArgs():
    options = getOptions()
    for (opts, arg) in options:
        if opts == '-p':
            process = int(arg)
        if opts == '-m':
            minP = int(arg)
        if opts == '-n':
            maxP = int(arg)
    return process, minP, maxP


def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] for i in range(wanted_parts) ]


def parallelSquares(part):
    print('Pool worker with pid ', getpid())
    return part**2


def main():
    process, minP, maxP = getArgs()
    pool = Pool()
    rang = list(range(minP, maxP))
    process_list = split_list(rang, process)

    print('Results with map:')
    for part in process_list:
        mapping = (pool.map(parallelSquares, part))
        print('Resultados: ', mapping)

    print('\nResults with apply:')
    for part in process_list:
        applying = [pool.apply(parallelSquares, args=(i,)) for i in part]
        print('Resultados: ', applying)


if __name__ == "__main__":
    main()
