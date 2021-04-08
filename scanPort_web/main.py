import socket

def portScan():
    website = input("Enter website: ")
    ports = [21, 23, 25, 53, 63, 70, 79, 80, 110, 119, 443, 2121, 3306, 8080]

    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #connection tcp/ip
        client.settimeout(0.5)      #runtime
        scan = client.connect_ex((website, port))
        print(f"Port: {port}, Scan: {scan}")

portScan()
