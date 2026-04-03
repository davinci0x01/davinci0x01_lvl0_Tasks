import psutil

for s in psutil.win_service_iter():
    info = s.as_dict()
    print(info["name"], "-", info["status"], "-", info["start_type"])