#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
from ui.ui_DialogCopyFiles import Ui_DialogCopyFiles
import os
import threading
import shutil
HOME_DIRECTORY = os.getenv('USERPROFILE') or os.getenv('HOME')

class DialogCopyFiles(QtGui.QDialog, threading.Thread):
    def __init__(self, src, dst, parent=None):
        threading.Thread.__init__(self)
        QtGui.QDialog.__init__(self, parent)
        self.src = src
        self.dst = dst
        
        self.ui = Ui_DialogCopyFiles()
        self.ui.setupUi(self)
        
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(200)
        self.timer.timeout.connect(self.update_bar)
        self.setFixedSize(self.size())
    
    @QtCore.pyqtSlot()
    def update_bar(self):
        self.ui.progressBar.setValue(self.ui.progressBar.value()+5)
    
    def run(self):
        self.timer.start()
        try:
            shutil.copy(self.src, self.dst)
            print 'copy finished'
        except:
            print 'error copying'
        self.timer.stop()
        self.close()
        
def main():
    import sys
    app = QtGui.QApplication(sys.argv)    
    vp = DialogCopyFiles(None, None)
    vp.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
    