import socket
import random

def build_dns_query(domain):
    # DNS Header
    transaction_id = random.randint(0, 65535).to_bytes(2, 'big')
    flags = b'\x01\x00'
    questions = b'\x00\x01'
    answer_rrs = b'\x00\x00'
    authority_rrs = b'\x00\x00'
    additional_rrs = b'\x00\x00'

    header = transaction_id + flags + questions + answer_rrs + authority_rrs + additional_rrs

    # DNS Question
    qname = b''
    for part in domain.split('.'):
        qname += bytes([len(part)]) + part.encode()
    qname += b'\x00'

    qtype = b'\x00\x01'
    qclass = b'\x00\x01'

    question = qname + qtype + qclass

    return header + question


def send_dns_query(domain):
    server = ("8.8.8.8", 53)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(3)

    query = build_dns_query(domain)
    sock.sendto(query, server)

    try:
        response, _ = sock.recvfrom(512)
        print(f"Received {len(response)} bytes from DNS server.")
    except socket.timeout:
        print("No response received.")

    sock.close()


domain = "example.com"
send_dns_query(domain)
