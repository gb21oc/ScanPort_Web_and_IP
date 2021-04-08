#!/usr/bin/python

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.0.22"
port = 443

def portScanner(port):
        if sock.connect_ex((host, port)):
                print(f"Port {port} closed")
        else:
                print(f"Port {port} opened")


portScanner(port)
