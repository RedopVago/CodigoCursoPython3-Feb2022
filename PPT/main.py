
import sys

from ppt import *

from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow

from PySide2.QtGui import QImageReader

from piedraPapelTijera import PiedraPapelTijera as ppt  # backend


class PiedraPapelTijera(QMainWindow):

    def __init__(self):
        super(PiedraPapelTijera, self).__init__()
        self.ui = Ui_ventana()
        self.ui.setupUi(self)

        self.pipati = ppt()

        # conexiones
        self.ui.seleccionCB.activated.connect(self.mostrarImagenUsuario)
        self.ui.jugarB.clicked.connect(self.mostrarImagenPc)

        self.ui.jugarB.setDisabled(True)

    def mostrarImagenUsuario(self):

        self.ui.imagenPc.setVisible(False)

        sel = self.ui.seleccionCB.currentText()

        if sel == 'Piedra':
            reader = QImageReader('piedraU.png')

        elif sel == 'Papel':
            reader = QImageReader('papelU.png')

        elif sel == 'Tijera':
            reader = QImageReader('tijeraU.png')

        else:
            self.ui.imagenUsuario.setVisible(False)
            return

        reader.setAutoTransform(True)
        imagen = reader.read()

        self.ui.imagenUsuario.setPixmap(QPixmap.fromImage(imagen))
        self.ui.imagenUsuario.setVisible(True)

        self.pipati.setSeleccionUsuario(sel.lower())

        self.ui.jugarB.setEnabled(True)  # Activar boton
        self.ui.resultadoL.clear()

    def mostrarImagenPc(self):

        # Obtener seleccion PC
        sel = self.pipati.getSeleccionPc()

        sel = sel.capitalize()

        if sel == 'Piedra':
            reader = QImageReader('piedraP.png')

        elif sel == 'Papel':
            reader = QImageReader('papelP.png')

        elif sel == 'Tijera':
            reader = QImageReader('tijeraP.png')

        imagen = reader.read()

        self.ui.imagenPc.setPixmap(QPixmap.fromImage(imagen))
        self.ui.imagenPc.setVisible(True)

        self.ui.resultadoL.setText(self.pipati.juego())

        self.ui.jugarB.setDisabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    juego_ppt = PiedraPapelTijera()

    juego_ppt.show()

    sys.exit(app.exec_())
