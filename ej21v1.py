#!/usr/bin/python3

from string import ascii_lowercase, digits
from time import sleep
from random import randint, choice
from multiprocessing import Lock, Process, Semaphore


def randomizedPatients(rooms):
    while True:
        patientTime = randint(1, 3)
        sleep(patientTime)
        patid = choice(ascii_lowercase)+choice(ascii_lowercase)+choice(ascii_lowercase)+choice(digits)+choice(digits)+choice(digits)
        p2 = Process(target=activity,args=(patid, rooms))
        p2.start()


def activity(patid, slots):
    attentionTime = randint(5, 7)
    print("Patient id: %s" %patid, "arrives at the hospital. Availiable slots %d" % slots.get_value())
    slots.acquire()
    print("Patient id: %s" %patid, "entering tho consulting room. Availiable slots %d" % slots.get_value())
    sleep(attentionTime)
    slots.release() 
    print("Patient id: %s" %patid, "leaves the hospital. Availiable slots %d" % slots.get_value())


if __name__ == "__main__":
    rooms = Semaphore(5)
    p = Process(target=randomizedPatients,args=(rooms,))
    p.start()
