import socket
import sys

def is_port_open(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

def scan_ports(host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        if is_port_open(host, port):
            open_ports.append(port)
    return open_ports

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python PortScanner.py host start_port end_port")
        sys.exit(1)
    host = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])
    open_ports = scan_ports(host, start_port, end_port)

    if open_ports:
        print("Open ports:", open_ports)
    else:
        print("No open ports found.")
