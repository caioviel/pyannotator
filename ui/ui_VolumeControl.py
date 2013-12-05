# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/VolumeControl.ui'
#
# Created: Thu Dec  5 17:41:18 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_VolumeControl(object):
    def setupUi(self, VolumeControl):
        VolumeControl.setObjectName(_fromUtf8("VolumeControl"))
        VolumeControl.resize(301, 237)
        self.lbl_vol_mp = QtGui.QLabel(VolumeControl)
        self.lbl_vol_mp.setGeometry(QtCore.QRect(-10, 0, 161, 61))
        self.lbl_vol_mp.setObjectName(_fromUtf8("lbl_vol_mp"))
        self.slider_mp = QtGui.QSlider(VolumeControl)
        self.slider_mp.setGeometry(QtCore.QRect(60, 70, 29, 151))
        self.slider_mp.setMaximum(100)
        self.slider_mp.setSliderPosition(50)
        self.slider_mp.setOrientation(QtCore.Qt.Vertical)
        self.slider_mp.setInvertedAppearance(False)
        self.slider_mp.setInvertedControls(False)
        self.slider_mp.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.slider_mp.setTickInterval(10)
        self.slider_mp.setObjectName(_fromUtf8("slider_mp"))
        self.lbl_vol_ac = QtGui.QLabel(VolumeControl)
        self.lbl_vol_ac.setGeometry(QtCore.QRect(140, 0, 161, 61))
        self.lbl_vol_ac.setObjectName(_fromUtf8("lbl_vol_ac"))
        self.slider_ac = QtGui.QSlider(VolumeControl)
        self.slider_ac.setGeometry(QtCore.QRect(210, 70, 29, 151))
        self.slider_ac.setMaximum(100)
        self.slider_ac.setProperty("value", 100)
        self.slider_ac.setSliderPosition(100)
        self.slider_ac.setOrientation(QtCore.Qt.Vertical)
        self.slider_ac.setInvertedAppearance(False)
        self.slider_ac.setInvertedControls(False)
        self.slider_ac.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.slider_ac.setTickInterval(10)
        self.slider_ac.setObjectName(_fromUtf8("slider_ac"))

        self.retranslateUi(VolumeControl)
        QtCore.QMetaObject.connectSlotsByName(VolumeControl)

    def retranslateUi(self, VolumeControl):
        VolumeControl.setWindowTitle(QtGui.QApplication.translate("VolumeControl", "Controle de Volume", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_vol_mp.setText(QtGui.QApplication.translate("VolumeControl", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Volume<br/>mídia principal:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_vol_ac.setText(QtGui.QApplication.translate("VolumeControl", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Volume<br/>conteúdo adicional:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

