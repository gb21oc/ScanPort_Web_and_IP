#!/usr/bin/python

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(1)
host = input("[*] Enter The Host To Scan: ")
load = "[*] Loading..."

def portScanner(port):
        if sock.connect_ex((host, port)):
                pass
                #print(f"Port {port} closed")
        else:
                print(f"Port {port} apened")

print(load)
for port in range(1, 1100):

        portScanner(port)

