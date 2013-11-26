#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
from ui.ui_AudioPlayer import Ui_AudioPlayer
from PyQt4.phonon import Phonon
import os

class AudioPlayer(QtGui.QWidget):
    def __init__(self, audio_source=None, begin_time=None, end_time=None, parent=None):
        super(AudioPlayer, self).__init__(parent)
        self.audio_source = audio_source
        self.begin_time = begin_time
        self.end_time = end_time
        
        self.ui = Ui_AudioPlayer()
        self.ui.setupUi(self)
        self.player = Phonon.VideoPlayer(self)
        self.player.setVisible(False)
        
        #self.player = self.ui.video_player
        self.init_ui()
        self.is_paused = False
        
        if audio_source is not None:
            self.load_audio(audio_source)
        
    def init_ui(self):
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
        
    def load_audio(self, audio_source):
        self.video_source = audio_source
        
        
        player = self.player
        player.stop()
        media_source = Phonon.MediaSource(audio_source)
        player.load( media_source )
        self.ui.seek_slider.setMediaObject(player.mediaObject())
        self.ui.volume_slider.setAudioOutput(player.audioOutput())
        
        self.ui.lbl_audio_description.setText(os.path.split(audio_source)[1])
        
        self.ui.btn_play.setEnabled(True)
        self.ui.btn_stop.setEnabled(True)
        self.ui.seek_slider.setEnabled(True)
        self.ui.volume_slider.setEnabled(True)
        
def main():
    import sys
    app = QtGui.QApplication(sys.argv)    
    vp = AudioPlayer('/home/caioviel/Music/audio.mp3')
    vp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()