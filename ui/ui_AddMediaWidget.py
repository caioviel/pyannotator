# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/AddMediaWidget.ui'
#
# Created: Thu Dec  5 17:41:16 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AddMediaWidget(object):
    def setupUi(self, AddMediaWidget):
        AddMediaWidget.setObjectName(_fromUtf8("AddMediaWidget"))
        AddMediaWidget.resize(721, 490)
        self.lst_medias = QtGui.QListWidget(AddMediaWidget)
        self.lst_medias.setGeometry(QtCore.QRect(20, 50, 221, 381))
        self.lst_medias.setObjectName(_fromUtf8("lst_medias"))
        self.preview_widget = QtGui.QWidget(AddMediaWidget)
        self.preview_widget.setGeometry(QtCore.QRect(250, 70, 441, 341))
        self.preview_widget.setObjectName(_fromUtf8("preview_widget"))
        self.btn_delete = QtGui.QPushButton(AddMediaWidget)
        self.btn_delete.setGeometry(QtCore.QRect(140, 440, 101, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/i/comment_delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_delete.setIcon(icon)
        self.btn_delete.setIconSize(QtCore.QSize(40, 40))
        self.btn_delete.setObjectName(_fromUtf8("btn_delete"))
        self.btn_edit = QtGui.QPushButton(AddMediaWidget)
        self.btn_edit.setGeometry(QtCore.QRect(20, 440, 101, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/i/comment_edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_edit.setIcon(icon1)
        self.btn_edit.setIconSize(QtCore.QSize(40, 40))
        self.btn_edit.setObjectName(_fromUtf8("btn_edit"))
        self.btn_audio = QtGui.QPushButton(AddMediaWidget)
        self.btn_audio.setGeometry(QtCore.QRect(30, 6, 41, 41))
        self.btn_audio.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/m/audio.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_audio.setIcon(icon2)
        self.btn_audio.setIconSize(QtCore.QSize(25, 25))
        self.btn_audio.setObjectName(_fromUtf8("btn_audio"))
        self.btn_image = QtGui.QPushButton(AddMediaWidget)
        self.btn_image.setGeometry(QtCore.QRect(70, 6, 41, 41))
        self.btn_image.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/m/image.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_image.setIcon(icon3)
        self.btn_image.setIconSize(QtCore.QSize(25, 25))
        self.btn_image.setObjectName(_fromUtf8("btn_image"))
        self.btn_video = QtGui.QPushButton(AddMediaWidget)
        self.btn_video.setGeometry(QtCore.QRect(110, 6, 41, 41))
        self.btn_video.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/m/video.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_video.setIcon(icon4)
        self.btn_video.setIconSize(QtCore.QSize(25, 25))
        self.btn_video.setObjectName(_fromUtf8("btn_video"))
        self.btn_text = QtGui.QPushButton(AddMediaWidget)
        self.btn_text.setGeometry(QtCore.QRect(150, 6, 41, 41))
        self.btn_text.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/m/plain_text.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_text.setIcon(icon5)
        self.btn_text.setIconSize(QtCore.QSize(25, 25))
        self.btn_text.setObjectName(_fromUtf8("btn_text"))
        self.btn_slides = QtGui.QPushButton(AddMediaWidget)
        self.btn_slides.setGeometry(QtCore.QRect(190, 6, 41, 41))
        self.btn_slides.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/i/slides.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_slides.setIcon(icon6)
        self.btn_slides.setIconSize(QtCore.QSize(25, 25))
        self.btn_slides.setObjectName(_fromUtf8("btn_slides"))

        self.retranslateUi(AddMediaWidget)
        QtCore.QMetaObject.connectSlotsByName(AddMediaWidget)

    def retranslateUi(self, AddMediaWidget):
        AddMediaWidget.setWindowTitle(QtGui.QApplication.translate("AddMediaWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_delete.setText(QtGui.QApplication.translate("AddMediaWidget", "Excluir", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_edit.setText(QtGui.QApplication.translate("AddMediaWidget", "Editar", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
