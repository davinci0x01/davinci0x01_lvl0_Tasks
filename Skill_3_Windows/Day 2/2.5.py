import psutil

found = any(p.info["name"] == "explorer.exe"
            for p in psutil.process_iter(["name"]))

print("Running" if found else "Not Running")
