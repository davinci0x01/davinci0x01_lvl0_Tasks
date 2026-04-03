import psutil

user = input("Enter username: ")
proc = input("Enter process name (notepad.exe): ")

for p in psutil.process_iter(["username", "name"]):
    try:
        if p.info["username"] and user.lower() in p.info["username"].lower() and p.info["name"] == proc:
            p.terminate()
            print("Terminated:", p.info["name"])
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass