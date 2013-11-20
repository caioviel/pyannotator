# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ProjectChooseWidget.ui'
#
# Created: Sat Nov 16 18:39:26 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ProjectChooseWidget(object):
    def setupUi(self, ProjectChooseWidget):
        ProjectChooseWidget.setObjectName(_fromUtf8("ProjectChooseWidget"))
        ProjectChooseWidget.resize(735, 361)
        self.frame = QtGui.QFrame(ProjectChooseWidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 351, 341))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.lst_projects = QtGui.QListWidget(self.frame)
        self.lst_projects.setGeometry(QtCore.QRect(10, 30, 331, 241))
        self.lst_projects.setObjectName(_fromUtf8("lst_projects"))
        self.btn_open_project = QtGui.QPushButton(self.frame)
        self.btn_open_project.setGeometry(QtCore.QRect(177, 280, 161, 51))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/i/folder_open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_open_project.setIcon(icon)
        self.btn_open_project.setIconSize(QtCore.QSize(40, 40))
        self.btn_open_project.setObjectName(_fromUtf8("btn_open_project"))
        self.frame_2 = QtGui.QFrame(ProjectChooseWidget)
        self.frame_2.setGeometry(QtCore.QRect(370, 10, 351, 341))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label_2 = QtGui.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 101, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 66, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.txt_project_id = QtGui.QPlainTextEdit(self.frame_2)
        self.txt_project_id.setGeometry(QtCore.QRect(110, 10, 221, 31))
        self.txt_project_id.setObjectName(_fromUtf8("txt_project_id"))
        self.txt_project_name = QtGui.QPlainTextEdit(self.frame_2)
        self.txt_project_name.setGeometry(QtCore.QRect(70, 50, 261, 31))
        self.txt_project_name.setObjectName(_fromUtf8("txt_project_name"))
        self.txt_description_2 = QtGui.QPlainTextEdit(self.frame_2)
        self.txt_description_2.setGeometry(QtCore.QRect(10, 110, 331, 161))
        self.txt_description_2.setObjectName(_fromUtf8("txt_description_2"))
        self.btn_create_project = QtGui.QPushButton(self.frame_2)
        self.btn_create_project.setGeometry(QtCore.QRect(177, 280, 161, 51))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../../../Downloads/file_upload.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_create_project.setIcon(icon1)
        self.btn_create_project.setIconSize(QtCore.QSize(40, 40))
        self.btn_create_project.setObjectName(_fromUtf8("btn_create_project"))
        self.label_4 = QtGui.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 91, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(ProjectChooseWidget)
        QtCore.QMetaObject.connectSlotsByName(ProjectChooseWidget)

    def retranslateUi(self, ProjectChooseWidget):
        ProjectChooseWidget.setWindowTitle(QtGui.QApplication.translate("ProjectChooseWidget", "Selecionado Projeto", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ProjectChooseWidget", "Projetos Recentes:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_open_project.setText(QtGui.QApplication.translate("ProjectChooseWidget", "Abrir Projeto", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ProjectChooseWidget", "Identificador:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ProjectChooseWidget", "Nome:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_create_project.setText(QtGui.QApplication.translate("ProjectChooseWidget", "Criar Projeto", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ProjectChooseWidget", "Descrição:", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
