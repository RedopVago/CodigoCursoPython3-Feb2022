import sys

a = input('Ingresa un numero: ')

print(type(a))

try:
    a = int(a)
except ValueError:
    print('El parametro no es un entero')
    sys.exit()

print(type(a))

print(a)