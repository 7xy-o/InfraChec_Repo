import socket

def check_port(ip, port):
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    try:
        result = sock.connect_ex((ip, port))
        sock.close()
        return not result
    except Exception:
        sock.close()
        return False
def scan_local_ports():
    target_ports = [21, 22, 25, 53, 80, 443, 3306, 5432, 8080]
    print("\n[*] Starting Network Port Scan on Localhost (127,0,0,1)...")
    for port in target_ports:
        is_open = check_port("127.0.0.1", port)
        if is_open:
            print(f"\033[91m[+] Port {port} is OPEN\033[0m")
        else:
            pass

if __name__ == "__main__":
    scan_local_ports()
