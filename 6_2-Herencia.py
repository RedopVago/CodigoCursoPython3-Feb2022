
class Vehiculo:
    _numero_llantas = 0
    _pasajeros = 0

    def acelera(self):
        ...

    def frena(self):
        ...

    def enciendeLuces(self):
        ...

    def cuantasLlantas(self):
        ...


class Motocicleta(Vehiculo):
    
    def __init__(self):
        self._numero_llantas = 2


class Camioneta(Vehiculo):
    __espacio = 0

    def __init__(self):
        self._numero_llantas = 4
        self.__espacio = '90cm3'

    def mostrarEspacio(self):
        print(self.__espacio)


if __name__ == '__main__':

    v = Vehiculo()

    m = Motocicleta()

    c = Camioneta()

    ...