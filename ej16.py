#!/usr/bin/python3


import multiprocessing as mp
from os import getpid
from time import sleep


def child(j, queue):
    pid = str(getpid())
    print("Proceso "+str(j)+", PID: "+pid)
    sleep(j)
    queue.put(pid+"\t")


if __name__ == "__main__":
    q = mp.Queue()
    ls = []
    for i in range(10):
        j = i + 1
        p = mp.Process(target=child, args=(j, q))
        ls.append(p)
        ls[i].start()
        ls[i].join()
    while not q.empty():
        print(q.get())
