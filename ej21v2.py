#!/usr/bin/python3

from sys import argv, exit
from getopt import getopt, GetoptError
from string import ascii_lowercase, digits
from time import sleep
from random import randint, choice
from multiprocessing import Lock, Process, Semaphore


def getOptions():
    if len(argv[1:]) == 0:
        print('Por favor ingrese -r y el numero de consultorios, -z y el tiempo minimo')
        print('-x y el tiempo maximo, -d y el tiempo minimo de atencion y -f y el tiempo maximo de atencion')
        print('Ejemplo de ejecución: python ej21v2.py -r 4 -z 1 -x 4 -d 5 -f 10')
        exit()
    try:
        (opts, arg) = getopt(argv[1:], 'r:z:x:d:f:', [])
        return opts
    except GetoptError as error:
        print('Wrong option: '+str(error))
        exit()

options = getOptions()
for (opts, arg) in options:
    if opts == '-r':
        nrooms = int(arg)
    if opts == '-z':
        tmin = int(arg)
    if opts == '-x':
        tmax = int(arg)
    if opts == '-d':
        dmin = int(arg)
    if opts == '-f':
        dmax = int(arg)


def randomizedPatients(rooms):
    while True:
        patientTime = randint(tmin, tmax)
        sleep(patientTime)
        patid = choice(ascii_lowercase)+choice(ascii_lowercase)+choice(ascii_lowercase)+choice(digits)+choice(digits)+choice(digits)
        p2 = Process(target=activity,args=(patid, rooms))
        p2.start()


def activity(patid, slots):
    attentionTime = randint(dmin, dmax)
    print("Patient id: %s" %patid, "arrives at the hospital. Availiable slots %d" % slots.get_value())
    slots.acquire()
    print("Patient id: %s" %patid, "entering tho consulting room. Availiable slots %d" % slots.get_value())
    sleep(attentionTime)
    slots.release() 
    print("Patient id: %s" %patid, "leaves the hospital. Availiable slots %d" % slots.get_value())


if __name__ == "__main__":
    rooms = Semaphore(nrooms)
    p = Process(target=randomizedPatients,args=(rooms,))
    p.start()
