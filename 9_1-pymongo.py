from pymongo import MongoClient


client = MongoClient()
db = client['python32022']
estudiantes = db.estudiantes


e1 = {
    'name': 'Juan',
    'email': 'juan.valenzuela@cinvestav.mx',
    'passwd': '12345'
}

# result = estudiantes.insert_one(e1)
# print(f'estudiante: {result.inserted_id}')


res = estudiantes.find()

print(type(res))

for e in res:
    print(e.nombre)
    print(e.correo)