#!/usr/bin/python

import socket
from time import sleep
from tqdm import tqdm

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("[*] Enter The Host To Scan: ")
port = input("[*] Enter The Port To Scan: ")

def portScanner(host, port):
        if sock.connect_ex((host, int(port))):
                for i in tqdm(range(100)):
                        sleep(0.15)
                print(f"Port {port} closed")
        else:
                for i in tqdm(range(100)):
                        sleep(0.15)
                print(f"Port {port} opened")


portScanner(host, port)
