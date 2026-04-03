import subprocess

ip = input("Enter IP address to ping: ")

result = subprocess.run(
    ["ping", "-n", "1", ip],  
    capture_output=True,
    text=True
)

out = (result.stdout)

if "TTL=" in out.upper():
    print(f"{ip} is reachable")
else:
    print(f"{ip} is not reachable")

