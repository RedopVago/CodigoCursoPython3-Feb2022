
import re

s1 = 'Hola, buenos dias a todos'
s2 = 'Hola, buenas tardes a todos'
s3 = 'Hola, buenas noches a todos'

p1 = 'dias'
p2 = 'noches'

p3 = 'buen[ao]s (.*) a'

ret = re.search(p3, s3)

# if ret:

#     print(f'grupos: {ret.groups()}')

#     momento = ret.group(1)
#     print(f'momento: {momento}')
# else:
#     print(f'No encontro coincidencias de "{p3}"')




# Buscar en archivo


# Correo nombre.apellido1@cinvestav.mx \w
# correo = input('Ingresa tu correo: ')

# patron_correo = '[a-z]{3,15}.[a-z]{3,15}@cinvestav.mx'
# patron_correo = '[a-z]{3,15}.?[a-z]{3,15}@[a-z]{5,15}.[a-z]{2,3}(.[a-z]{2})?'

# ret = re.match(patron_correo, correo)

# if ret:
#     print('El correo es valido')
# else:
#     print('El correo no es valido')

### Clase 5
# Telefono 3345678923 (33) 22222222 (331) 234 33 33
# telefono_in = 'tel: 33 44 55 66 77.'
# patron_telefono = '.*([0-9]{2}(?: [0-9]{2}){4}).*'

# ret = re.search(patron_telefono, telefono_in)

# telefono = ret.group(1)

# print(telefono)

# if ret:
#     print('Telefono valido')
# else:
#     print('Telefono no valido')

# RFC XXXX123456abc
# RFC = 'vasp031156mj8'

# RFC = RFC.upper() 
# patron_rfc = '[A-Z]{4}[\d]{6}[A-Z\d]{3}'  # \d

# ret = re.match(patron_rfc, RFC)

# if ret:
#     print('RFC valido')
# else:
#     print('RFC no valido')

# CURP  XXXX123456 S ES ABC HH
CURP = 'vasp031156mjal3n08'
CURP = CURP.upper()
patron_curp = '[A-Z]{4}[\d]{6}[HM][A-Z]{2}[A-Z]{3}[A-Z\d]{2}'


ret = re.match(patron_curp, CURP)

if ret:
    print('CURP valido')
else:
    print('CURP no valido')

# Validar entradas
def validarEnteros(entero):
    ...
    # validar entero
    if not type(entero) == int:
        return 'ERROR'

    patron = '-?[0-9]{5}'

    ret = re.match(patron, entero)

    if not ret:
        return 'ERROR' 
