# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/DialogCopyFiles.ui'
#
# Created: Thu Dec 12 11:39:06 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogCopyFiles(object):
    def setupUi(self, DialogCopyFiles):
        DialogCopyFiles.setObjectName(_fromUtf8("DialogCopyFiles"))
        DialogCopyFiles.resize(400, 83)
        self.lbl_text = QtGui.QLabel(DialogCopyFiles)
        self.lbl_text.setGeometry(QtCore.QRect(50, 10, 301, 17))
        self.lbl_text.setObjectName(_fromUtf8("lbl_text"))
        self.progressBar = QtGui.QProgressBar(DialogCopyFiles)
        self.progressBar.setGeometry(QtCore.QRect(20, 40, 361, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))

        self.retranslateUi(DialogCopyFiles)
        QtCore.QMetaObject.connectSlotsByName(DialogCopyFiles)

    def retranslateUi(self, DialogCopyFiles):
        DialogCopyFiles.setWindowTitle(QtGui.QApplication.translate("DialogCopyFiles", "Copiando Arquivos", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_text.setText(QtGui.QApplication.translate("DialogCopyFiles", "Copiando arquivos para a pasta do projeto...", None, QtGui.QApplication.UnicodeUTF8))

