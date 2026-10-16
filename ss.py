import socket

def check_port(host, port, timeout=5):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((host, port))  
    sock.close()
    status = "OPEN" if result == 0 else "CLOSED/FILTERED"
    print(f"[{'+' if result==0 else '-'}] Port {port}: {status}")

host = "192.168.68.65"
for port in [21, 22, 23, 3398, 3306, 5900, 25, 80, 443, 9929, 31337]:
    check_port(host, port)