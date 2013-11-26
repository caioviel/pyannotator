#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
from ui.ui_ImageContent import Ui_ImageContent
from LayoutSelector import LayoutSelector
import model
import os
HOME_DIRECTORY = os.getenv('USERPROFILE') or os.getenv('HOME')

class ImageContent(QtGui.QWidget):
    def __init__(self, audio_source=None, begin_time=None, end_time=None, parent=None):
        super(ImageContent, self).__init__(parent)
        self.audio_source = audio_source
        self.begin_time = begin_time
        self.end_time = end_time
        
        self.ui = Ui_ImageContent()
        self.ui.setupUi(self)
        #self.lbl_image = self.ui.lbl_image
        self.init_ui()
        
    def init_ui(self):
        self.setFixedSize(self.size())
        
        self.ui.btn_choose_image.clicked.connect(self.choose_image)
    
        self.layout_selector = LayoutSelector(self.ui.layout_selector_widget)
        #self.lbl_image = self.layout_selector.lbl_content
        #self.lbl_image.setScaledContents(True)
        
    @QtCore.pyqtSlot()
    def choose_image(self):
        path = QtGui.QFileDialog.getOpenFileName(self, 
                                                 u'Selecione uma imagem',
                                                 HOME_DIRECTORY,
                                                 model.CONTENT_TYPES[model.Media.IMAGE])
        if path == None:
            return
        
        self.image_path = path
        self.ui.txt_media_name.clear()
        self.ui.txt_media_name.appendPlainText(path)
        self.layout_selector.load_image(path)
        
def main():
    import sys
    app = QtGui.QApplication(sys.argv)    
    vp = ImageContent()
    vp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()