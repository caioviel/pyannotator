# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AnnotationListItem.ui'
#
# Created: Mon Feb  4 00:03:27 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AnnotationListItem(object):
    def setupUi(self, AnnotationListItem):
        AnnotationListItem.setObjectName("AnnotationListItem")
        AnnotationListItem.resize(272, 54)
        self.lbl_content_type = QtGui.QLabel(AnnotationListItem)
        self.lbl_content_type.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.lbl_content_type.setText("")
        self.lbl_content_type.setPixmap(QtGui.QPixmap(":/m/audio.png"))
        self.lbl_content_type.setScaledContents(True)
        self.lbl_content_type.setObjectName("lbl_content_type")
        self.lbl_type = QtGui.QLabel(AnnotationListItem)
        self.lbl_type.setGeometry(QtCore.QRect(70, 10, 201, 17))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.lbl_type.setFont(font)
        self.lbl_type.setObjectName("lbl_type")
        self.lbl_timestamp = QtGui.QLabel(AnnotationListItem)
        self.lbl_timestamp.setGeometry(QtCore.QRect(70, 30, 66, 17))
        self.lbl_timestamp.setObjectName("lbl_timestamp")

        self.retranslateUi(AnnotationListItem)
        QtCore.QMetaObject.connectSlotsByName(AnnotationListItem)

    def retranslateUi(self, AnnotationListItem):
        AnnotationListItem.setWindowTitle(QtGui.QApplication.translate("AnnotationListItem", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_type.setText(QtGui.QApplication.translate("AnnotationListItem", "Informação SImples", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_timestamp.setText(QtGui.QApplication.translate("AnnotationListItem", "00:48:56", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
