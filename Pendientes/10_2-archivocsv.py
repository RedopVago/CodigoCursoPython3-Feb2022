# enconding=latin-1

import re 
from estudiante import Estudiante

file = 'Pendientes/test.csv'


with open(file) as f:

    encabezados = f.readline()
    print(encabezados)

    for line in f:
        # print(line, end='')
        # items = line.replace('\n', '').split(',')
        # print(items)

        # nombre = items[0] + ' ' + items[1]
        # correo = items[2]
        # contra = items[3]


        # print(f'Nombre: {nombre}')
        # print(f'Correo: {correo}')
        # print(f'Contraseña: {contra}')
        # print()

        # [a-z]+.?[a-z]*@[a-z]+.[a-z]{3}(?:.(a-z)[2]?)

        patron = '([A-Z][a-z]{2,20}),([A-Z][a-z]{2,20}),(.+@.+),([A-Za-z0-9-_]*)'

        res = re.match(patron, line)

        if res:
            nombre = res.group(1) + ' ' + res.group(2)
            correo = res.group(3)
            contra = res.group(4)

            print(f'Nombre: {nombre}')
            print(f'Correo: {correo}')
            print(f'Contraseña: {contra}')
            print()

            e = Estudiante(nombre, correo, contra)
