# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/MediaListItem.ui'
#
# Created: Thu Dec 12 11:39:06 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MediaListItem(object):
    def setupUi(self, MediaListItem):
        MediaListItem.setObjectName(_fromUtf8("MediaListItem"))
        MediaListItem.resize(219, 45)
        self.lbl_content_icon = QtGui.QLabel(MediaListItem)
        self.lbl_content_icon.setGeometry(QtCore.QRect(0, 10, 41, 31))
        self.lbl_content_icon.setText(_fromUtf8(""))
        self.lbl_content_icon.setPixmap(QtGui.QPixmap(_fromUtf8(":/m/audio.png")))
        self.lbl_content_icon.setScaledContents(True)
        self.lbl_content_icon.setObjectName(_fromUtf8("lbl_content_icon"))
        self.lbl_description = QtGui.QLabel(MediaListItem)
        self.lbl_description.setGeometry(QtCore.QRect(50, 10, 181, 31))
        self.lbl_description.setObjectName(_fromUtf8("lbl_description"))

        self.retranslateUi(MediaListItem)
        QtCore.QMetaObject.connectSlotsByName(MediaListItem)

    def retranslateUi(self, MediaListItem):
        MediaListItem.setWindowTitle(QtGui.QApplication.translate("MediaListItem", "Mídia", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_description.setText(QtGui.QApplication.translate("MediaListItem", "De 00:00:00 até 00:00:00", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
