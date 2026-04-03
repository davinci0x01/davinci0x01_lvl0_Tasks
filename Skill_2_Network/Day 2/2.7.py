import psutil

listening_ports = []

for conn in psutil.net_connections(kind="inet"):
    if conn.status == psutil.CONN_LISTEN and conn.laddr.ip in ("127.0.0.1" ,"0.0.0.0"):
        listening_ports.append(conn.laddr.port)

print("Listening ports on 127.0.0.1 and 0.0.0.0 :")
for port in listening_ports:
    print(port)
