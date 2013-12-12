# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/WaitingDialog.ui'
#
# Created: Thu Dec 12 11:39:07 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_WaitingDialog(object):
    def setupUi(self, WaitingDialog):
        WaitingDialog.setObjectName(_fromUtf8("WaitingDialog"))
        WaitingDialog.resize(400, 76)
        self.lbl_message = QtGui.QLabel(WaitingDialog)
        self.lbl_message.setGeometry(QtCore.QRect(30, 10, 301, 17))
        self.lbl_message.setObjectName(_fromUtf8("lbl_message"))
        self.pgb_status = QtGui.QProgressBar(WaitingDialog)
        self.pgb_status.setGeometry(QtCore.QRect(30, 40, 331, 23))
        self.pgb_status.setProperty("value", 24)
        self.pgb_status.setObjectName(_fromUtf8("pgb_status"))

        self.retranslateUi(WaitingDialog)
        QtCore.QMetaObject.connectSlotsByName(WaitingDialog)

    def retranslateUi(self, WaitingDialog):
        WaitingDialog.setWindowTitle(QtGui.QApplication.translate("WaitingDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_message.setText(QtGui.QApplication.translate("WaitingDialog", "Copiando arquivos para a pasta do projeto...", None, QtGui.QApplication.UnicodeUTF8))

