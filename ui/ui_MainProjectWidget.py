# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainProjectWidget.ui'
#
# Created: Sun Feb  3 12:30:30 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainProjectWidget(object):
    def setupUi(self, MainProjectWidget):
        MainProjectWidget.setObjectName("MainProjectWidget")
        MainProjectWidget.resize(997, 537)
        self.btn_choose_video = QtGui.QPushButton(MainProjectWidget)
        self.btn_choose_video.setGeometry(QtCore.QRect(520, 10, 161, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/i/folder_open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_choose_video.setIcon(icon)
        self.btn_choose_video.setIconSize(QtCore.QSize(40, 40))
        self.btn_choose_video.setObjectName("btn_choose_video")
        self.txt_main_video = QtGui.QPlainTextEdit(MainProjectWidget)
        self.txt_main_video.setGeometry(QtCore.QRect(10, 10, 501, 41))
        self.txt_main_video.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.txt_main_video.setObjectName("txt_main_video")
        self.seek_slider = phonon.Phonon.SeekSlider(MainProjectWidget)
        self.seek_slider.setGeometry(QtCore.QRect(100, 440, 451, 41))
        self.seek_slider.setObjectName("seek_slider")
        self.volume_slider = phonon.Phonon.VolumeSlider(MainProjectWidget)
        self.volume_slider.setGeometry(QtCore.QRect(560, 440, 114, 41))
        self.volume_slider.setObjectName("volume_slider")
        self.time_edit = QtGui.QTimeEdit(MainProjectWidget)
        self.time_edit.setGeometry(QtCore.QRect(10, 490, 118, 27))
        self.time_edit.setObjectName("time_edit")
        self.btn_pause = QtGui.QPushButton(MainProjectWidget)
        self.btn_pause.setGeometry(QtCore.QRect(10, 440, 41, 41))
        self.btn_pause.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/i/button_blue_pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_pause.setIcon(icon1)
        self.btn_pause.setIconSize(QtCore.QSize(40, 40))
        self.btn_pause.setObjectName("btn_pause")
        self.btn_stop = QtGui.QPushButton(MainProjectWidget)
        self.btn_stop.setGeometry(QtCore.QRect(50, 440, 41, 41))
        self.btn_stop.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/i/button_blue_stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_stop.setIcon(icon2)
        self.btn_stop.setIconSize(QtCore.QSize(40, 40))
        self.btn_stop.setObjectName("btn_stop")
        self.btn_play = QtGui.QPushButton(MainProjectWidget)
        self.btn_play.setGeometry(QtCore.QRect(10, 440, 41, 41))
        self.btn_play.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/i/button_blue_play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_play.setIcon(icon3)
        self.btn_play.setIconSize(QtCore.QSize(40, 40))
        self.btn_play.setObjectName("btn_play")
        self.btn_add_annotation = QtGui.QPushButton(MainProjectWidget)
        self.btn_add_annotation.setGeometry(QtCore.QRect(130, 480, 191, 41))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/i/comment_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add_annotation.setIcon(icon4)
        self.btn_add_annotation.setIconSize(QtCore.QSize(40, 40))
        self.btn_add_annotation.setObjectName("btn_add_annotation")
        self.frame_notes = QtGui.QFrame(MainProjectWidget)
        self.frame_notes.setGeometry(QtCore.QRect(690, 10, 301, 521))
        self.frame_notes.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_notes.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_notes.setObjectName("frame_notes")
        self.label = QtGui.QLabel(self.frame_notes)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 17))
        self.label.setObjectName("label")
        self.list_notes = QtGui.QListWidget(self.frame_notes)
        self.list_notes.setGeometry(QtCore.QRect(10, 30, 281, 431))
        self.list_notes.setObjectName("list_notes")
        self.btn_edit = QtGui.QPushButton(self.frame_notes)
        self.btn_edit.setGeometry(QtCore.QRect(10, 470, 131, 41))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/i/comment_edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_edit.setIcon(icon5)
        self.btn_edit.setIconSize(QtCore.QSize(40, 40))
        self.btn_edit.setObjectName("btn_edit")
        self.btn_delete = QtGui.QPushButton(self.frame_notes)
        self.btn_delete.setGeometry(QtCore.QRect(160, 470, 131, 41))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/i/comment_delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_delete.setIcon(icon6)
        self.btn_delete.setIconSize(QtCore.QSize(40, 40))
        self.btn_delete.setObjectName("btn_delete")
        self.btn_generate_ncl = QtGui.QPushButton(MainProjectWidget)
        self.btn_generate_ncl.setGeometry(QtCore.QRect(380, 480, 151, 41))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/i/notepad.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_generate_ncl.setIcon(icon7)
        self.btn_generate_ncl.setIconSize(QtCore.QSize(40, 40))
        self.btn_generate_ncl.setObjectName("btn_generate_ncl")
        self.btn_save_project = QtGui.QPushButton(MainProjectWidget)
        self.btn_save_project.setGeometry(QtCore.QRect(530, 480, 151, 41))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/i/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save_project.setIcon(icon8)
        self.btn_save_project.setIconSize(QtCore.QSize(40, 40))
        self.btn_save_project.setObjectName("btn_save_project")
        self.video_player = phonon.Phonon.VideoPlayer(MainProjectWidget)
        self.video_player.setGeometry(QtCore.QRect(10, 60, 671, 371))
        self.video_player.setObjectName("video_player")

        self.retranslateUi(MainProjectWidget)
        QtCore.QMetaObject.connectSlotsByName(MainProjectWidget)

    def retranslateUi(self, MainProjectWidget):
        MainProjectWidget.setWindowTitle(QtGui.QApplication.translate("MainProjectWidget", "Projeto", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_choose_video.setText(QtGui.QApplication.translate("MainProjectWidget", "Escolha o Vídeo", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_add_annotation.setText(QtGui.QApplication.translate("MainProjectWidget", "Adicionar Anotação", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainProjectWidget", "Anotações:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_edit.setText(QtGui.QApplication.translate("MainProjectWidget", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_delete.setText(QtGui.QApplication.translate("MainProjectWidget", "Excluir", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_generate_ncl.setText(QtGui.QApplication.translate("MainProjectWidget", "Gerar NCL", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_save_project.setText(QtGui.QApplication.translate("MainProjectWidget", "Salvar Projeto", None, QtGui.QApplication.UnicodeUTF8))

from PySide import phonon
import icons_rc
