# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WaitingDialog.ui'
#
# Created: Thu Oct 31 20:28:09 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 76)
        self.lbl_message = QtGui.QLabel(Dialog)
        self.lbl_message.setGeometry(QtCore.QRect(30, 10, 301, 17))
        self.lbl_message.setObjectName("lbl_message")
        self.pgb_status = QtGui.QProgressBar(Dialog)
        self.pgb_status.setGeometry(QtCore.QRect(30, 40, 331, 23))
        self.pgb_status.setProperty("value", 24)
        self.pgb_status.setObjectName("pgb_status")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_message.setText(QtGui.QApplication.translate("Dialog", "Copiando arquivos para a pasta do projeto...", None, QtGui.QApplication.UnicodeUTF8))

