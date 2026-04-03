import ipaddress

ipv6_input = input("Enter an IPv6 address: ")

try:
    ip = ipaddress.IPv6Address(ipv6_input)

    compressed = ip.compressed

    expanded = ip.exploded

    print("Compressed IPv6:", compressed)
    print("Expanded IPv6  :", expanded)

except ValueError:
    print("Invalid IPv6 address")
