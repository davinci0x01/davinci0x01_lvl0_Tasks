import psutil

name = input("Enter process name(notepad.exe): ")

for p in psutil.process_iter(["name"]):
    if p.info["name"] == name:
        p.terminate()
        print("Process terminated")
