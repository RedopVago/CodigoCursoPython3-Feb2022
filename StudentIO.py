
import shelve

from estudiante import Estudiante

'''
Se trabajara con un archivo de nombre students
'''

def guardarEstudiante(e:Estudiante):

    e = leerEstudiante(e.correo)

    if type(e) == Estudiante:
        print('ERROR: Ya existe un estudiante con ese correo')
        return

    with shelve.open('students') as s:
        s[e.correo] = e

        print(f'Objeto estudiante guardado')
    
    
def leerEstudiante(correo):
    with shelve.open('students') as s:
        try:
            return s[correo]
        except KeyError:
            return 'No existe objeto con esa llave'


def actualizarEstudiante(e:Estudiante, nombre=None, correo=None, contra=None):
    
    if type(e) != Estudiante:
        print('El objeto no es dle tipo estudiante')
        return

    e = leerEstudiante(e.correo)

    if type(e) != Estudiante:
        print('ERROR: No existe un estudiante con ese correo')
        return
    
    
    cambio = False

    if nombre:
        e.nombre = nombre
        cambio = True

    if correo:
        e.correo = correo
        cambio = True

    if contra:
        e.contra = contra
        cambio = True

    if cambio:
        
        with shelve.open('students') as s:
            s[e.correo] = e

            print('Estudiante actualizado')
            return s[e.correo]

    else:
        print('No se cambio el estudiante')



if __name__ == '__main__':
    # est = Estudiante('Pedro', 'juan.valenzuela@cinvestav.mx', '123456')
    # est = Estudiante('Juan', 'juan.valenzuela@cinvestav.mx', '654321')
    # guardarEstudiante(est)

    e1 = ...
    e2 = leerEstudiante('juan.valenzuela@cinvestav.m')
    print(e2)
    e3 = ...
    e4 = ...
    e5 = ...

    act = actualizarEstudiante(e2, contra=1234567)
    print(act)