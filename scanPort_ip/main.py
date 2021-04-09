#!/usr/bin/python

import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(1)
host = input("[*] Enter The Host To Scan: ")
load = "[*] Loading..."

def portScanner(port):
        if sock.connect_ex((host, port)):
                print(colored(f"Port {port} closed", 'red'))
        else:
                print(colored(f"Port {port} apened", 'green'))


for port in range(1, 1100):

        portScanner(port)

