# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/AudioContent.ui'
#
# Created: Thu Dec 12 14:19:17 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AudioContent(object):
    def setupUi(self, AudioContent):
        AudioContent.setObjectName(_fromUtf8("AudioContent"))
        AudioContent.resize(742, 451)
        self.lbl_begin_time = QtGui.QLabel(AudioContent)
        self.lbl_begin_time.setGeometry(QtCore.QRect(10, 20, 111, 21))
        self.lbl_begin_time.setObjectName(_fromUtf8("lbl_begin_time"))
        self.lbl_duration = QtGui.QLabel(AudioContent)
        self.lbl_duration.setGeometry(QtCore.QRect(480, 20, 141, 21))
        self.lbl_duration.setObjectName(_fromUtf8("lbl_duration"))
        self.txt_duration = QtGui.QPlainTextEdit(AudioContent)
        self.txt_duration.setEnabled(True)
        self.txt_duration.setGeometry(QtCore.QRect(620, 14, 104, 31))
        self.txt_duration.setObjectName(_fromUtf8("txt_duration"))
        self.lbl_end_time = QtGui.QLabel(AudioContent)
        self.lbl_end_time.setGeometry(QtCore.QRect(230, 20, 131, 21))
        self.lbl_end_time.setObjectName(_fromUtf8("lbl_end_time"))
        self.time_begin = QtGui.QTimeEdit(AudioContent)
        self.time_begin.setGeometry(QtCore.QRect(120, 14, 91, 31))
        self.time_begin.setObjectName(_fromUtf8("time_begin"))
        self.time_end = QtGui.QTimeEdit(AudioContent)
        self.time_end.setGeometry(QtCore.QRect(360, 14, 91, 31))
        self.time_end.setObjectName(_fromUtf8("time_end"))
        self.btn_choose_audio = QtGui.QPushButton(AudioContent)
        self.btn_choose_audio.setGeometry(QtCore.QRect(560, 50, 161, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/i/folder_open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_choose_audio.setIcon(icon)
        self.btn_choose_audio.setIconSize(QtCore.QSize(40, 40))
        self.btn_choose_audio.setObjectName(_fromUtf8("btn_choose_audio"))
        self.txt_media_name = QtGui.QPlainTextEdit(AudioContent)
        self.txt_media_name.setGeometry(QtCore.QRect(10, 50, 541, 41))
        self.txt_media_name.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.txt_media_name.setObjectName(_fromUtf8("txt_media_name"))
        self.audio_player_widget = QtGui.QWidget(AudioContent)
        self.audio_player_widget.setGeometry(QtCore.QRect(20, 100, 694, 92))
        self.audio_player_widget.setObjectName(_fromUtf8("audio_player_widget"))
        self.volume_control_widget = QtGui.QWidget(AudioContent)
        self.volume_control_widget.setGeometry(QtCore.QRect(20, 200, 301, 237))
        self.volume_control_widget.setObjectName(_fromUtf8("volume_control_widget"))
        self.btn_ok = QtGui.QPushButton(AudioContent)
        self.btn_ok.setGeometry(QtCore.QRect(520, 400, 101, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/i/check.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_ok.setIcon(icon1)
        self.btn_ok.setIconSize(QtCore.QSize(25, 25))
        self.btn_ok.setObjectName(_fromUtf8("btn_ok"))
        self.btn_cancel = QtGui.QPushButton(AudioContent)
        self.btn_cancel.setGeometry(QtCore.QRect(630, 400, 101, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/i/no.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cancel.setIcon(icon2)
        self.btn_cancel.setIconSize(QtCore.QSize(25, 25))
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))

        self.retranslateUi(AudioContent)
        QtCore.QMetaObject.connectSlotsByName(AudioContent)

    def retranslateUi(self, AudioContent):
        AudioContent.setWindowTitle(QtGui.QApplication.translate("AudioContent", "Conteúdo em Áudio", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_begin_time.setText(QtGui.QApplication.translate("AudioContent", "Tempo de Início:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_duration.setText(QtGui.QApplication.translate("AudioContent", "Duração (segundos):", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_end_time.setText(QtGui.QApplication.translate("AudioContent", "Tempo de Término:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_choose_audio.setText(QtGui.QApplication.translate("AudioContent", "Escolher Áudio", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_ok.setText(QtGui.QApplication.translate("AudioContent", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancel.setText(QtGui.QApplication.translate("AudioContent", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
