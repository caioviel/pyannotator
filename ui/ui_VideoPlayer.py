# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/VideoPlayer.ui'
#
# Created: Tue Nov 26 12:02:01 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_VideoPlayer(object):
    def setupUi(self, VideoPlayer):
        VideoPlayer.setObjectName(_fromUtf8("VideoPlayer"))
        VideoPlayer.resize(694, 432)
        self.video_player = phonon.Phonon.VideoPlayer(VideoPlayer)
        self.video_player.setGeometry(QtCore.QRect(10, 10, 671, 371))
        self.video_player.setObjectName(_fromUtf8("video_player"))
        self.seek_slider = phonon.Phonon.SeekSlider(VideoPlayer)
        self.seek_slider.setGeometry(QtCore.QRect(100, 390, 451, 41))
        self.seek_slider.setObjectName(_fromUtf8("seek_slider"))
        self.btn_play = QtGui.QPushButton(VideoPlayer)
        self.btn_play.setGeometry(QtCore.QRect(10, 390, 41, 41))
        self.btn_play.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/i/button_blue_play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_play.setIcon(icon)
        self.btn_play.setIconSize(QtCore.QSize(40, 40))
        self.btn_play.setObjectName(_fromUtf8("btn_play"))
        self.volume_slider = phonon.Phonon.VolumeSlider(VideoPlayer)
        self.volume_slider.setGeometry(QtCore.QRect(560, 390, 114, 41))
        self.volume_slider.setObjectName(_fromUtf8("volume_slider"))
        self.btn_stop = QtGui.QPushButton(VideoPlayer)
        self.btn_stop.setGeometry(QtCore.QRect(50, 390, 41, 41))
        self.btn_stop.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/i/button_blue_stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_stop.setIcon(icon1)
        self.btn_stop.setIconSize(QtCore.QSize(40, 40))
        self.btn_stop.setObjectName(_fromUtf8("btn_stop"))
        self.btn_pause = QtGui.QPushButton(VideoPlayer)
        self.btn_pause.setGeometry(QtCore.QRect(10, 390, 41, 41))
        self.btn_pause.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/i/button_blue_pause.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_pause.setIcon(icon2)
        self.btn_pause.setIconSize(QtCore.QSize(40, 40))
        self.btn_pause.setObjectName(_fromUtf8("btn_pause"))

        self.retranslateUi(VideoPlayer)
        QtCore.QMetaObject.connectSlotsByName(VideoPlayer)

    def retranslateUi(self, VideoPlayer):
        VideoPlayer.setWindowTitle(QtGui.QApplication.translate("VideoPlayer", "Player de Vídeo", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import phonon
import icons_rc
