import os
import socket

s = socket.socket()
port = 8080
host = input(str("please enter the server adresse : "))
s.connect((host,port))
print("")
print("connected to the server successfuly")
print("")

#connection 

#rec command 

while 1:
    command = s.recv(1024)
    command = command.decode()
    print("command rec")
    print("")
    if command == "view_cwd":
        files = os.getcwd()
        files = str(files)
        s.send("".encode())
        s.send(files.encode())
        print("command has been executed successfuly")
    elif command == "costum_dirr":
        user_input = s.recv(5000)
        user_input = user_input.decode()
        files = os.listdir(user_input)
        files = str(files)
        s.send(files.encode())
        print("")
        print("command successfuly")
        print("")
    elif command == "dwnd_file":
        fpath = s.recv(5000)
        fpath = fpath.decode()
        file = open(fpath,"rb")
        data = file.read()
        s.send(data)
        print("file has been sent successfuly")
        print("")
    
    elif command == "rmv_file":
        fd = s.recv(6000)
        fd = fd.decode()
        os.remove(fd)
        print("")
        print("command has been executed successfuly")
        print("")
    
    elif command == "send_file":
        fs = s.recv(6000)
        nf = open(fs,"wb")
        data = s.recv(6000)
        #size will be change when size file is big 
        nf.write(data)
        nf.close()
    else:
        print("")
        print("command not req")