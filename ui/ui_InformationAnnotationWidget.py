# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InformationAnnotationWidget.ui'
#
# Created: Sun Feb  3 12:30:30 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_InformationAnnotationWidget(object):
    def setupUi(self, InformationAnnotationWidget):
        InformationAnnotationWidget.setObjectName("InformationAnnotationWidget")
        InformationAnnotationWidget.resize(663, 680)
        self.label = QtGui.QLabel(InformationAnnotationWidget)
        self.label.setGeometry(QtCore.QRect(120, 20, 141, 17))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(InformationAnnotationWidget)
        self.label_2.setGeometry(QtCore.QRect(120, 60, 251, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(InformationAnnotationWidget)
        self.label_3.setGeometry(QtCore.QRect(390, 60, 131, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(InformationAnnotationWidget)
        self.label_4.setGeometry(QtCore.QRect(10, 140, 171, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(InformationAnnotationWidget)
        self.label_5.setGeometry(QtCore.QRect(10, 200, 171, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(InformationAnnotationWidget)
        self.label_6.setGeometry(QtCore.QRect(10, 170, 81, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtGui.QLabel(InformationAnnotationWidget)
        self.label_7.setGeometry(QtCore.QRect(310, 200, 161, 17))
        self.label_7.setObjectName("label_7")
        self.cmb_content_type = QtGui.QComboBox(InformationAnnotationWidget)
        self.cmb_content_type.setGeometry(QtCore.QRect(140, 130, 161, 27))
        self.cmb_content_type.setObjectName("cmb_content_type")
        self.cmb_content_type.addItem("")
        self.cmb_content_type.addItem("")
        self.cmb_content_type.addItem("")
        self.cmb_content_type.addItem("")
        self.cmb_content_type.addItem("")
        self.time_icon = QtGui.QTimeEdit(InformationAnnotationWidget)
        self.time_icon.setGeometry(QtCore.QRect(260, 50, 118, 27))
        self.time_icon.setObjectName("time_icon")
        self.time_content = QtGui.QTimeEdit(InformationAnnotationWidget)
        self.time_content.setGeometry(QtCore.QRect(180, 190, 118, 27))
        self.time_content.setObjectName("time_content")
        self.cmb_content_durartion = QtGui.QComboBox(InformationAnnotationWidget)
        self.cmb_content_durartion.setGeometry(QtCore.QRect(480, 190, 51, 31))
        self.cmb_content_durartion.setObjectName("cmb_content_durartion")
        self.cmb_content_durartion.addItem("")
        self.cmb_content_durartion.setItemText(0, "")
        self.cmb_content_durartion.addItem("")
        self.cmb_content_durartion.addItem("")
        self.cmb_content_durartion.addItem("")
        self.cmb_content_durartion.addItem("")
        self.label_8 = QtGui.QLabel(InformationAnnotationWidget)
        self.label_8.setGeometry(QtCore.QRect(540, 200, 71, 17))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtGui.QLabel(InformationAnnotationWidget)
        self.label_9.setGeometry(QtCore.QRect(580, 60, 71, 17))
        self.label_9.setObjectName("label_9")
        self.cmb_icon_duration = QtGui.QComboBox(InformationAnnotationWidget)
        self.cmb_icon_duration.setGeometry(QtCore.QRect(520, 50, 51, 31))
        self.cmb_icon_duration.setObjectName("cmb_icon_duration")
        self.cmb_icon_duration.addItem("")
        self.cmb_icon_duration.addItem("")
        self.cmb_icon_duration.addItem("")
        self.cmb_icon_duration.addItem("")
        self.btn_choose_content = QtGui.QPushButton(InformationAnnotationWidget)
        self.btn_choose_content.setGeometry(QtCore.QRect(560, 160, 98, 27))
        self.btn_choose_content.setObjectName("btn_choose_content")
        self.lbl_icon_display = QtGui.QLabel(InformationAnnotationWidget)
        self.lbl_icon_display.setGeometry(QtCore.QRect(10, 10, 100, 100))
        self.lbl_icon_display.setFrameShape(QtGui.QFrame.Box)
        self.lbl_icon_display.setText("")
        self.lbl_icon_display.setObjectName("lbl_icon_display")
        self.cmb_icon = QtGui.QComboBox(InformationAnnotationWidget)
        self.cmb_icon.setGeometry(QtCore.QRect(270, 10, 271, 27))
        self.cmb_icon.setObjectName("cmb_icon")
        self.btn_choose_icon = QtGui.QPushButton(InformationAnnotationWidget)
        self.btn_choose_icon.setGeometry(QtCore.QRect(560, 10, 98, 27))
        self.btn_choose_icon.setObjectName("btn_choose_icon")
        self.frame = QtGui.QFrame(InformationAnnotationWidget)
        self.frame.setGeometry(QtCore.QRect(10, 240, 641, 391))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lbl_image_display = QtGui.QLabel(self.frame)
        self.lbl_image_display.setGeometry(QtCore.QRect(10, 10, 621, 371))
        self.lbl_image_display.setObjectName("lbl_image_display")
        self.video_player = phonon.Phonon.VideoPlayer(self.frame)
        self.video_player.setGeometry(QtCore.QRect(10, 10, 621, 341))
        self.video_player.setObjectName("video_player")
        self.seek_slider = phonon.Phonon.SeekSlider(self.frame)
        self.seek_slider.setGeometry(QtCore.QRect(90, 360, 421, 21))
        self.seek_slider.setObjectName("seek_slider")
        self.volume_slider = phonon.Phonon.VolumeSlider(self.frame)
        self.volume_slider.setGeometry(QtCore.QRect(510, 360, 121, 21))
        self.volume_slider.setObjectName("volume_slider")
        self.txt_content_display = QtGui.QPlainTextEdit(self.frame)
        self.txt_content_display.setGeometry(QtCore.QRect(10, 10, 621, 371))
        self.txt_content_display.setObjectName("txt_content_display")
        self.web_content = QtWebKit.QWebView(self.frame)
        self.web_content.setGeometry(QtCore.QRect(10, 10, 621, 371))
        self.web_content.setUrl(QtCore.QUrl("about:blank"))
        self.web_content.setObjectName("web_content")
        self.btn_play = QtGui.QPushButton(self.frame)
        self.btn_play.setGeometry(QtCore.QRect(10, 350, 41, 41))
        self.btn_play.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/i/button_blue_play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_play.setIcon(icon)
        self.btn_play.setIconSize(QtCore.QSize(40, 40))
        self.btn_play.setObjectName("btn_play")
        self.btn_stop = QtGui.QPushButton(self.frame)
        self.btn_stop.setGeometry(QtCore.QRect(50, 350, 41, 41))
        self.btn_stop.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/i/button_blue_stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_stop.setIcon(icon1)
        self.btn_stop.setIconSize(QtCore.QSize(40, 40))
        self.btn_stop.setObjectName("btn_stop")
        self.btn_pause = QtGui.QPushButton(self.frame)
        self.btn_pause.setGeometry(QtCore.QRect(10, 350, 41, 41))
        self.btn_pause.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/i/button_blue_pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_pause.setIcon(icon2)
        self.btn_pause.setIconSize(QtCore.QSize(40, 40))
        self.btn_pause.setObjectName("btn_pause")
        self.btn_save = QtGui.QPushButton(InformationAnnotationWidget)
        self.btn_save.setGeometry(QtCore.QRect(440, 640, 98, 27))
        self.btn_save.setObjectName("btn_save")
        self.btn_cancel = QtGui.QPushButton(InformationAnnotationWidget)
        self.btn_cancel.setGeometry(QtCore.QRect(550, 640, 98, 27))
        self.btn_cancel.setObjectName("btn_cancel")
        self.txt_content = QtGui.QPlainTextEdit(InformationAnnotationWidget)
        self.txt_content.setGeometry(QtCore.QRect(90, 160, 461, 31))
        self.txt_content.setObjectName("txt_content")

        self.retranslateUi(InformationAnnotationWidget)
        QtCore.QMetaObject.connectSlotsByName(InformationAnnotationWidget)

    def retranslateUi(self, InformationAnnotationWidget):
        InformationAnnotationWidget.setWindowTitle(QtGui.QApplication.translate("InformationAnnotationWidget", "Conteúdo Complementar - Informação Simples", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("InformationAnnotationWidget", "Ícone de Notificação:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("InformationAnnotationWidget", "Timestamp do Ícone:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("InformationAnnotationWidget", "Duração do Ícone:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("InformationAnnotationWidget", "Tipo de Conteúdo:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("InformationAnnotationWidget", "Timestamp do Conteúdo:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("InformationAnnotationWidget", "Conteúdo:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("InformationAnnotationWidget", "Duração do Conteúdo:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_content_type.setItemText(0, QtGui.QApplication.translate("InformationAnnotationWidget", "Áudio", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_content_type.setItemText(1, QtGui.QApplication.translate("InformationAnnotationWidget", "Vídeo", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_content_type.setItemText(2, QtGui.QApplication.translate("InformationAnnotationWidget", "Imagem", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_content_type.setItemText(3, QtGui.QApplication.translate("InformationAnnotationWidget", "Texto Plano", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_content_type.setItemText(4, QtGui.QApplication.translate("InformationAnnotationWidget", "Html", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_content_durartion.setItemText(1, QtGui.QApplication.translate("InformationAnnotationWidget", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_content_durartion.setItemText(2, QtGui.QApplication.translate("InformationAnnotationWidget", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_content_durartion.setItemText(3, QtGui.QApplication.translate("InformationAnnotationWidget", "15", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_content_durartion.setItemText(4, QtGui.QApplication.translate("InformationAnnotationWidget", "20", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("InformationAnnotationWidget", "segundos", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("InformationAnnotationWidget", "segundos", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_icon_duration.setItemText(0, QtGui.QApplication.translate("InformationAnnotationWidget", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_icon_duration.setItemText(1, QtGui.QApplication.translate("InformationAnnotationWidget", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_icon_duration.setItemText(2, QtGui.QApplication.translate("InformationAnnotationWidget", "15", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_icon_duration.setItemText(3, QtGui.QApplication.translate("InformationAnnotationWidget", "20", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_choose_content.setText(QtGui.QApplication.translate("InformationAnnotationWidget", "Escolher", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_choose_icon.setText(QtGui.QApplication.translate("InformationAnnotationWidget", "Escolher", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_image_display.setText(QtGui.QApplication.translate("InformationAnnotationWidget", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_save.setText(QtGui.QApplication.translate("InformationAnnotationWidget", "Salvar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancel.setText(QtGui.QApplication.translate("InformationAnnotationWidget", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

from PySide import phonon
from PySide import QtWebKit
import icons_rc
