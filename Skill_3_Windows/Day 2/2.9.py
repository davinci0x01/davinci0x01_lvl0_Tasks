import psutil, time, os

while True:
    time.sleep(5)
    os.system("cls")
    procs = []
    for p in psutil.process_iter(["name"]):
        try:
            procs.append((p.info["name"], p.cpu_percent(0.1) / psutil.cpu_count()))
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    for name, cpu in sorted(procs, key=lambda x: x[1], reverse=True)[:5]:
        print(name, "-", round(cpu, 2), "%")
