#!/usr/bin/python3

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
    if fork():
        close(w)
        r = fdopen(r)
        # Proceso A
        print("A: "+str(getpid()))
        # Cuando reciba la USR2, leer el contenido del pipe y mostrar por pantalla
        pause()
        sleep(2)
        print("Contenido del pipe: \n")
        string = r.readline()
        print(string)
        r.close()
        exit()
    else:
        close(r)
        w = fdopen(w, 'w')
        # Proceso B
        pBid = str(getpid())
        print("B: "+pBid+", mi padre es: "+str(getppid()))
        
        # Escribir en pipe "Mensaje 1 (PID=BBBB)\n"
        msg = "Mensaje 1 (PID="+pBid+")\n"
        print(msg)
        w.write(msg)
        w.close()
        # Enviar USR1 al Proceso C
        #kill()
        
        if not fork():
            #w = fdopen(w, 'w')
            # Proceso C
            pCid = str(getpid())
            print("C: "+str(getpid())+", mi padre es: "+str(getppid()))
            # Escribir en el pipe el mensaje "Mensaje 2 (PID=CCCC)\n".
            #msg = "Mensaje 2 (PID="+pCid+")\n"
            #print(msg)
            #w.write(msg)
            # Enviar al Proceso A, la USR2
            print(pAid)
            kill(pAid, SIGUSR2)
            #w.close()

if __name__ == "__main__":
    main()
