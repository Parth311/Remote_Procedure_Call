import socket
import json
import server

host="127.0.0.1"
port=7004

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind((host,port))
    while True:
        s.listen()
        conn,addr=s.accept()
        with conn:
            print('Connected to ',addr)
            data=conn.recv(1024)

            data=data.decode()
            temp=json.loads(data)

            func_name=temp["function_name"]
            args=temp["parameters_val"]

            val=getattr(server,"%s"%func_name)(*args)

            conn.sendall(str(val).encode())