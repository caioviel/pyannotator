# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PreviewWidget.ui'
#
# Created: Sun Feb  3 15:09:41 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_PreviewWidget(object):
    def setupUi(self, PreviewWidget):
        PreviewWidget.setObjectName("PreviewWidget")
        PreviewWidget.resize(967, 722)
        self.webView = QtWebKit.QWebView(PreviewWidget)
        self.webView.setGeometry(QtCore.QRect(10, 10, 951, 701))
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")

        self.retranslateUi(PreviewWidget)
        QtCore.QMetaObject.connectSlotsByName(PreviewWidget)

    def retranslateUi(self, PreviewWidget):
        PreviewWidget.setWindowTitle(QtGui.QApplication.translate("PreviewWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))

from PySide import QtWebKit
