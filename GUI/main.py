
import sys

from PySide2.QtWidgets import QApplication, QMainWindow

from testqt import Ui_MainWidget

class QtWindow(QMainWindow):

    def __init__(self):
        super(QtWindow, self).__init__()
        self.ui = Ui_MainWidget()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.botonPresionado)

    def botonPresionado(self):
        print('Boton Enviar presionado')

if __name__ == '__main__':

    app = QApplication()
    window = QtWindow()

    window.show()

    sys.exit(app.exec_())
