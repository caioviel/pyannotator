# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ImageContent.ui'
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

class Ui_ImageContent(object):
    def setupUi(self, ImageContent):
        ImageContent.setObjectName(_fromUtf8("ImageContent"))
        ImageContent.resize(743, 573)
        self.txt_duration = QtGui.QPlainTextEdit(ImageContent)
        self.txt_duration.setEnabled(True)
        self.txt_duration.setGeometry(QtCore.QRect(620, 10, 104, 31))
        self.txt_duration.setObjectName(_fromUtf8("txt_duration"))
        self.btn_cancel = QtGui.QPushButton(ImageContent)
        self.btn_cancel.setGeometry(QtCore.QRect(630, 520, 101, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/i/no.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cancel.setIcon(icon)
        self.btn_cancel.setIconSize(QtCore.QSize(25, 25))
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.time_end = QtGui.QTimeEdit(ImageContent)
        self.time_end.setGeometry(QtCore.QRect(360, 10, 91, 31))
        self.time_end.setObjectName(_fromUtf8("time_end"))
        self.lbl_duration = QtGui.QLabel(ImageContent)
        self.lbl_duration.setGeometry(QtCore.QRect(480, 16, 141, 21))
        self.lbl_duration.setObjectName(_fromUtf8("lbl_duration"))
        self.btn_ok = QtGui.QPushButton(ImageContent)
        self.btn_ok.setGeometry(QtCore.QRect(520, 520, 101, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/i/check.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_ok.setIcon(icon1)
        self.btn_ok.setIconSize(QtCore.QSize(25, 25))
        self.btn_ok.setObjectName(_fromUtf8("btn_ok"))
        self.lbl_end_time = QtGui.QLabel(ImageContent)
        self.lbl_end_time.setGeometry(QtCore.QRect(230, 16, 131, 21))
        self.lbl_end_time.setObjectName(_fromUtf8("lbl_end_time"))
        self.lbl_begin_time = QtGui.QLabel(ImageContent)
        self.lbl_begin_time.setGeometry(QtCore.QRect(10, 16, 111, 21))
        self.lbl_begin_time.setObjectName(_fromUtf8("lbl_begin_time"))
        self.time_begin = QtGui.QTimeEdit(ImageContent)
        self.time_begin.setGeometry(QtCore.QRect(120, 10, 91, 31))
        self.time_begin.setObjectName(_fromUtf8("time_begin"))
        self.txt_media_name = QtGui.QPlainTextEdit(ImageContent)
        self.txt_media_name.setGeometry(QtCore.QRect(10, 50, 541, 41))
        self.txt_media_name.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.txt_media_name.setObjectName(_fromUtf8("txt_media_name"))
        self.btn_choose_image = QtGui.QPushButton(ImageContent)
        self.btn_choose_image.setGeometry(QtCore.QRect(560, 50, 161, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/i/folder_open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_choose_image.setIcon(icon2)
        self.btn_choose_image.setIconSize(QtCore.QSize(40, 40))
        self.btn_choose_image.setObjectName(_fromUtf8("btn_choose_image"))
        self.layout_selector_widget = QtGui.QWidget(ImageContent)
        self.layout_selector_widget.setGeometry(QtCore.QRect(10, 100, 721, 411))
        self.layout_selector_widget.setObjectName(_fromUtf8("layout_selector_widget"))

        self.retranslateUi(ImageContent)
        QtCore.QMetaObject.connectSlotsByName(ImageContent)

    def retranslateUi(self, ImageContent):
        ImageContent.setWindowTitle(QtGui.QApplication.translate("ImageContent", "Conteúdo em Imagem", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancel.setText(QtGui.QApplication.translate("ImageContent", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_duration.setText(QtGui.QApplication.translate("ImageContent", "Duração (segundos):", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_ok.setText(QtGui.QApplication.translate("ImageContent", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_end_time.setText(QtGui.QApplication.translate("ImageContent", "Tempo de Término:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_begin_time.setText(QtGui.QApplication.translate("ImageContent", "Tempo de Início:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_choose_image.setText(QtGui.QApplication.translate("ImageContent", "Escolher Imagem", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
