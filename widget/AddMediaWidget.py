#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
from ui.ui_AddMediaWidget import Ui_AddMediaWidget
import os
import model
HOME_DIRECTORY = os.getenv('USERPROFILE') or os.getenv('HOME')


class AddMediaWidget(QtGui.QDialog):
    def __init__(self, parent=None):
        super(AddMediaWidget, self).__init__(parent)
        self.ui = Ui_AddMediaWidget()
        self.ui.setupUi(self)
        
        self.init_ui()
        self.show()
        
    def init_ui(self):
        pass
        
def main():
    import sys
    app = QtGui.QApplication(sys.argv)    
    vp = AddMediaWidget()
    vp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()