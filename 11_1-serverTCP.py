
from socket import socket

s = socket()
host = 'localhost'
port = 9999

s.bind((host, port))

s.listen(5)

while True:
    print('Esperando conexion')
    conn, addr = s.accept()
    print(f'Direccion: {addr}')

    # conn.send(b'Hola cliente!')

    salir = False

    while not salir:

        res = conn.recv(10)

        print(res)

        conn.send(res)

        if res == b'9':
            salir = True


    conn.close()