# mytoolbox
Tools and stuff

## Port scanner

import socket

def is_port_open(host, port):
    """Check if a port is open on the given host."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout of 1 second
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except socket.error:
        return False

def scan_ports(host, start_port, end_port):
    """Scan a range of ports on a host."""
    print(f"Scanning ports on {host} from {start_port} to {end_port}")
    for port in range(start_port, end_port + 1):
        if is_port_open(host, port):
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")

# Example usage
target_host = "192.168.1.1"  # Replace with the target host IP
start_port = 1
end_port = 100  # Scanning first 100 ports

scan_ports(target_host, start_port, end_port)

