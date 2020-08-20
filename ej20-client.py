#!/usr/bin/python3

from getopt import getopt, GetoptError
from socket import socket, AF_INET, SOCK_STREAM


def createSocketTCP(port):
    clientSocket = socket(AF_INET, SOCK_STREAM)


if __name__ == "__main__":
    createSocketTCP(port)