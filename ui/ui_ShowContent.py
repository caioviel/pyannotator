# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ShowContent.ui'
#
# Created: Thu Dec  5 19:02:03 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ShowContent(object):
    def setupUi(self, ShowContent):
        ShowContent.setObjectName(_fromUtf8("ShowContent"))
        ShowContent.resize(763, 647)
        self.lbl_begin_time = QtGui.QLabel(ShowContent)
        self.lbl_begin_time.setGeometry(QtCore.QRect(10, 20, 141, 21))
        self.lbl_begin_time.setObjectName(_fromUtf8("lbl_begin_time"))
        self.time_begin = QtGui.QTimeEdit(ShowContent)
        self.time_begin.setGeometry(QtCore.QRect(70, 14, 91, 31))
        self.time_begin.setObjectName(_fromUtf8("time_begin"))
        self.textEdit = QtGui.QTextEdit(ShowContent)
        self.textEdit.setGeometry(QtCore.QRect(260, 10, 491, 41))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label = QtGui.QLabel(ShowContent)
        self.label.setGeometry(QtCore.QRect(170, 10, 91, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.tabs = QtGui.QTabWidget(ShowContent)
        self.tabs.setGeometry(QtCore.QRect(20, 60, 721, 531))
        self.tabs.setObjectName(_fromUtf8("tabs"))
        self.tab_icon = QtGui.QWidget()
        self.tab_icon.setObjectName(_fromUtf8("tab_icon"))
        self.frame = QtGui.QFrame(self.tab_icon)
        self.frame.setGeometry(QtCore.QRect(20, 10, 341, 271))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.radio_info = QtGui.QRadioButton(self.frame)
        self.radio_info.setGeometry(QtCore.QRect(10, 20, 116, 71))
        self.radio_info.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/ncl/icon_info.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radio_info.setIcon(icon)
        self.radio_info.setIconSize(QtCore.QSize(30, 30))
        self.radio_info.setObjectName(_fromUtf8("radio_info"))
        self.radio_no = QtGui.QRadioButton(self.frame)
        self.radio_no.setGeometry(QtCore.QRect(200, 20, 116, 71))
        self.radio_no.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/ncl/icon_no.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radio_no.setIcon(icon1)
        self.radio_no.setIconSize(QtCore.QSize(30, 30))
        self.radio_no.setObjectName(_fromUtf8("radio_no"))
        self.radio_sexual = QtGui.QRadioButton(self.frame)
        self.radio_sexual.setGeometry(QtCore.QRect(10, 70, 116, 71))
        self.radio_sexual.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/ncl/icon_sexual.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radio_sexual.setIcon(icon2)
        self.radio_sexual.setIconSize(QtCore.QSize(30, 30))
        self.radio_sexual.setObjectName(_fromUtf8("radio_sexual"))
        self.radio_violence = QtGui.QRadioButton(self.frame)
        self.radio_violence.setGeometry(QtCore.QRect(100, 20, 116, 71))
        self.radio_violence.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/ncl/icon_violencia.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radio_violence.setIcon(icon3)
        self.radio_violence.setIconSize(QtCore.QSize(30, 30))
        self.radio_violence.setObjectName(_fromUtf8("radio_violence"))
        self.radio_yes = QtGui.QRadioButton(self.frame)
        self.radio_yes.setGeometry(QtCore.QRect(100, 70, 116, 71))
        self.radio_yes.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/ncl/icon_yes.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radio_yes.setIcon(icon4)
        self.radio_yes.setIconSize(QtCore.QSize(30, 30))
        self.radio_yes.setObjectName(_fromUtf8("radio_yes"))
        self.radio_personalized = QtGui.QRadioButton(self.frame)
        self.radio_personalized.setGeometry(QtCore.QRect(200, 70, 141, 71))
        self.radio_personalized.setIconSize(QtCore.QSize(30, 30))
        self.radio_personalized.setObjectName(_fromUtf8("radio_personalized"))
        self.btn_choose_icon = QtGui.QPushButton(self.frame)
        self.btn_choose_icon.setGeometry(QtCore.QRect(180, 130, 151, 41))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/i/folder_open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_choose_icon.setIcon(icon5)
        self.btn_choose_icon.setIconSize(QtCore.QSize(40, 40))
        self.btn_choose_icon.setObjectName(_fromUtf8("btn_choose_icon"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(80, 10, 161, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 190, 161, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 230, 191, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.cmb_icon_before = QtGui.QComboBox(self.frame)
        self.cmb_icon_before.setGeometry(QtCore.QRect(150, 190, 51, 27))
        self.cmb_icon_before.setObjectName(_fromUtf8("cmb_icon_before"))
        self.cmb_icon_before.addItem(_fromUtf8(""))
        self.cmb_icon_before.addItem(_fromUtf8(""))
        self.cmb_icon_before.addItem(_fromUtf8(""))
        self.cmb_icon_before.addItem(_fromUtf8(""))
        self.cmb_icon_before.addItem(_fromUtf8(""))
        self.cmb_icon_before.addItem(_fromUtf8(""))
        self.cmb_icon_duration = QtGui.QComboBox(self.frame)
        self.cmb_icon_duration.setGeometry(QtCore.QRect(200, 230, 51, 27))
        self.cmb_icon_duration.setObjectName(_fromUtf8("cmb_icon_duration"))
        self.cmb_icon_duration.addItem(_fromUtf8(""))
        self.cmb_icon_duration.addItem(_fromUtf8(""))
        self.cmb_icon_duration.addItem(_fromUtf8(""))
        self.cmb_icon_duration.addItem(_fromUtf8(""))
        self.cmb_icon_duration.addItem(_fromUtf8(""))
        self.cmb_icon_duration.addItem(_fromUtf8(""))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(210, 190, 131, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(260, 230, 111, 31))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.frame_3 = QtGui.QFrame(self.tab_icon)
        self.frame_3.setGeometry(QtCore.QRect(20, 280, 681, 211))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.radio_tr = QtGui.QRadioButton(self.frame_3)
        self.radio_tr.setGeometry(QtCore.QRect(20, 40, 181, 22))
        self.radio_tr.setObjectName(_fromUtf8("radio_tr"))
        self.label_7 = QtGui.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 121, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.radio_tl = QtGui.QRadioButton(self.frame_3)
        self.radio_tl.setGeometry(QtCore.QRect(20, 70, 221, 22))
        self.radio_tl.setObjectName(_fromUtf8("radio_tl"))
        self.radio_br = QtGui.QRadioButton(self.frame_3)
        self.radio_br.setGeometry(QtCore.QRect(20, 100, 181, 22))
        self.radio_br.setObjectName(_fromUtf8("radio_br"))
        self.radio_bl = QtGui.QRadioButton(self.frame_3)
        self.radio_bl.setGeometry(QtCore.QRect(20, 130, 201, 22))
        self.radio_bl.setObjectName(_fromUtf8("radio_bl"))
        self.radio_free_position = QtGui.QRadioButton(self.frame_3)
        self.radio_free_position.setGeometry(QtCore.QRect(20, 160, 181, 22))
        self.radio_free_position.setObjectName(_fromUtf8("radio_free_position"))
        self.widget_icon = QtGui.QWidget(self.frame_3)
        self.widget_icon.setGeometry(QtCore.QRect(330, 10, 341, 191))
        self.widget_icon.setObjectName(_fromUtf8("widget_icon"))
        self.frame_4 = QtGui.QFrame(self.tab_icon)
        self.frame_4.setGeometry(QtCore.QRect(360, 10, 341, 271))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.ckb_viber = QtGui.QCheckBox(self.frame_4)
        self.ckb_viber.setGeometry(QtCore.QRect(20, 140, 171, 22))
        self.ckb_viber.setObjectName(_fromUtf8("ckb_viber"))
        self.comboBox = QtGui.QComboBox(self.frame_4)
        self.comboBox.setGeometry(QtCore.QRect(150, 10, 171, 27))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.btn_choose_icon_2 = QtGui.QPushButton(self.frame_4)
        self.btn_choose_icon_2.setGeometry(QtCore.QRect(150, 40, 171, 41))
        self.btn_choose_icon_2.setIcon(icon5)
        self.btn_choose_icon_2.setIconSize(QtCore.QSize(40, 40))
        self.btn_choose_icon_2.setObjectName(_fromUtf8("btn_choose_icon_2"))
        self.ckb_audio = QtGui.QCheckBox(self.frame_4)
        self.ckb_audio.setGeometry(QtCore.QRect(20, 10, 141, 21))
        self.ckb_audio.setObjectName(_fromUtf8("ckb_audio"))
        self.tabs.addTab(self.tab_icon, _fromUtf8(""))
        self.tab_interaction = QtGui.QWidget()
        self.tab_interaction.setObjectName(_fromUtf8("tab_interaction"))
        self.radio_skip = QtGui.QRadioButton(self.tab_interaction)
        self.radio_skip.setGeometry(QtCore.QRect(160, 20, 116, 22))
        self.radio_skip.setObjectName(_fromUtf8("radio_skip"))
        self.radio_back = QtGui.QRadioButton(self.tab_interaction)
        self.radio_back.setGeometry(QtCore.QRect(300, 20, 161, 22))
        self.radio_back.setObjectName(_fromUtf8("radio_back"))
        self.radio_show = QtGui.QRadioButton(self.tab_interaction)
        self.radio_show.setGeometry(QtCore.QRect(10, 20, 116, 22))
        self.radio_show.setObjectName(_fromUtf8("radio_show"))
        self.radio_back_to = QtGui.QRadioButton(self.tab_interaction)
        self.radio_back_to.setGeometry(QtCore.QRect(480, 20, 231, 22))
        self.radio_back_to.setObjectName(_fromUtf8("radio_back_to"))
        self.tabs.addTab(self.tab_interaction, _fromUtf8(""))
        self.tab_content = QtGui.QWidget()
        self.tab_content.setObjectName(_fromUtf8("tab_content"))
        self.tabs.addTab(self.tab_content, _fromUtf8(""))
        self.tab_behavior = QtGui.QWidget()
        self.tab_behavior.setObjectName(_fromUtf8("tab_behavior"))
        self.ckb_compulsory = QtGui.QCheckBox(self.tab_behavior)
        self.ckb_compulsory.setGeometry(QtCore.QRect(40, 30, 331, 22))
        self.ckb_compulsory.setObjectName(_fromUtf8("ckb_compulsory"))
        self.ckb_pause_main_video = QtGui.QCheckBox(self.tab_behavior)
        self.ckb_pause_main_video.setGeometry(QtCore.QRect(40, 90, 331, 22))
        self.ckb_pause_main_video.setObjectName(_fromUtf8("ckb_pause_main_video"))
        self.ckb_allows_end_content = QtGui.QCheckBox(self.tab_behavior)
        self.ckb_allows_end_content.setGeometry(QtCore.QRect(40, 120, 331, 22))
        self.ckb_allows_end_content.setChecked(True)
        self.ckb_allows_end_content.setObjectName(_fromUtf8("ckb_allows_end_content"))
        self.ckb_show_on_mobile = QtGui.QCheckBox(self.tab_behavior)
        self.ckb_show_on_mobile.setGeometry(QtCore.QRect(40, 180, 331, 22))
        self.ckb_show_on_mobile.setObjectName(_fromUtf8("ckb_show_on_mobile"))
        self.ckb_show_on_tv = QtGui.QCheckBox(self.tab_behavior)
        self.ckb_show_on_tv.setGeometry(QtCore.QRect(40, 150, 331, 22))
        self.ckb_show_on_tv.setChecked(True)
        self.ckb_show_on_tv.setObjectName(_fromUtf8("ckb_show_on_tv"))
        self.ckb_compulsory_2 = QtGui.QCheckBox(self.tab_behavior)
        self.ckb_compulsory_2.setGeometry(QtCore.QRect(40, 60, 331, 22))
        self.ckb_compulsory_2.setObjectName(_fromUtf8("ckb_compulsory_2"))
        self.tabs.addTab(self.tab_behavior, _fromUtf8(""))
        self.btn_cancel = QtGui.QPushButton(ShowContent)
        self.btn_cancel.setGeometry(QtCore.QRect(640, 600, 101, 41))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/i/no.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cancel.setIcon(icon6)
        self.btn_cancel.setIconSize(QtCore.QSize(25, 25))
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.btn_ok = QtGui.QPushButton(ShowContent)
        self.btn_ok.setGeometry(QtCore.QRect(530, 600, 101, 41))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/i/check.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_ok.setIcon(icon7)
        self.btn_ok.setIconSize(QtCore.QSize(25, 25))
        self.btn_ok.setObjectName(_fromUtf8("btn_ok"))

        self.retranslateUi(ShowContent)
        self.tabs.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(ShowContent)

    def retranslateUi(self, ShowContent):
        ShowContent.setWindowTitle(QtGui.QApplication.translate("ShowContent", "Mostrar Conteúdo", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_begin_time.setText(QtGui.QApplication.translate("ShowContent", "Tempo:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ShowContent", "Comentário:", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_personalized.setText(QtGui.QApplication.translate("ShowContent", "Personalizado", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_choose_icon.setText(QtGui.QApplication.translate("ShowContent", "Escolher Ícone", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ShowContent", "Ícone de Interatividade", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ShowContent", "Ícone deve aparecer:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ShowContent", "Íconde deve ser exibido por:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_icon_before.setItemText(0, QtGui.QApplication.translate("ShowContent", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_icon_before.setItemText(1, QtGui.QApplication.translate("ShowContent", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_icon_before.setItemText(2, QtGui.QApplication.translate("ShowContent", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_icon_before.setItemText(3, QtGui.QApplication.translate("ShowContent", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_icon_before.setItemText(4, QtGui.QApplication.translate("ShowContent", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_icon_before.setItemText(5, QtGui.QApplication.translate("ShowContent", "15", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_icon_duration.setItemText(0, QtGui.QApplication.translate("ShowContent", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_icon_duration.setItemText(1, QtGui.QApplication.translate("ShowContent", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_icon_duration.setItemText(2, QtGui.QApplication.translate("ShowContent", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_icon_duration.setItemText(3, QtGui.QApplication.translate("ShowContent", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_icon_duration.setItemText(4, QtGui.QApplication.translate("ShowContent", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_icon_duration.setItemText(5, QtGui.QApplication.translate("ShowContent", "15", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ShowContent", "segundo(s) antes.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ShowContent", "segundo(s).", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_tr.setText(QtGui.QApplication.translate("ShowContent", "Canto Superior Direito", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ShowContent", "Posicionamento:", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_tl.setText(QtGui.QApplication.translate("ShowContent", "Canto Superior Esquerdo", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_br.setText(QtGui.QApplication.translate("ShowContent", "Canto Inferior Direito", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_bl.setText(QtGui.QApplication.translate("ShowContent", "Canto Inferior Esquerdo", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_free_position.setText(QtGui.QApplication.translate("ShowContent", "Personalizado", None, QtGui.QApplication.UnicodeUTF8))
        self.ckb_viber.setText(QtGui.QApplication.translate("ShowContent", "Alerta Vibratório", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_choose_icon_2.setText(QtGui.QApplication.translate("ShowContent", "Escolher Áudio", None, QtGui.QApplication.UnicodeUTF8))
        self.ckb_audio.setText(QtGui.QApplication.translate("ShowContent", "Alerta Sonoro", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_icon), QtGui.QApplication.translate("ShowContent", "Tipo de Alerta", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_skip.setText(QtGui.QApplication.translate("ShowContent", "Pular trecho", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_back.setText(QtGui.QApplication.translate("ShowContent", "Voltar 5 segundos", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_show.setText(QtGui.QApplication.translate("ShowContent", "Apenas exibir", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_back_to.setText(QtGui.QApplication.translate("ShowContent", "Voltar a um trecho específico", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_interaction), QtGui.QApplication.translate("ShowContent", "Tipo Interação", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_content), QtGui.QApplication.translate("ShowContent", "Tipos de Mídias", None, QtGui.QApplication.UnicodeUTF8))
        self.ckb_compulsory.setText(QtGui.QApplication.translate("ShowContent", "Apresentar o conteúdo de forma compulsória", None, QtGui.QApplication.UnicodeUTF8))
        self.ckb_pause_main_video.setText(QtGui.QApplication.translate("ShowContent", "Pausar o vídeo principal", None, QtGui.QApplication.UnicodeUTF8))
        self.ckb_allows_end_content.setText(QtGui.QApplication.translate("ShowContent", "Permitir finalizar o conteúdo complementar", None, QtGui.QApplication.UnicodeUTF8))
        self.ckb_show_on_mobile.setText(QtGui.QApplication.translate("ShowContent", "Enviar conteúdo para o celular", None, QtGui.QApplication.UnicodeUTF8))
        self.ckb_show_on_tv.setText(QtGui.QApplication.translate("ShowContent", "Exibir o conteúdo na TV", None, QtGui.QApplication.UnicodeUTF8))
        self.ckb_compulsory_2.setText(QtGui.QApplication.translate("ShowContent", "Apresentar o conteúdo de forma interativa", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_behavior), QtGui.QApplication.translate("ShowContent", "Comportamento", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancel.setText(QtGui.QApplication.translate("ShowContent", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_ok.setText(QtGui.QApplication.translate("ShowContent", "Ok", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
