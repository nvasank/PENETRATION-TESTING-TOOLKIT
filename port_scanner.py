import socket

def scan_ports(target, ports):
    print(f"Scanning {target}...")
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} is open")
            s.close()
        except KeyboardInterrupt:
            print("Scan interrupted.")
            break
        except socket.error:
            print("Could not connect to server.")
            break