#!/usr/bin/python3

import multiprocessing as mp

def child():
    pass

if __name__ == "__main__":
    p = mp.Process(target=child)
    p.start()
    p.join()

