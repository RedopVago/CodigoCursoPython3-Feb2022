
import math

class Figura:
    no_lados = 0
    area = 0  # unidades cuadradas
    perimetro = 0  # unidades

    def calcularArea(self):
        ...

    def calcularPerimetro(self):
        ...


class Rectangulo(Figura):

    area = ...
    l1 = 0  # unidades
    l2 = 0  # unidades
    
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2

    def calcularArea(self):

        self.area = self.l1 * self.l2

        return self.area

    def calcularPerimetro(self):
        return 2 * (self.l1 + self.l2)

class Triangulo(Figura):

    area = ...
    l1 = 0  # unidades  --> base
    l2 = 0  # unidades
    l3 = 0  #
    
    def __init__(self, l1, l2):
        '''
        l1 es la base
        l2 es el valor de los otros dos lados
        '''
        self.l1 = l1
        self.l2 = l2
        self.l3 = l2

    def calcularArea(self):

        a = math.sqrt(self.l2**2 + (self.l1/2)**2)

        return self.l1 * a

    def calcularPerimetro(self):
        return self.l1 + self.l2 + self.l3



if __name__ == '__main__':

    rec = Rectangulo(3, 4)
    area = rec.calcularArea()
    print(f'El area del rectangulo es: {area} unidades cuadradas')

    peri = rec.calcularPerimetro()
    print(f'El perimetro del rectangulo es: {peri} unidades')

    ...