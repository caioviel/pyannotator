# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/MainProjectWidget.ui'
#
# Created: Fri Nov 29 06:38:46 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainProjectWidget(object):
    def setupUi(self, MainProjectWidget):
        MainProjectWidget.setObjectName(_fromUtf8("MainProjectWidget"))
        MainProjectWidget.resize(999, 664)
        self.btn_choose_video = QtGui.QPushButton(MainProjectWidget)
        self.btn_choose_video.setGeometry(QtCore.QRect(520, 10, 161, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/i/folder_open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_choose_video.setIcon(icon)
        self.btn_choose_video.setIconSize(QtCore.QSize(40, 40))
        self.btn_choose_video.setObjectName(_fromUtf8("btn_choose_video"))
        self.txt_main_video = QtGui.QPlainTextEdit(MainProjectWidget)
        self.txt_main_video.setGeometry(QtCore.QRect(10, 10, 501, 41))
        self.txt_main_video.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.txt_main_video.setObjectName(_fromUtf8("txt_main_video"))
        self.time_edit = QtGui.QTimeEdit(MainProjectWidget)
        self.time_edit.setGeometry(QtCore.QRect(10, 620, 118, 27))
        self.time_edit.setObjectName(_fromUtf8("time_edit"))
        self.btn_add_annotation = QtGui.QPushButton(MainProjectWidget)
        self.btn_add_annotation.setGeometry(QtCore.QRect(130, 610, 191, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/i/comment_add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add_annotation.setIcon(icon1)
        self.btn_add_annotation.setIconSize(QtCore.QSize(40, 40))
        self.btn_add_annotation.setObjectName(_fromUtf8("btn_add_annotation"))
        self.frame_notes = QtGui.QFrame(MainProjectWidget)
        self.frame_notes.setGeometry(QtCore.QRect(690, 10, 301, 641))
        self.frame_notes.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_notes.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_notes.setObjectName(_fromUtf8("frame_notes"))
        self.label = QtGui.QLabel(self.frame_notes)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.list_notes = QtGui.QListWidget(self.frame_notes)
        self.list_notes.setGeometry(QtCore.QRect(10, 30, 281, 551))
        self.list_notes.setObjectName(_fromUtf8("list_notes"))
        self.btn_edit = QtGui.QPushButton(self.frame_notes)
        self.btn_edit.setGeometry(QtCore.QRect(10, 590, 131, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/i/comment_edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_edit.setIcon(icon2)
        self.btn_edit.setIconSize(QtCore.QSize(40, 40))
        self.btn_edit.setObjectName(_fromUtf8("btn_edit"))
        self.btn_delete = QtGui.QPushButton(self.frame_notes)
        self.btn_delete.setGeometry(QtCore.QRect(160, 590, 131, 41))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/i/comment_delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_delete.setIcon(icon3)
        self.btn_delete.setIconSize(QtCore.QSize(40, 40))
        self.btn_delete.setObjectName(_fromUtf8("btn_delete"))
        self.btn_generate_ncl = QtGui.QPushButton(MainProjectWidget)
        self.btn_generate_ncl.setEnabled(False)
        self.btn_generate_ncl.setGeometry(QtCore.QRect(530, 610, 151, 41))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/i/notepad.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_generate_ncl.setIcon(icon4)
        self.btn_generate_ncl.setIconSize(QtCore.QSize(40, 40))
        self.btn_generate_ncl.setObjectName(_fromUtf8("btn_generate_ncl"))
        self.btn_save_project = QtGui.QPushButton(MainProjectWidget)
        self.btn_save_project.setGeometry(QtCore.QRect(380, 610, 151, 41))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/i/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save_project.setIcon(icon5)
        self.btn_save_project.setIconSize(QtCore.QSize(40, 40))
        self.btn_save_project.setObjectName(_fromUtf8("btn_save_project"))
        self.txt_description = QtGui.QTextEdit(MainProjectWidget)
        self.txt_description.setGeometry(QtCore.QRect(10, 490, 671, 101))
        self.txt_description.setObjectName(_fromUtf8("txt_description"))
        self.player_widget = QtGui.QWidget(MainProjectWidget)
        self.player_widget.setGeometry(QtCore.QRect(0, 40, 691, 481))
        self.player_widget.setObjectName(_fromUtf8("player_widget"))

        self.retranslateUi(MainProjectWidget)
        QtCore.QMetaObject.connectSlotsByName(MainProjectWidget)

    def retranslateUi(self, MainProjectWidget):
        MainProjectWidget.setWindowTitle(QtGui.QApplication.translate("MainProjectWidget", "Projeto", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_choose_video.setText(QtGui.QApplication.translate("MainProjectWidget", "Escolha o Vídeo", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_add_annotation.setText(QtGui.QApplication.translate("MainProjectWidget", "Adicionar Anotação", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainProjectWidget", "Anotações:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_edit.setText(QtGui.QApplication.translate("MainProjectWidget", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_delete.setText(QtGui.QApplication.translate("MainProjectWidget", "Excluir", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_generate_ncl.setText(QtGui.QApplication.translate("MainProjectWidget", "Gerar...", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_save_project.setText(QtGui.QApplication.translate("MainProjectWidget", "Salvar Projeto", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
