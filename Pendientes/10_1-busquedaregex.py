
import re

def replace():
    with open('Pendientes/PYTHON.txt', 'r') as f, open('Pendientes/Pendientes-SUB.txt', 'w') as s:

        patron = '<<PYTHON>>'

        for line in f:
            res = re.sub(patron, 'Python', line)

            s.write(res)


def readFile(filename, pat='<<PYTHON>>'):
    with open(filename, 'r') as f:

        patron = pat

        index = 0

        for line in f:
            res = re.search(patron, line)

            if res:
                index += 1
                print(f'[{index}] {line}')

        if index == 0:
            print('No se encontraron coincidencias')


if __name__ == '__main__':
    filename1 = 'Pendientes/PYTHON.txt'

    filename2 = 'Pendientes-SUB.txt'


    readFile(filename2, 'Python')