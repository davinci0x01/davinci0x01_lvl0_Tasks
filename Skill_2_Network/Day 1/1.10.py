ip1 = input("Enter first IP: ").split(".")
ip2 = input("Enter second IP: ").split(".")

if ip1[:3] == ip2[:3]:
    print("They are in the same subnet.")
else:
    print("They are NOT in the same subnet.")
