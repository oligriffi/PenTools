import socket

def is_port_open(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

def scan_ports(host):
    open_ports = []
    for port in range(1, 65535):
        if is_port_open(host, port):
            open_ports.append(port)
    return open_ports

host = input("Enter the host to scan: ")
open_ports = scan_ports(host)

if open_ports:
    print("Open ports:", open_ports)
else:
    print("No open ports found.")

