from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        
        if TCP in packet:
            tcp_layer = packet[TCP]
            print(f"[TCP] {src_ip}:{tcp_layer.sport} → {dst_ip}:{tcp_layer.dport}   Flags: {tcp_layer.flags}")
        elif UDP in packet:
            udp_layer = packet[UDP]
            print(f"[UDP] {src_ip}:{udp_layer.sport} → {dst_ip}:{udp_layer.dport}")

print("Simple TCP/UDP Sniffer Started")
print("Press Ctrl+C to stop")
print("-" * 60)

sniff(prn=packet_callback, store=False)