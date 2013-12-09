#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ui.ui_VideoPlayer import Ui_VideoPlayer
from PyQt4 import QtGui, QtCore
from PyQt4.phonon import Phonon


class MySlider(Phonon.SeekSlider):
    mouse_released = QtCore.pyqtSignal(int) 
    
    def __init__(self, parent=None):
        super(MySlider, self).__init__(parent)
        
    def mouseReleaseEvent(self, mouseEvent):
        #print self.pos()
        self.mouse_released.emit(self.pos())
        


class VideoPlayer(QtGui.QWidget):
    def __init__(self, video_source=None, begin_time=None, end_time=None, parent=None):
        super(VideoPlayer, self).__init__(parent)
        self.ui = Ui_VideoPlayer()
        self.ui.setupUi(self)
        self.begin_time = begin_time
        self.end_time = end_time
        
        self.player = self.ui.video_player
        self.init_ui()
        self.is_paused = False
        
        if video_source is not None:
            self.load_video(video_source)
        
    def init_ui(self):
        self.ui.seek_slider = MySlider(self.ui.seek_slider_widget)
        self.ui.seek_slider.resize(self.ui.seek_slider_widget.size())
        
        self.ui.btn_pause.setVisible(False)
        self.ui.btn_play.setEnabled(False)
        self.ui.btn_stop.setEnabled(False)
        self.ui.seek_slider.setEnabled(False)
        self.ui.volume_slider.setEnabled(False)
        
        self.ui.btn_play.clicked.connect(self.play)
        self.ui.btn_stop.clicked.connect(self.stop)
        self.ui.btn_pause.clicked.connect(self.pause)
        
    @QtCore.pyqtSlot()
    def stop(self):
        self.player.stop()
        self.ui.btn_stop.setEnabled(False)
        self.ui.btn_pause.setVisible(False)
        self.ui.btn_play.setVisible(True)
        self.is_paused = False
    
    @QtCore.pyqtSlot()
    def play(self):            
        self.player.play()
        self.ui.btn_play.setVisible(False)
        self.ui.btn_stop.setEnabled(True)
        self.ui.btn_pause.setVisible(True)
    
    @QtCore.pyqtSlot()
    def pause(self):
        self.player.pause()
        self.ui.btn_play.setVisible(True)
        self.ui.btn_pause.setVisible(False)
    
    @QtCore.pyqtSlot(int)
    def seek(self, msec):
        self.player.seek(msec)
        
    def get_pixmap(self):
        return QtGui.QPixmap.grabWindow(self.player.videoWidget().winId())
    
    def load_video(self, video_source):
        self.video_source = video_source
        
        player = self.player
        player.stop()
        media_source = Phonon.MediaSource(video_source)
        player.load( media_source )
        
        self.ui.seek_slider.setMediaObject(player.mediaObject())
        self.ui.volume_slider.setAudioOutput(player.audioOutput())
        
        self.ui.btn_play.setEnabled(True)
        self.ui.btn_stop.setEnabled(True)
        self.ui.seek_slider.setEnabled(True)
        self.ui.volume_slider.setEnabled(True)
        
def main():
    import sys
    app = QtGui.QApplication(sys.argv)    
    vp = VideoPlayer('/home/caioviel/Videos/Videosgreentower.avi', begin_time=5000)
    vp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()