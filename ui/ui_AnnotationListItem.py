# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/AnnotationListItem.ui'
#
# Created: Tue Nov 26 15:18:12 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AnnotationListItem(object):
    def setupUi(self, AnnotationListItem):
        AnnotationListItem.setObjectName(_fromUtf8("AnnotationListItem"))
        AnnotationListItem.resize(272, 54)
        self.lbl_content_type = QtGui.QLabel(AnnotationListItem)
        self.lbl_content_type.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.lbl_content_type.setText(_fromUtf8(""))
        self.lbl_content_type.setPixmap(QtGui.QPixmap(_fromUtf8(":/m/audio.png")))
        self.lbl_content_type.setScaledContents(True)
        self.lbl_content_type.setObjectName(_fromUtf8("lbl_content_type"))
        self.lbl_type = QtGui.QLabel(AnnotationListItem)
        self.lbl_type.setGeometry(QtCore.QRect(70, 10, 201, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_type.setFont(font)
        self.lbl_type.setObjectName(_fromUtf8("lbl_type"))
        self.lbl_timestamp = QtGui.QLabel(AnnotationListItem)
        self.lbl_timestamp.setGeometry(QtCore.QRect(70, 30, 66, 17))
        self.lbl_timestamp.setObjectName(_fromUtf8("lbl_timestamp"))

        self.retranslateUi(AnnotationListItem)
        QtCore.QMetaObject.connectSlotsByName(AnnotationListItem)

    def retranslateUi(self, AnnotationListItem):
        AnnotationListItem.setWindowTitle(QtGui.QApplication.translate("AnnotationListItem", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_type.setText(QtGui.QApplication.translate("AnnotationListItem", "Informação SImples", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_timestamp.setText(QtGui.QApplication.translate("AnnotationListItem", "00:48:56", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
