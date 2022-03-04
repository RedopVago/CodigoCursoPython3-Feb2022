from mongoengine import connect, Document, StringField


class Estudiante(Document):
    nombre = StringField(required=True)
    correo = StringField(required=True)
    contra = StringField(required= True)


def conetarBaseDeDatos():
    connect('python32022', host='localhost', port=27017)


def guardarEstudiante(nombre, correo, contra):
    e = Estudiante(nombre=nombre, correo=correo, contra=contra)
    e.save()


def leerEstudiante(mail):
    res = Estudiante.objects(correo=mail)
    return res
    

def actualizarEstudiante(e, nombre=None, correo=None, contra=None):
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
        e.save()
        print(f'Estudiante actualizado: {e.id}')
    else:
        print('No se realizaron cambios')


if __name__ == '__main__':

    conetarBaseDeDatos()

    res = leerEstudiante('luis@cinvestav.mx')

    for i, e in enumerate(res):
        print(f'[{i+1}] Nombre: {e.nombre}')
        print(f'[{i+1}] Correo: {e.correo}')
        print()


    # for i, e in enumerate(res):
    #     actualizarEstudiante(e, correo='luis@cinvestav.mx')