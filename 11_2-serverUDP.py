
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = 'localhost'
port = 12345

sock.bind((host, port))


while True:
    data, addr = sock.recvfrom(20)
    
    print(data)

    sock.sendto(b'Paquete recibido!', addr)