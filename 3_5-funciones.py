
# funcion sin parametros y sin retorno
import re


def saludo():
    print('Hola')

# funcion sin parametros y con retorno
def saludo2():
    return 'Hola'

# funcion con un parametro y con retorno
def saludo3(nombre):
    # return f'Hola {nombre}'

    return 'Hola ' + nombre

def saludo31(nombre, apellido):
    # return f'Hola {nombre}'

    return 'Hola ' + nombre + ' ' + apellido


def saludo4(nombre:str='<Nombre>', apellido:str='<Apellido>') -> str:
    '''
    Funcion que retorna un saludo a nombre apellido
    '''

    if not type(nombre) == str:
        return 'Parametro nombre con tipo incorrecto'

    if not type(apellido) == str:
        return 'Parametro apellido con tipo incorrecto'

    # return f'Hola {nombre} {apellido}'

    ret = f'Hola {nombre} {apellido}'

    if not type(ret) == str:
        return 'Retorno con tipo incorrecto' 

    return ret

def modificarSecuencia(seq):

    print(id(seq))

    if len(seq) > 1:
        seq[1] = 'P'

def modificarEntero(ent):
    ent = 9

    print(ent)
    print(id(ent))

if __name__ == '__main__':

    # x = saludo()
    # print(type(x))

    # x = saludo2()
    # print(x)
    # print(type(x))

    # x = saludo3(5)
    # print(x)

    # var = ('Juan', 'Godoy')
    # var = ()

    # x = saludo31(*var)
    # print(x)
    
    # x = saludo4()
    # print(x)
    
    # x = saludo4('Juan')
    # print(x)
    
    # x = saludo4('Juan', 'Godoy')
    # print(x)

    # x = saludo4(apellido='Godoy')
    # print(x)
    
    # x = saludo4(apellido='Godoy', nombre='Juan')
    # print(x)

    # *var separa una tupla
    # var = ('Juan', 'Godoy')
    # x = saludo4(*var)
    # print(x)


    # **var separa un diccionario
    # var2 = {'apellido':'Godoy', 'nombre':'Juan'}
    # x = saludo4(**var2)
    # print(x)


    # t = (1, 2, 3)
    # l = [1, 2, 3]

    # modificarSecuencia(t)
    # print(t)

    # modificarSecuencia(l)
    # print(id(l))

    # x = 5
    # modificarEntero(x)

    # print(id(x))