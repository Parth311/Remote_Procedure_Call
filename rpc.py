import re
with open("server.py","r") as fi:

    f=open("client_stub.py","w")
    f.write('''import socket
import json

host="127.0.0.1"
port=7004

tosend={}

def setconnection(data):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.connect((host,port))

        s.sendall(data.encode())
        data=s.recv(1024)
        return (data.decode())\n\n''')
    f.close()

    f=open("client_stub.py","a")

    for ln in fi:
        if ln.startswith("def "):
            lst=ln.split()

            f_lst=lst[1]

            x = re.split("[\(\)]", f_lst)
            f_name=x[0]
            
            args_lst=x[1].split(',')
            str_args=str(args_lst).replace("'",'')
            f.write(ln)


            f.write('''    tosend["function_name"]="'''+f_name+'''"
    tosend["no_of_parameters"]='''+str(len(args_lst))+'''
    tosend["parameters_val"]='''+str_args+'''

    data=json.dumps(tosend)
    val=setconnection(data)

    return val\n\n''')
 
