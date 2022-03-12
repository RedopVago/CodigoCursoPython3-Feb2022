from random import randint


class PiedraPapelTijera:

    def __init__(self):
        self.opciones = ['piedra', 'papel', 'tijera']
        self.usuario = None
        self.pc = None

    def setSeleccionUsuario(self, seleccion):
        self.usuario = seleccion

    def getSeleccionPc(self):
        self.pc = self.opciones[randint(0, 2)]
        return self.pc

    def juego(self):

        msj = None

        if not self.usuario and not self.pc:
            return 'Error en las selecciones'

        if self.usuario != self.pc:
            if self.usuario == 'piedra':
                if self.pc == 'papel':
                    msj = 'Perdiste!'
                else:
                    msj = 'Ganaste!'

            elif self.usuario == 'papel':
                if self.pc == 'tijera':
                    msj = 'Perdiste!'
                else:
                    msj = 'Ganaste!'

            elif self.usuario == 'tijera':
                if self.pc == 'piedra':
                    msj = 'Perdiste!'
                else:
                    msj = 'Ganaste!'
        else:
            msj = 'Empate!'

        return msj
