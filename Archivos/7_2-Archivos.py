
from fileinput import filename


def escribir():

    filename = 'foo.txt'

    file = open(filename, 'wb')

    file.write(b'Hola!')

    file.close()

    print(file.name)
    print(file.closed)
    print(file.mode)
    print(type(file.mode))


def leer():
    
    filename = 'foo.txt'

    file = open(filename)

    r = file.read()

    print(f'El contenido del archivo {filename} es:\n{r}')

    print(file.name)
    print(file.closed)
    print(file.mode)
    print(type(file.mode))

    file.close()


def leer2():
    with open('foo.txt') as file:
        
        r = file.read()

        print(f'El contenido del archivo {filename} es:\n{r}')

        print(file.name)
        print(file.closed)
        print(file.mode)
        print(type(file.mode))

    print()
    print(file.name)
    print(file.closed)
    print(file.mode)
    print(type(file.mode))

if __name__ == '__main__':

    # escribir()
    # leer()

    leer2()

    ...
