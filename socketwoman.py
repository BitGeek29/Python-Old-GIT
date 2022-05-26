import socket

host = input("Enter Host :--> ")
port = int(input("Enter Port :--> "))
s = socket.socket()
s.connect((host,port))
while True:
    str = input("enter message: \n")
    s.send(str.encode());
    if(str == "Bye" or str == "bye"):
        break
    print("N:",s.recv(1024).decode())
s.close()

