#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Feb 3, 2013

@author: caioviel
'''
from model import Annotation, CONTENT_TYPES
from PySide import QtGui, QtCore
from PySide.phonon import Phonon
from ui.ui_MainProjectWidget import Ui_MainProjectWidget
import os
from model.InformationAnnotation import InformationAnnotationWidget, InformationAnnotation

class MainProjectWidget(QtGui.QWidget):
    
    def __init__(self, parent=None):
        super(MainProjectWidget, self).__init__(parent)
        self.ui = Ui_MainProjectWidget()
        self.ui.setupUi(self)
        self.project_diretory = os.getenv('USERPROFILE') or os.getenv('HOME')
        self.main_video_path = None
        self.is_editing_time = False
        
        self.init_ui()
        
        self.show()
        
    def eventFilter(self, myObject, event):
        if myObject == self.ui.time_edit:
            if event.type() == QtCore.QEvent.FocusIn:
                self.timer_focus_in()
            elif event.type() == QtCore.QEvent.FocusOut:
                pass
            
        return False
        
    
    def init_ui(self):
        player = self.ui.video_player
        
        self.ui.btn_choose_video.clicked.connect(self.choose_video)
        self.ui.btn_play.clicked.connect(self.start_playback)
        self.ui.btn_stop.clicked.connect(self.stop_playback)
        self.ui.btn_pause.clicked.connect(self.pause_playback)
        
        self.ui.btn_add_annotation.clicked.connect(self.add_annotation)
        
        player.mediaObject().tick.connect(self.update_time_edit)
        self.ui.time_edit.timeChanged.connect(self.editing_time)
        self.ui.time_edit.installEventFilter(self)
        
    @QtCore.Slot()
    def add_annotation(self):
        self.pause_playback()
        annotation = InformationAnnotation('MyId')
        annotation.notification_icon_timestamp = self.ui.time_edit.time()
        self.widget = InformationAnnotationWidget(annotation, self)
        #self.widget.setWindowModality(QtCore.Qt.ApplicationModal)
        #self.widget.setModal(True)
        self.widget.show()
        #self.setEnabled(False)
        
    @QtCore.Slot(int)
    def update_time_edit(self, time):
        if not self.is_editing_time:
            time_edit = self.ui.time_edit
            time_edit.setTime(QtCore.QTime().addMSecs(time))
        
        
    @QtCore.Slot()
    def start_playback(self):
        player = self.ui.video_player
        player.play()
        self.ui.btn_pause.setVisible(True)
        self.ui.btn_play.setVisible(False)
        self.ui.btn_stop.setEnabled(True)
        self.is_editing_time = False
        
    
    @QtCore.Slot(QtCore.QTime)
    def editing_time(self, time):
        if self.is_editing_time:
            total_time = self.ui.video_player.mediaObject().totalTime()
            max_time = QtCore.QTime(0,0,0).addMSecs(total_time)
            self.ui.time_edit.setTimeRange(QtCore.QTime(0,0,0), max_time)
            
            
            msec = time.hour()
            msec = time.minute() + msec*60
            msec = time.second() + msec*60
            msec = msec*1000 + time.msec()
            self.ui.video_player.seek(msec)
            
            
    def timer_focus_in(self):
        self.pause_playback()
        self.is_editing_time = True
        
    
    @QtCore.Slot()
    def stop_playback(self):
        player = self.ui.video_player
        player.stop()
        self.ui.btn_stop.setEnabled(False)
        self.ui.btn_pause.setVisible(False)
        self.ui.btn_play.setVisible(True)
    
    @QtCore.Slot()
    def pause_playback(self):
        player = self.ui.video_player
        player.pause()
        self.ui.btn_pause.setVisible(False)
        self.ui.btn_play.setVisible(True)
        
    
    @QtCore.Slot()
    def choose_video(self):
        path, _ = QtGui.QFileDialog.getOpenFileName(self, 
                                                 u'Selecione o Vídeo Principal',
                                                 self.project_diretory,
                                                 CONTENT_TYPES[Annotation.VIDEO])
        if path == None:
            return
        
        
        self.main_video_path = path           
        player = self.ui.video_player
        self.ui.txt_main_video.clear()
        self.ui.txt_main_video.appendPlainText(path)
        
        player.stop()
        media_source = Phonon.MediaSource(path)
        player.load( media_source )
        self.ui.seek_slider.setMediaObject(player.mediaObject())
        self.ui.volume_slider.setAudioOutput(player.audioOutput())
        
        player.setVisible(True)
        self.ui.seek_slider.setVisible(True)
        self.ui.volume_slider.setVisible(True)
        self.ui.btn_play.setVisible(True)
        self.ui.btn_stop.setVisible(True)
        self.ui.btn_stop.setEnabled(False)

def test():
    import sys
    app = QtGui.QApplication(sys.argv)
    widget = MainProjectWidget()
    sys.exit(app.exec_())
        
if __name__ == "__main__":
    test()