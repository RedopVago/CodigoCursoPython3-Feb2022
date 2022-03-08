
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

# res = s.recv(1024)
# print(res)

l = [str(n) for n in range(10)]

for i in l:
    s.send(i.encode())

    res = s.recv(10)

    print(res)

s.close()




