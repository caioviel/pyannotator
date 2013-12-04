#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ui.ui_VideoContent import Ui_VideoContent
from VideoPlayer import VideoPlayer
from PyQt4 import QtGui, QtCore
from LayoutSelector import LayoutSelector
from VolumeControl import VolumeControl
import model
import os
HOME_DIRECTORY = os.getenv('USERPROFILE') or os.getenv('HOME')

class VideoContent(QtGui.QDialog):
    def __init__(self, project=None, content=None, parent=None):
        super(VideoContent, self).__init__(parent)
        self.project = project
        self.content = content
        self.result = None
        
        self.ui = Ui_VideoContent()
        self.ui.setupUi(self)
        
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
        self.ui.tabs.setCurrentIndex(0)
        
        self.ui.btn_choose_video.clicked.connect(self.choose_video)
        
        #Tab 0
        player_holder = self.ui.player_holder
        layout = QtGui.QVBoxLayout()
        self.video_player = VideoPlayer()
        layout.addWidget(self.video_player)
        player_holder.setLayout(layout)       
        
        #Tab 1
        tab = self.ui.tab_position
        self.layout_selector = LayoutSelector(parent=tab)
        
        #Tab 2
        tab = self.ui.tab_behavior
        #self.ui.volume_control_widget.resize(800,800)
        self.volume_control = VolumeControl(tab)
        #self.volume_control.show()
        
        
    @QtCore.pyqtSlot()
    def choose_video(self):
        path = QtGui.QFileDialog.getOpenFileName(self, 
                                                 u'Selecione um vídeo',
                                                 HOME_DIRECTORY,
                                                 model.CONTENT_TYPES[model.Media.VIDEO])
        if path == None:
            return
        
        
        
        self.video_path = path
        vp = self.video_player
        self.ui.txt_media_name.clear()
        self.ui.txt_media_name.appendPlainText(path)
        
        vp.load_video(path)
        
  
        
def main():
    import sys
    app = QtGui.QApplication(sys.argv)    
    vp = VideoContent()
    vp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()