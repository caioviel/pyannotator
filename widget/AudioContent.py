#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
from ui.ui_AudioContent import Ui_AudioContent
from VolumeControl import VolumeControl
from AudioPlayer import AudioPlayer
import model
import os
import util
HOME_DIRECTORY = os.getenv('USERPROFILE') or os.getenv('HOME')


class AudioContent(QtGui.QDialog):
    def __init__(self, project=None, annotation=None, content=None, parent=None):
        super(AudioContent, self).__init__(parent)
        
        self.project = project
        self.annotation = annotation
        self.content = content
        self.result = None
        
        self.ui = Ui_AudioContent()
        self.ui.setupUi(self)
        
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
                self.audio_path = self.content.filename
                self.audio_player.load_audio(unicode(self.audio_path))
                
            if self.content.main_video_volume is not None:
                self.volume_control.ui.slider_mp.setValue(self.content.main_video_volume)
                
            if self.content.media_volume is not None:
                self.volume_control.ui.slider_ac.setValue(self.content.media_volume)
                
    
    def init_ui(self):
        self.setFixedSize(self.size())
        self.volume_control = VolumeControl(self.ui.volume_control_widget)
        self.audio_player = AudioPlayer(parent=self.ui.audio_player_widget)
        
        self.ui.btn_choose_audio.clicked.connect(self.choose_audio)
        
        self.ui.time_begin.timeChanged.connect(self.calc_duration)
        self.ui.time_end.timeChanged.connect(self.calc_duration)
        
        self.ui.btn_ok.clicked.connect(self.ok_pressed)
        self.ui.btn_cancel.clicked.connect(self.cancel_pressed)
        
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
        finalpath = util.copy_to_directory(self.project, filename)
        showtime = util.qtime_to_sec(self.ui.time_begin.time())
        duration = util.qtime_to_sec(self.ui.time_end.time()) - showtime
        audio_content = None
        if self.content is None:
            audio_content = model.Audio(filename, finalpath, showtime)
            audio_content.duration = duration
        else:
            audio_content = self.content
            audio_content.id = filename
            audio_content.filename = finalpath
            audio_content.showtime = showtime
            audio_content.duration = duration

        audio_content.main_video_volume = self.volume_control.ui.slider_mp.value()
        audio_content.media_volume = self.volume_control.ui.slider_ac.value()
            
        self.result = audio_content
        
        self.close()
    
    @QtCore.pyqtSlot()
    def cancel_pressed(self):
        self.close()
        
    @QtCore.pyqtSlot()
    def choose_audio(self):
        path = QtGui.QFileDialog.getOpenFileName(self, 
                                                 u'Selecione um áudio',
                                                 HOME_DIRECTORY,
                                                 model.CONTENT_TYPES[model.Media.AUDIO])
        if path == None:
            return
        
        
        
        self.audio_path = path
        ap = self.audio_player
        self.ui.txt_media_name.clear()
        self.ui.txt_media_name.appendPlainText(path)
        
        ap.load_audio(unicode(path))
        
def main():
    import sys
    app = QtGui.QApplication(sys.argv)    
    vp = AudioContent()
    vp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()