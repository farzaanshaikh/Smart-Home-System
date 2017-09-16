import socket
from process import command
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "172.19.17.1"
port = 8888
print (host)
print (port)
serversocket.bind((host, port))

serversocket.listen(5)

print ('server started and listening')
while 1:
    (clientsocket, address) = serversocket.accept()
    data = clientsocket.recv(1024).decode()
    command(data)
    r='REceieve'
    clientsocket.send(r.encode())
