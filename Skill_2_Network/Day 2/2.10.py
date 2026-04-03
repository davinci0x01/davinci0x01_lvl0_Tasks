# Reserved ports (1–1023) commonly targeted in security testing
reserved_ports = {
    21:  "FTP",
    22:  "SSH",
    23:  "Telnet",
    25:  "SMTP",
    53:  "DNS",
    69:  "TFTP",
    80:  "HTTP",
    110: "POP3",
    111: "RPC",
    123: "NTP",
    137: "NetBIOS",
    138: "NetBIOS",
    139: "NetBIOS",
    143: "IMAP",
    161: "SNMP",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    512: "Rexec",
    513: "Rlogin",
    514: "Rsh",
    636: "LDAPS",
    873: "rsync",
    993: "IMAPS",
    995: "POP3S"
}

print("Reserved ports commonly targeted:\n")
for port, service in sorted(reserved_ports.items()):
    print(f"Port {port} -> {service}")
