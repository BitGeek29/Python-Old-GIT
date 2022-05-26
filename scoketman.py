import socket
from threading import *

def cmde(cmd):
  from subprocess import run as rn
  return rn(cmd, capture_output=True, shell=True).stdout

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 8000
print("Local access at: '%s' ,Other access at: '%s'; " % (host,cmde('hostname --all-ip-addresses').decode('utf-8')))
print(port)
serversocket.bind((host, port))

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            print('Client sent:', self.sock.recv(1024).decode())
            self.sock.send(b'Oi you sent something to me')

serversocket.listen(5)
print('server started and listening')
while 1:
    clientsocket, address = serversocket.accept()
    client(clientsocket, address)
