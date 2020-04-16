#!/usr/bin/python

from os import fork, getpid, wait

def main():
    ret = fork()
    if(ret != 0):
        pid = getpid()
        for a in range(2):
            print("Soy el padre, PID "+str(pid)+", mi hijo es "+str(ret))
        wait()
        print("Mi proceso hijo, PID "+str(ret)+" termino")
    else:
        childpid = getpid()
        for a in range(5):
            print("Soy el hijo, PID "+str(childpid))
        print("PID "+str(childpid)+" terminando")

main()
