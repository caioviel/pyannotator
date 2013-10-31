# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WaitingDialog.ui'
#
# Created: Thu Oct 31 20:35:42 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_WaitingDialog(object):
    def setupUi(self, WaitingDialog):
        WaitingDialog.setObjectName("WaitingDialog")
        WaitingDialog.resize(400, 76)
        self.lbl_message = QtGui.QLabel(WaitingDialog)
        self.lbl_message.setGeometry(QtCore.QRect(30, 10, 301, 17))
        self.lbl_message.setObjectName("lbl_message")
        self.pgb_status = QtGui.QProgressBar(WaitingDialog)
        self.pgb_status.setGeometry(QtCore.QRect(30, 40, 331, 23))
        self.pgb_status.setProperty("value", 24)
        self.pgb_status.setObjectName("pgb_status")

        self.retranslateUi(WaitingDialog)
        QtCore.QMetaObject.connectSlotsByName(WaitingDialog)

    def retranslateUi(self, WaitingDialog):
        WaitingDialog.setWindowTitle(QtGui.QApplication.translate("WaitingDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_message.setText(QtGui.QApplication.translate("WaitingDialog", "Copiando arquivos para a pasta do projeto...", None, QtGui.QApplication.UnicodeUTF8))

