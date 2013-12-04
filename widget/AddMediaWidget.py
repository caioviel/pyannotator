#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
from ui.ui_AddMediaWidget import Ui_AddMediaWidget
import os
import model
HOME_DIRECTORY = os.getenv('USERPROFILE') or os.getenv('HOME')

from TextContent import TextContent
from VideoContent import VideoContent
from ImageContent import ImageContent
from AudioContent import AudioContent


class AddMediaWidget(QtGui.QDialog):
    def __init__(self, parent=None):
        super(AddMediaWidget, self).__init__(parent)
        self.ui = Ui_AddMediaWidget()
        self.ui.setupUi(self)
        
        self.init_ui()
        self.show()
        
    def init_ui(self):
        self.ui.btn_audio.clicked.connect(self.add_audio)
        self.ui.btn_image.clicked.connect(self.add_image)
        self.ui.btn_video.clicked.connect(self.add_video)
        self.ui.btn_text.clicked.connect(self.add_text)
        self.ui.btn_slides.clicked.connect(self.add_slides)
        
        self.ui.btn_slides.setEnabled(False)
        
    @QtCore.pyqtSlot()
    def add_audio(self):
        myclass = AudioContent(self)
        myclass.exec_()
        
    @QtCore.pyqtSlot()
    def add_image(self):
        myclass = ImageContent(self)
        myclass.exec_()
        
    @QtCore.pyqtSlot()
    def add_video(self):
        myclass = VideoContent(self)
        myclass.exec_()
        
    @QtCore.pyqtSlot()
    def add_text(self):
        myclass = TextContent(self)
        myclass.exec_()
        
    @QtCore.pyqtSlot()
    def add_slides(self):
        print 'add add_slides'
        
def main():
    import sys
    app = QtGui.QApplication(sys.argv)    
    vp = AddMediaWidget()
    vp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()