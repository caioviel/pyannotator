# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/TextContent.ui'
#
# Created: Tue Nov 26 12:45:55 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_TextContent(object):
    def setupUi(self, TextContent):
        TextContent.setObjectName(_fromUtf8("TextContent"))
        TextContent.resize(743, 741)
        self.textEdit = QtGui.QTextEdit(TextContent)
        self.textEdit.setGeometry(QtCore.QRect(10, 70, 721, 121))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label = QtGui.QLabel(TextContent)
        self.label.setGeometry(QtCore.QRect(10, 50, 311, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(TextContent)
        self.label_2.setGeometry(QtCore.QRect(290, 246, 111, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(TextContent)
        self.label_3.setGeometry(QtCore.QRect(10, 246, 101, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.btn_Font = QtGui.QPushButton(TextContent)
        self.btn_Font.setGeometry(QtCore.QRect(10, 200, 161, 27))
        self.btn_Font.setObjectName(_fromUtf8("btn_Font"))
        self.btn_font_color = QtGui.QPushButton(TextContent)
        self.btn_font_color.setGeometry(QtCore.QRect(160, 240, 98, 27))
        self.btn_font_color.setObjectName(_fromUtf8("btn_font_color"))
        self.lbl_font_color = QtGui.QLabel(TextContent)
        self.lbl_font_color.setGeometry(QtCore.QRect(110, 246, 41, 21))
        self.lbl_font_color.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.lbl_font_color.setText(_fromUtf8(""))
        self.lbl_font_color.setObjectName(_fromUtf8("lbl_font_color"))
        self.lbl_bg_color = QtGui.QLabel(TextContent)
        self.lbl_bg_color.setGeometry(QtCore.QRect(390, 246, 41, 21))
        self.lbl_bg_color.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lbl_bg_color.setText(_fromUtf8(""))
        self.lbl_bg_color.setObjectName(_fromUtf8("lbl_bg_color"))
        self.btn_bg_color = QtGui.QPushButton(TextContent)
        self.btn_bg_color.setGeometry(QtCore.QRect(440, 240, 98, 27))
        self.btn_bg_color.setObjectName(_fromUtf8("btn_bg_color"))
        self.ckb_transparency = QtGui.QCheckBox(TextContent)
        self.ckb_transparency.setGeometry(QtCore.QRect(570, 240, 161, 31))
        self.ckb_transparency.setObjectName(_fromUtf8("ckb_transparency"))
        self.time_end = QtGui.QTimeEdit(TextContent)
        self.time_end.setGeometry(QtCore.QRect(360, 10, 91, 31))
        self.time_end.setObjectName(_fromUtf8("time_end"))
        self.txt_duration = QtGui.QPlainTextEdit(TextContent)
        self.txt_duration.setEnabled(True)
        self.txt_duration.setGeometry(QtCore.QRect(620, 10, 104, 31))
        self.txt_duration.setObjectName(_fromUtf8("txt_duration"))
        self.lbl_end_time = QtGui.QLabel(TextContent)
        self.lbl_end_time.setGeometry(QtCore.QRect(230, 16, 131, 21))
        self.lbl_end_time.setObjectName(_fromUtf8("lbl_end_time"))
        self.lbl_begin_time = QtGui.QLabel(TextContent)
        self.lbl_begin_time.setGeometry(QtCore.QRect(10, 16, 111, 21))
        self.lbl_begin_time.setObjectName(_fromUtf8("lbl_begin_time"))
        self.lbl_duration = QtGui.QLabel(TextContent)
        self.lbl_duration.setGeometry(QtCore.QRect(480, 16, 141, 21))
        self.lbl_duration.setObjectName(_fromUtf8("lbl_duration"))
        self.time_begin = QtGui.QTimeEdit(TextContent)
        self.time_begin.setGeometry(QtCore.QRect(120, 10, 91, 31))
        self.time_begin.setObjectName(_fromUtf8("time_begin"))
        self.layout_selection_holder = QtGui.QWidget(TextContent)
        self.layout_selection_holder.setGeometry(QtCore.QRect(20, 280, 700, 394))
        self.layout_selection_holder.setObjectName(_fromUtf8("layout_selection_holder"))
        self.btn_ok = QtGui.QPushButton(TextContent)
        self.btn_ok.setGeometry(QtCore.QRect(520, 690, 101, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/i/check.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_ok.setIcon(icon)
        self.btn_ok.setIconSize(QtCore.QSize(25, 25))
        self.btn_ok.setObjectName(_fromUtf8("btn_ok"))
        self.btn_cancel = QtGui.QPushButton(TextContent)
        self.btn_cancel.setGeometry(QtCore.QRect(630, 690, 101, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/i/no.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cancel.setIcon(icon1)
        self.btn_cancel.setIconSize(QtCore.QSize(25, 25))
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.btn_reset_layout = QtGui.QPushButton(TextContent)
        self.btn_reset_layout.setGeometry(QtCore.QRect(20, 680, 131, 31))
        self.btn_reset_layout.setObjectName(_fromUtf8("btn_reset_layout"))
        self.label_4 = QtGui.QLabel(TextContent)
        self.label_4.setGeometry(QtCore.QRect(180, 200, 101, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.cmb_alligment = QtGui.QComboBox(TextContent)
        self.cmb_alligment.setGeometry(QtCore.QRect(280, 200, 181, 27))
        self.cmb_alligment.setObjectName(_fromUtf8("cmb_alligment"))
        self.cmb_alligment.addItem(_fromUtf8(""))
        self.cmb_alligment.addItem(_fromUtf8(""))
        self.cmb_alligment.addItem(_fromUtf8(""))

        self.retranslateUi(TextContent)
        QtCore.QMetaObject.connectSlotsByName(TextContent)

    def retranslateUi(self, TextContent):
        TextContent.setWindowTitle(QtGui.QApplication.translate("TextContent", "Conteúdo em Texto", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("TextContent", "Entre com o conteúdo de texto:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("TextContent", "Cor de Fundo:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("TextContent", "Cor da Fonte:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Font.setText(QtGui.QApplication.translate("TextContent", "Selecionar Fonte", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_font_color.setText(QtGui.QApplication.translate("TextContent", "Mudar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_bg_color.setText(QtGui.QApplication.translate("TextContent", "Mudar", None, QtGui.QApplication.UnicodeUTF8))
        self.ckb_transparency.setText(QtGui.QApplication.translate("TextContent", "Fundo Transparente", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_end_time.setText(QtGui.QApplication.translate("TextContent", "Tempo de Termino:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_begin_time.setText(QtGui.QApplication.translate("TextContent", "Tempo de Início:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_duration.setText(QtGui.QApplication.translate("TextContent", "Duração (segundos):", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_ok.setText(QtGui.QApplication.translate("TextContent", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancel.setText(QtGui.QApplication.translate("TextContent", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_reset_layout.setText(QtGui.QApplication.translate("TextContent", "Resetar Posição", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("TextContent", "Alinhamento:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_alligment.setItemText(0, QtGui.QApplication.translate("TextContent", "Esquerda", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_alligment.setItemText(1, QtGui.QApplication.translate("TextContent", "Centro", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_alligment.setItemText(2, QtGui.QApplication.translate("TextContent", "Direita", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
