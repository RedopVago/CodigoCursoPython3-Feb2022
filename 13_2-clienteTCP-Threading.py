
import socket
import sys

s = socket.socket()

server_host = 'localhost'
server_port = 9999

try:
    s.connect((server_host, server_port))
except ConnectionRefusedError:
    print('El servidor no esta activo')
    print('Saliendo ...')
    sys.exit()

while True:
    res = s.recv(20)

    print(res)

s.close()




