from sys import exit


print('Hoy es Febrero', 17)

try:
    print('Test1')
    print('Hoy es Febrero' + 17)
    print('Test2')
except TypeError:
    print('Los paraametros son de diferente tipo')
    exit()

print('FIN')