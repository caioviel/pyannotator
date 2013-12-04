#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
from ui.ui_ImageContent import Ui_ImageContent
from LayoutSelector import LayoutSelector
import model
import os
import util
HOME_DIRECTORY = os.getenv('USERPROFILE') or os.getenv('HOME')

class ImageContent(QtGui.QDialog):
    def __init__(self, project=None, content=None, parent=None):
        super(ImageContent, self).__init__(parent)
        self.project = project
        self.content = content
        self.result = None
        
        self.ui = Ui_ImageContent()
        self.ui.setupUi(self)
        #self.lbl_image = self.ui.lbl_image
        #TODO:
        if content is not None:
            self.load_content()
        
        self.init_ui()
        
    def get_result(self):
        return self.result
            
    def load_content(self):
        pass
        
    def init_ui(self):
        self.setFixedSize(self.size())
        
        self.ui.btn_choose_image.clicked.connect(self.choose_image)
    
        self.layout_selector = LayoutSelector(parent=self.ui.layout_selector_widget)
        #self.lbl_image = self.layout_selector.lbl_content
        #self.lbl_image.setScaledContents(True)
        
        self.ui.btn_ok.clicked.connect(self.ok_pressed)
        self.ui.btn_cancel.clicked.connect(self.cancel_pressed)
        
        self.ui.time_begin.timeChanged.connect(self.calc_duration)
        self.ui.time_end.timeChanged.connect(self.calc_duration)
        
    @QtCore.pyqtSlot()   
    def calc_duration(self):
        begin = util.qtime_to_sec(self.ui.time_begin.time())
        end = util.qtime_to_sec(self.ui.time_end.time())
        
        self.ui.txt_duration.clear()
        if end >= begin:
            duration = end - begin
            self.ui.txt_duration.appendPlainText(str(duration))
        else:
            self.ui.txt_duration.appendPlainText('---')
    
    @QtCore.pyqtSlot()
    def ok_pressed(self):
        filename = unicode(self.ui.txt_media_name.toPlainText())
        #finalpath = util.copy_to_directory(self.project, filename)
        finalpath = filename
        showtime = util.qtime_to_sec(self.ui.time_begin.time())
        duration = util.qtime_to_sec(self.ui.time_end.time()) - showtime
        image_content = model.Image(filename, finalpath, showtime, duration)
        image_content.bondaries = self.layout_selector.get_content_bondaries()
        
        if self.layout_selector.is_main_video_resized():
            image_content.resize_main_video = self.layout_selector.get_main_video_bondaries()
            
        self.result = image_content
        
        self.close()
    
    @QtCore.pyqtSlot()
    def cancel_pressed(self):
        self.close()
    
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