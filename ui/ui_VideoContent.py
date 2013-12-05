# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/VideoContent.ui'
#
# Created: Wed Dec  4 23:42:37 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_VideoContent(object):
    def setupUi(self, VideoContent):
        VideoContent.setObjectName(_fromUtf8("VideoContent"))
        VideoContent.resize(744, 640)
        self.tabs = QtGui.QTabWidget(VideoContent)
        self.tabs.setGeometry(QtCore.QRect(10, 50, 721, 531))
        self.tabs.setObjectName(_fromUtf8("tabs"))
        self.tab_content = QtGui.QWidget()
        self.tab_content.setObjectName(_fromUtf8("tab_content"))
        self.txt_media_name = QtGui.QPlainTextEdit(self.tab_content)
        self.txt_media_name.setGeometry(QtCore.QRect(10, 10, 521, 41))
        self.txt_media_name.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.txt_media_name.setObjectName(_fromUtf8("txt_media_name"))
        self.btn_choose_video = QtGui.QPushButton(self.tab_content)
        self.btn_choose_video.setGeometry(QtCore.QRect(540, 10, 161, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/i/folder_open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_choose_video.setIcon(icon)
        self.btn_choose_video.setIconSize(QtCore.QSize(40, 40))
        self.btn_choose_video.setObjectName(_fromUtf8("btn_choose_video"))
        self.player_holder = QtGui.QWidget(self.tab_content)
        self.player_holder.setGeometry(QtCore.QRect(0, 50, 721, 451))
        self.player_holder.setObjectName(_fromUtf8("player_holder"))
        self.tabs.addTab(self.tab_content, _fromUtf8(""))
        self.tab_position = QtGui.QWidget()
        self.tab_position.setObjectName(_fromUtf8("tab_position"))
        self.tabs.addTab(self.tab_position, _fromUtf8(""))
        self.tab_behavior = QtGui.QWidget()
        self.tab_behavior.setObjectName(_fromUtf8("tab_behavior"))
        self.volume_control_widget = QtGui.QWidget(self.tab_behavior)
        self.volume_control_widget.setGeometry(QtCore.QRect(721, 20, 301, 237))
        self.volume_control_widget.setObjectName(_fromUtf8("volume_control_widget"))
        self.tabs.addTab(self.tab_behavior, _fromUtf8(""))
        self.lbl_begin_time = QtGui.QLabel(VideoContent)
        self.lbl_begin_time.setGeometry(QtCore.QRect(10, 16, 111, 21))
        self.lbl_begin_time.setObjectName(_fromUtf8("lbl_begin_time"))
        self.time_begin = QtGui.QTimeEdit(VideoContent)
        self.time_begin.setGeometry(QtCore.QRect(120, 10, 91, 31))
        self.time_begin.setObjectName(_fromUtf8("time_begin"))
        self.lbl_duration = QtGui.QLabel(VideoContent)
        self.lbl_duration.setGeometry(QtCore.QRect(480, 16, 141, 21))
        self.lbl_duration.setObjectName(_fromUtf8("lbl_duration"))
        self.lbl_end_time = QtGui.QLabel(VideoContent)
        self.lbl_end_time.setGeometry(QtCore.QRect(230, 16, 131, 21))
        self.lbl_end_time.setObjectName(_fromUtf8("lbl_end_time"))
        self.time_end = QtGui.QTimeEdit(VideoContent)
        self.time_end.setGeometry(QtCore.QRect(360, 10, 91, 31))
        self.time_end.setObjectName(_fromUtf8("time_end"))
        self.txt_duration = QtGui.QPlainTextEdit(VideoContent)
        self.txt_duration.setEnabled(True)
        self.txt_duration.setGeometry(QtCore.QRect(620, 10, 104, 31))
        self.txt_duration.setObjectName(_fromUtf8("txt_duration"))
        self.btn_ok = QtGui.QPushButton(VideoContent)
        self.btn_ok.setGeometry(QtCore.QRect(520, 590, 101, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/i/check.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_ok.setIcon(icon1)
        self.btn_ok.setIconSize(QtCore.QSize(25, 25))
        self.btn_ok.setObjectName(_fromUtf8("btn_ok"))
        self.btn_cancel = QtGui.QPushButton(VideoContent)
        self.btn_cancel.setGeometry(QtCore.QRect(630, 590, 101, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/i/no.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cancel.setIcon(icon2)
        self.btn_cancel.setIconSize(QtCore.QSize(25, 25))
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))

        self.retranslateUi(VideoContent)
        self.tabs.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(VideoContent)

    def retranslateUi(self, VideoContent):
        VideoContent.setWindowTitle(QtGui.QApplication.translate("VideoContent", "Conteúdo em Vídeo", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_choose_video.setText(QtGui.QApplication.translate("VideoContent", "Escolher Vídeo", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_content), QtGui.QApplication.translate("VideoContent", "Conteúdo", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_position), QtGui.QApplication.translate("VideoContent", "Posição", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_behavior), QtGui.QApplication.translate("VideoContent", "Comportamento", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_begin_time.setText(QtGui.QApplication.translate("VideoContent", "Tempo de Início:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_duration.setText(QtGui.QApplication.translate("VideoContent", "Duração (segundos):", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_end_time.setText(QtGui.QApplication.translate("VideoContent", "Tempo de Termino:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_ok.setText(QtGui.QApplication.translate("VideoContent", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancel.setText(QtGui.QApplication.translate("VideoContent", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
