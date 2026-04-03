import psutil

procs = [(p.info["name"],p.cpu_percent(interval=0.1) / psutil.cpu_count())
         for p in psutil.process_iter(["name"])]

for name, cpu in sorted(procs, key=lambda x: x[1], reverse=True)[:5]:
    print(name, "-", cpu, "%")
