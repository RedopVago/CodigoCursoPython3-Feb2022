
import mysql.connector

def connectMysql(database='python32022'):
    dataBase = mysql.connector.connect(
        host='localhost',
        user='python',
        passwd='python3',
        database=database
    )

    return dataBase


def disconnect(db):
    db.close()


def createDB():
    
    db = mysql.connector.connect(
        host='localhost',
        user='python',
        passwd='python3'
    )

    cursorObject = db.cursor()

    cursorObject.execute('CREATE DATABASE python32022')

    db.close()


def createTable():
    
    db = mysql.connector.connect(
        host='localhost',
        user='python',
        passwd='python3',
        database='python32022'
    )

    cursorObject = db.cursor()

    tablaEstudiante = '''CREATE TABLE ESTUDIANTE (
                      NOMBRE VARCHAR(50),
                      CORREO VARCHAR(50),
                      CONTRA VARCHAR(12)
                      ) 
                      '''
    cursorObject.execute(tablaEstudiante)

    db.close()


def guardarEstudiante(db, nombre, correo, contra):
    cursorObject = db.cursor()

    query = 'INSERT INTO ESTUDIANTE (NOMBRE, CORREO, CONTRA) VALUES (%s, %s, %s)'
    val = (nombre, correo, contra)

    cursorObject.execute(query, val)
    db.commit()

    ...


def leerEstudiante(db, correo):
    cursorObject = db.cursor()

    query = f'SELECT * FROM ESTUDIANTE WHERE CORREO="{correo}"'
    cursorObject.execute(query)

    res = cursorObject.fetchall()

    return res


def actualizarEstudiante(db, correo, nombre=None, correon=None, contra=None):
    cursorObject = db.cursor()

    query = 'UPDATE ESTUDIANTE SET'

    if nombre:
        query += f' NOMBRE="{nombre}"'

    if correon:
        if nombre:
            query += ','

        query += f' CORREO="{correo}"'

    if contra:
        if nombre or correon:
            query += ','

        query += f' CONTRA="{contra}"'

    cursorObject.execute(query)
    db.commit()


def eliminarEstudiante(db, correo):
    cursorObject = db.cursor()

    query = f'DELETE FROM ESTUDIANTE WHERE CORREO="{correo}"'
    cursorObject.execute(query)
    db.commit()


if __name__ == '__main__':

    # createDB()
    # createTable()

    db = connectMysql()


    guardarEstudiante(db, 'Juan', 'juan.valenzuela@cinvestav.mx', '12345')

    estudiante = leerEstudiante(db, 'juan.valenzuela@cinvestav.mx')

    for e in estudiante:
        print(e)

    actualizarEstudiante(db, 'juan.valenzuela@cinvestav.mx', nombre='Pedro')

    estudiante = leerEstudiante(db, 'juan.valenzuela@cinvestav.mx')
    for e in estudiante:
        print(e)
    
    eliminarEstudiante(db, 'juan.valenzuela@cinvestav.mx')

    estudiante = leerEstudiante(db, 'juan.valenzuela@cinvestav.mx')
    for e in estudiante:
        print(e)


    disconnect(db)

    print(f'Script {__name__} finalizado')

    ...
