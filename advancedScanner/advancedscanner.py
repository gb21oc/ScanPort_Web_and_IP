#!/usr/bin/python

from socket import *
from threading import *

x = 0


def connScan(tgtHost, tgtPort):
    global sock
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        print(f"[*] {tgtPort}/tcp Open")
    except:
        print(f"[-] {tgtPort}/tcp Close")
    finally:
        sock.close()


def portScan(tgtHost, tgtPorts, tgtForIn):
    global x, tgtIp
    if tgtForIn:
        try:
            tgtIp = gethostbyname(tgtHost)
        except:
            print(f"[-] Unknows Host {tgtHost}")
        try:
            tgtName = gethostbyaddr(tgtIp)
            print(f"[*] Scan Results For: {tgtName[0]}")
        except:
            print(f"[*] Scan Results For: {tgtIp}")
        setdefaulttimeout(1)
        for tgtPort in tgtPorts:
            t = Thread(target=connScan(tgtHost, int(tgtPort)))
            t.start()
    else:
        x += 1
        try:
            tgtIp = gethostbyname(tgtHost)
        except:
            print(f"[-] Unknows Host {tgtHost}")
        try:
            tgtName = gethostbyaddr(tgtIp)
            if x <= 1:
                print(f"[*] Scan Results For: {tgtName[0]}")
        except:
            if x <= 1:
                print(f"[-] Scan Results For: {tgtIp}")
        setdefaulttimeout(1)
        t = Thread(target=connScan(tgtHost, int(tgtPorts)))
        t.start()


def main():
    question = input(
        "Do you want to choose the port manually or do you want it automatically?[manually/auto]: ").upper()
    if question == "MANUALLY":
        tgtHost = input("[*] Enter The Host: ")
        tgtPorts = input("[*] Enter The Port: ")
        tgtPorts = str(tgtPorts).split(",")
        tgtForIn = True
        if (tgtHost is None) or (tgtPorts is None):
            print("Host and port cannot be empty")
            exit(0)
        portScan(tgtHost, tgtPorts, tgtForIn)
    else:
        tgtHost = input("[*] Enter The Host: ")
        tgtForIn = False
        for i in range(10000):
            portScan(tgtHost, str(i), tgtForIn)


if __name__ == '__main__':
    main()
