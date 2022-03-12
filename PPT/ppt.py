# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ppt.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ventana(object):
    def setupUi(self, ventana):
        if not ventana.objectName():
            ventana.setObjectName(u"ventana")
        ventana.resize(911, 457)
        self.jugarB = QPushButton(ventana)
        self.jugarB.setObjectName(u"jugarB")
        self.jugarB.setGeometry(QRect(380, 380, 161, 61))
        font = QFont()
        font.setPointSize(30)
        self.jugarB.setFont(font)
        self.seleccionCB = QComboBox(ventana)
        self.seleccionCB.addItem("")
        self.seleccionCB.addItem("")
        self.seleccionCB.addItem("")
        self.seleccionCB.addItem("")
        self.seleccionCB.setObjectName(u"seleccionCB")
        self.seleccionCB.setGeometry(QRect(40, 320, 301, 41))
        font1 = QFont()
        font1.setPointSize(20)
        self.seleccionCB.setFont(font1)
        self.resultadoL = QLabel(ventana)
        self.resultadoL.setObjectName(u"resultadoL")
        self.resultadoL.setGeometry(QRect(370, 320, 181, 41))
        self.resultadoL.setFont(font)
        self.resultadoL.setAlignment(Qt.AlignCenter)
        self.groupBox = QGroupBox(ventana)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(40, 10, 380, 291))
        self.groupBox.setFont(font1)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.imagenUsuario = QLabel(self.groupBox)
        self.imagenUsuario.setObjectName(u"imagenUsuario")
        self.imagenUsuario.setMinimumSize(QSize(360, 240))
        self.imagenUsuario.setMaximumSize(QSize(360, 240))

        self.horizontalLayout.addWidget(self.imagenUsuario)

        self.groupBox_2 = QGroupBox(ventana)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(490, 10, 380, 291))
        self.groupBox_2.setFont(font1)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.imagenPc = QLabel(self.groupBox_2)
        self.imagenPc.setObjectName(u"imagenPc")
        self.imagenPc.setMinimumSize(QSize(360, 240))
        self.imagenPc.setMaximumSize(QSize(360, 240))
        self.imagenPc.setFont(font1)

        self.horizontalLayout_2.addWidget(self.imagenPc)


        self.retranslateUi(ventana)

        QMetaObject.connectSlotsByName(ventana)
    # setupUi

    def retranslateUi(self, ventana):
        ventana.setWindowTitle(QCoreApplication.translate("ventana", u"Piedra, Papel o Tijera", None))
        self.jugarB.setText(QCoreApplication.translate("ventana", u"Jugar", None))
        self.seleccionCB.setItemText(0, QCoreApplication.translate("ventana", u"Seleccione un opcion", None))
        self.seleccionCB.setItemText(1, QCoreApplication.translate("ventana", u"Piedra", None))
        self.seleccionCB.setItemText(2, QCoreApplication.translate("ventana", u"Papel", None))
        self.seleccionCB.setItemText(3, QCoreApplication.translate("ventana", u"Tijera", None))

        self.resultadoL.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("ventana", u"Usuario", None))
        self.imagenUsuario.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("ventana", u"PC", None))
        self.imagenPc.setText("")
    # retranslateUi

