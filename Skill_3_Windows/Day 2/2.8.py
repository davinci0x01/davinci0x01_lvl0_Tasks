import subprocess

svc = input("Service name: ")
act = input("Action (start/stop/restart): ").lower()

if act == "restart":
    subprocess.run(f"net stop {svc}", shell=True)
    subprocess.run(f"net start {svc}", shell=True)
else:
    subprocess.run(f"net {act} {svc}", shell=True)