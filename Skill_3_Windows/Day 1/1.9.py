from cpuinfo import get_cpu_info

print("CPU:", get_cpu_info()["brand_raw"])
print("Cores:", get_cpu_info()["count"])
