ports_services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS"
}

user_port = input("Enter a port number: ")

if user_port.isdigit():
    port = int(user_port)

    if port in ports_services:
        print(f"Port {port} uses {ports_services[port]} service.")
    else:
        print("Port not found in the dictionary.")
else:
    print("Please enter a valid port number.")
