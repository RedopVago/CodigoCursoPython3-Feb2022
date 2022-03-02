
from Modulos import resta, mi_suma


if  __name__ == '__main__':
    
    a = 3
    b = 2

    mi_suma(a, b)

    a = 5
    b = 1
    ret = resta(a, b)

    print(f'la resta de {a} menos {b} es {ret}')