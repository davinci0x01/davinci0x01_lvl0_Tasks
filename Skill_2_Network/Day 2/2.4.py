def detect_port_protocol(port):
    common_ports = {
        21: "TCP (FTP)",
        22: "TCP (SSH)",
        23: "TCP (Telnet)",
        25: "TCP (SMTP)",
        53: "TCP & UDP (DNS)",
        67: "UDP (DHCP)",
        68: "UDP (DHCP)",
        80: "TCP (HTTP)",
        110: "TCP (POP3)",
        123: "UDP (NTP)",
        143: "TCP (IMAP)",
        161: "UDP (SNMP)",
        443: "TCP (HTTPS)"
    }

    if port in common_ports:
        return common_ports[port]
    else:
        return "Unknown service or protocol"


port = int(input("Enter port number: "))
print("Protocol:", detect_port_protocol(port))
