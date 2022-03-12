
from socket import socket
from threading import Thread

import time

def trabajo(sock, tid):

    msg = f'[{tid}] Recibido'

    sock.send(msg.encode())
    print(msg)

    salir = False

    while not salir:

        msg = f'[{tid}] Actualizacion'

        sock.send(msg.encode())
        print(msg)
        
        time.sleep(5)

    sock.close()



s = socket()
host = 'localhost'
port = 9999

s.bind((host, port))

s.listen(5)

counter = 0

while True:
    print('Esperando conexion')
    conn, addr = s.accept()

    counter += 1

    print(f'[{counter}] Direccion: {addr}')

    t = Thread(target=trabajo, args=(conn, counter))
    t.start()


    