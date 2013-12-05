#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ui.ui_VideoContent import Ui_VideoContent
from VideoPlayer import VideoPlayer
from PyQt4 import QtGui, QtCore
from LayoutSelector import LayoutSelector
from VolumeControl import VolumeControl
import model
import os
import util
HOME_DIRECTORY = os.getenv('USERPROFILE') or os.getenv('HOME')

class VideoContent(QtGui.QDialog):
    def __init__(self, project=None, annotation=None, content=None, parent=None):
        super(VideoContent, self).__init__(parent)
        self.project = project
        self.content = content
        self.annotation = annotation
        self.result = None
        
        self.ui = Ui_VideoContent()
        self.ui.setupUi(self)
        
        #TODO:
        self.init_ui()
        self.load_content()
       
    def get_result(self):
        return self.result
            
    def load_content(self):
        if self.annotation is not None:
            self.ui.time_begin.setTime(self.annotation.annotation_time)
            
        if self.content is not None:
            begin = util.sec_to_qtime(self.content.showtime)
            
            self.ui.time_begin.setTime(begin)
            
            self.ui.time_end.setTime(begin.addSecs(self.content.duration))
            
            if self.content.filename is not None:
                self.ui.txt_media_name.appendPlainText(self.content.filename)
                self.video_path = self.content.filename
                self.video_player.load_video(unicode(self.video_path))
                
            if self.content.main_video_volume is not None:
                self.volume_control.ui.slider_mp.setValue(self.content.main_video_volume)
                
            if self.content.media_volume is not None:
                self.volume_control.ui.slider_ac.setValue(self.content.media_volume)
                
            if self.content.bondaries is not None:
                self.layout_selector.set_content_bondaires(
                                            self.content.bondaries)
            
            if self.content.resize_main_video is not None:
                self.layout_selector.set_main_video_bondaries(
                                            self.content.resize_main_video)
            
    @QtCore.pyqtSlot()
    def ok_pressed(self):
        filename = unicode(self.ui.txt_media_name.toPlainText())
        finalpath = util.copy_to_directory(self.project, filename)
        showtime = util.qtime_to_sec(self.ui.time_begin.time())
        duration = util.qtime_to_sec(self.ui.time_end.time()) - showtime
        video_content = None
        if self.content is None:
            video_content = model.Video(filename, finalpath, showtime)
            video_content.duration = duration
        else:
            video_content = self.content
            video_content.id = filename
            video_content.filename = finalpath
            video_content.showtime = showtime
            video_content.duration = duration
        video_content.bondaries = self.layout_selector.get_content_bondaries()
        
        if self.layout_selector.is_main_video_resized():
            video_content.resize_main_video = self.layout_selector.get_main_video_bondaries()
            
        video_content.main_video_volume = self.volume_control.ui.slider_mp.value()
        video_content.media_volume = self.volume_control.ui.slider_ac.value()
            
        self.result = video_content
        
        self.close()
    
    @QtCore.pyqtSlot()
    def cancel_pressed(self):
        self.close()
        
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
        
        self.ui.btn_ok.clicked.connect(self.ok_pressed)
        self.ui.btn_cancel.clicked.connect(self.cancel_pressed)
        
        self.ui.time_begin.timeChanged.connect(self.calc_duration)
        self.ui.time_end.timeChanged.connect(self.calc_duration)
        
        
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