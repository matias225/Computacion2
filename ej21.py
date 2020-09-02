#!/usr/bin/python3

from multiprocessing import Lock, Process, Semaphore


def func():
    pass


if __name__ == "__main__":
    lock = Semaphore()
    p = Process(target=func,args=(lock))
    p.start()