
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s_host = 'localhost'
s_port = 12345

msg = b'Paquete UDP'


sock.sendto(msg, (s_host, s_port))

data, addr = sock.recvfrom(20)

print(data)