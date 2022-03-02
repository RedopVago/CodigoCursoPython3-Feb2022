
from mimetypes import init


class MiClase:

    _attr1 = None
    __attr2 = None

    def __init__(self, attr1='', attr2=''):
        '''
        attr1 debe ser de tipo str
        attr2 debe ser de tipo str
        '''
        # self._attr1 = attr1
        # self.__attr2 = attr2
        ...

    def __mostrarString(self, string, string2):
        print(string)
        print(string2)


    def assignarAttr(self, attr1, attr2):
        self._attr1 = attr1
        self.__attr2 = attr2
        ...


    def mostrarString2(self):
        try:
            if self._attr1:
                print(f'attr1: {self._attr1}')

            if self.__attr2:    
                print(f'attr2: {self.__attr2}')
            else:
                print('No hay parametros')
        except AttributeError:
            print('No existen los atributos en el objeto')
        ...

# False, 0, '', [], {}, None

if __name__ == '__main__':

    miClase = MiClase()
    # miClase.mostrarString('Hola', 'Adios')

    miCLase2 = MiClase()
    miCLase2.mostrarString2()
    miCLase2.assignarAttr('Uno', 'Dos')
    miCLase2.mostrarString2()

    miCLase2._MiClase__attr2 = 'Asigado!'
    miCLase2.mostrarString2()

    ...