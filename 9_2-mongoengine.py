
from mongoengine import connect, Document, StringField

connect('python32022', host='localhost', port=27017)

class Estudiante(Document):
    nombre = StringField(required=True)
    correo = StringField(required=True)
    contra = StringField(required= True)


e = Estudiante(nombre= 'Luis', correo='luis@civestav.mx', contra='1234')
e.save()


for e in Estudiante.objects():
    print(e.nombre)
    print(e.correo)