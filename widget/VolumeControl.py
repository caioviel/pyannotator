#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
from ui.ui_VolumeControl import Ui_VolumeControl

class VolumeControl(QtGui.QWidget):
    def __init__(self, parent=None):
        super(VolumeControl, self).__init__(parent)
        self.ui = Ui_VolumeControl()
        self.ui.setupUi(self)
        self.show()
        
def main():
    import sys
    app = QtGui.QApplication(sys.argv)    
    vp = VolumeControl()
    vp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()