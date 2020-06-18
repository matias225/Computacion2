#!/usr/bin/python3


import multiprocessing as mp
from os import getpid


def child(i):
    print("Proceso "+i+", PID: "+os.getpid())


if __name__ == "__main__":
    p1 = mp.Process(target=child, args=1)
    #p2 = mp.Process(target=child, args=2)
    #p3 = mp.Process(target=child, args=3)
    #p4 = mp.Process(target=child, args=4)
    #p5 = mp.Process(target=child, args=5)
    #p6 = mp.Process(target=child, args=6)
    #p7 = mp.Process(target=child, args=7)
    #p8 = mp.Process(target=child, args=8)
    #p9 = mp.Process(target=child, args=9)
    #p10 = mp.Process(target=child, args=10)
    
    p1.start()
    p1.join()

    #p2.start()
    #p2.join()
    
    p3.start()
    p3.join()

    p4.start()
    p4.join()

    p5.start()
    p5.join()

    p6.start()
    p6.join()

    p7.start()
    p7.join()

    p8.start()
    p8.join()

    p9.start()
    p9.join()

    p10.start()
    p10.join()
