class Estudiante:
    nombre = ''
    correo = ''
    contra = ''

    def __init__(self, nombre, correo, contra):
        self.nombre = nombre
        self.correo = correo
        self.contra = contra

    def obtenerNombre(self):
        return self.nombre
    
    def obtenerCorreo(self):
        return self.correo

    def obtenerContra(self):
        return self.contra

    def __str__(self) -> str:
        return f'Nombre: {self.nombre}\nCorreo: {self.correo}\nContra: {self.contra}'


if __name__ == '__main__':

    e = Estudiante('Pedro', 'juan.valenzuela@cinvestav.mx', '1234')

    print(f'Nombre: {e.obtenerNombre()}')
    print(f'Correo: {e.obtenerCorreo()}')
    print(f'Contra: {e.obtenerContra()}')