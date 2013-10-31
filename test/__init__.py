#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore

class MyItem(QtGui.QWidget):
    
    def __init__(self):
        super(MyItem, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        label1 = QtGui.QLabel('Zetcode', self)
        label1.move(15, 10)

        label2 = QtGui.QLabel('tutorials', self)
        label2.move(35, 40)
        
        label3 = QtGui.QLabel('for programmers', self)
        label3.move(55, 70)        
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')    
        self.show()

from widget.WaitingDialog import WaitingDialog
 
def test():
    import sys
    app = QtGui.QApplication(sys.argv)
    dialog = WaitingDialog()
    dialog.show()
    
    
    sys.exit(app.exec_())
        
if __name__ == "__main__":
    test()