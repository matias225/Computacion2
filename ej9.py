#!/usr/bin/python

from time import sleep
from os import fork, getpid, getppid, pipe, fdopen, wait, kill, close
from signal import signal, SIGUSR1, SIGUSR2, pause


def funcUSR1(s, frame):
    pass


def funcUSR2(s, frame):
    pass


def main():
    signal(SIGUSR1, funcUSR1)
    signal(SIGUSR2, funcUSR2)
    r, w = pipe()
    pAid = getpid()
    pBid = fork()   
    if pBid:
        # Proceso A
        close(w)
        print("Proceso A: "+str(getpid()))
        pause()
        # Enviar señal USR1 al Proceso B
        kill(pBid, SIGUSR1)
        # Cuando reciba la USR2, leer el contenido del pipe y mostrar por pantalla
        pause()
        r = fdopen(r)
        print("Contenido del pipe: \n")
        for line in r:
            print(line)
        r.close()
        exit()
    else:
        # Proceso B
        close(r)
        sleep(1)
        pCid = fork()    
        if not pCid:
            # Proceso C
            pause()
            w = fdopen(w, 'w')
            print("Proceso C: "+str(getpid())+", mi padre es: "+str(getppid())+"\n")
            # Escribir en el pipe el mensaje "Mensaje 2 (PID=CCCC)\n".
            msg = "Mensaje 2 (PID = "+str(getpid())+")\n"
            w.write(msg)
            w.close()
            # Enviar al Proceso A, la USR2
            sleep(1)
            kill(pAid, SIGUSR2)
        else:
            # Proceso B
            w = fdopen(w, 'w')
            pBid = str(getpid())
            print("Proceso B: "+pBid+", mi padre es: "+str(getppid()))
            # Escribir en pipe "Mensaje 1 (PID=BBBB)\n"
            msg = "Mensaje 1 (PID = "+pBid+")\n"
            w.write(msg)
            # Enviar USR2 al Proceso A
            kill(pAid, SIGUSR2)
            sleep(1)    
            # Enviar USR1 al Proceso C
            kill(pCid, SIGUSR1)


if __name__ == "__main__":
    main()
