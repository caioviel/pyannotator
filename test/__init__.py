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


def test():
    import sys
    app = QtGui.QApplication(sys.argv)
    myItem = MyItem()
    item = QtGui.QListWidgetItem()
    item.setSizeHint(QtCore.QSize(40,160))
    myList = QtGui.QListWidget()
    myList.addItem(item)
    myList.setItemWidget(item, myItem)
    myList.show()
    
    sys.exit(app.exec_())
        
if __name__ == "__main__":
    test()