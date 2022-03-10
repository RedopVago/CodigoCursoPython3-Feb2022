# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testqt.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        if not MainWidget.objectName():
            MainWidget.setObjectName(u"MainWidget")
        MainWidget.resize(400, 124)
        self.pushButton = QPushButton(MainWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(9, 92, 381, 23))
        self.widget = QWidget(MainWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(9, 9, 381, 74))
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.nombre_LE = QLineEdit(self.widget)
        self.nombre_LE.setObjectName(u"nombre_LE")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nombre_LE)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.correo_LE = QLineEdit(self.widget)
        self.correo_LE.setObjectName(u"correo_LE")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.correo_LE)

        self.contre_LE = QLineEdit(self.widget)
        self.contre_LE.setObjectName(u"contre_LE")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.contre_LE)


        self.retranslateUi(MainWidget)

        QMetaObject.connectSlotsByName(MainWidget)
    # setupUi

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QCoreApplication.translate("MainWidget", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("MainWidget", u"Enviar", None))
        self.label.setText(QCoreApplication.translate("MainWidget", u"Nombre", None))
        self.label_2.setText(QCoreApplication.translate("MainWidget", u"Correo", None))
        self.label_3.setText(QCoreApplication.translate("MainWidget", u"Contrase\u00f1a", None))
    # retranslateUi

