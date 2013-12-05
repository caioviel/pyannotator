# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/PreviewWidget.ui'
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

class Ui_PreviewWidget(object):
    def setupUi(self, PreviewWidget):
        PreviewWidget.setObjectName(_fromUtf8("PreviewWidget"))
        PreviewWidget.resize(967, 722)
        self.webView = QtWebKit.QWebView(PreviewWidget)
        self.webView.setGeometry(QtCore.QRect(10, 10, 951, 701))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))

        self.retranslateUi(PreviewWidget)
        QtCore.QMetaObject.connectSlotsByName(PreviewWidget)

    def retranslateUi(self, PreviewWidget):
        PreviewWidget.setWindowTitle(QtGui.QApplication.translate("PreviewWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
