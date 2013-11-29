# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/AudioPlayer.ui'
#
# Created: Fri Nov 29 17:39:24 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AudioPlayer(object):
    def setupUi(self, AudioPlayer):
        AudioPlayer.setObjectName(_fromUtf8("AudioPlayer"))
        AudioPlayer.resize(694, 92)
        self.btn_stop = QtGui.QPushButton(AudioPlayer)
        self.btn_stop.setGeometry(QtCore.QRect(50, 40, 41, 41))
        self.btn_stop.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/i/button_blue_stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_stop.setIcon(icon)
        self.btn_stop.setIconSize(QtCore.QSize(40, 40))
        self.btn_stop.setObjectName(_fromUtf8("btn_stop"))
        self.btn_play = QtGui.QPushButton(AudioPlayer)
        self.btn_play.setGeometry(QtCore.QRect(10, 40, 41, 41))
        self.btn_play.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/i/button_blue_play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_play.setIcon(icon1)
        self.btn_play.setIconSize(QtCore.QSize(40, 40))
        self.btn_play.setObjectName(_fromUtf8("btn_play"))
        self.volume_slider = phonon.Phonon.VolumeSlider(AudioPlayer)
        self.volume_slider.setGeometry(QtCore.QRect(560, 40, 114, 41))
        self.volume_slider.setObjectName(_fromUtf8("volume_slider"))
        self.seek_slider = phonon.Phonon.SeekSlider(AudioPlayer)
        self.seek_slider.setGeometry(QtCore.QRect(100, 40, 451, 41))
        self.seek_slider.setObjectName(_fromUtf8("seek_slider"))
        self.lbl_audio_description = QtGui.QLabel(AudioPlayer)
        self.lbl_audio_description.setGeometry(QtCore.QRect(10, 10, 671, 17))
        self.lbl_audio_description.setStyleSheet(_fromUtf8("font: 75 bold 12pt \"Ubuntu\";"))
        self.lbl_audio_description.setObjectName(_fromUtf8("lbl_audio_description"))
        self.btn_pause = QtGui.QPushButton(AudioPlayer)
        self.btn_pause.setGeometry(QtCore.QRect(10, 40, 41, 41))
        self.btn_pause.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/i/button_blue_pause.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_pause.setIcon(icon2)
        self.btn_pause.setIconSize(QtCore.QSize(40, 40))
        self.btn_pause.setObjectName(_fromUtf8("btn_pause"))

        self.retranslateUi(AudioPlayer)
        QtCore.QMetaObject.connectSlotsByName(AudioPlayer)

    def retranslateUi(self, AudioPlayer):
        AudioPlayer.setWindowTitle(QtGui.QApplication.translate("AudioPlayer", "Player de Áudio", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_audio_description.setText(QtGui.QApplication.translate("AudioPlayer", "Nenhum áudio selecionado...", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import phonon
import icons_rc
