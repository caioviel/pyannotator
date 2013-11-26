#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
from ui.ui_AudioContent import Ui_AudioContent
from VolumeControl import VolumeControl
from AudioPlayer import AudioPlayer
import model
import os
HOME_DIRECTORY = os.getenv('USERPROFILE') or os.getenv('HOME')


class AudioContent(QtGui.QDialog):
    def __init__(self, parent=None):
        super(AudioContent, self).__init__(parent)
        self.ui = Ui_AudioContent()
        self.ui.setupUi(self)
        
        self.init_ui()
        self.show()
        
    def init_ui(self):
        self.volume_control = VolumeControl(self.ui.volume_control_widget)
        self.audio_player = AudioPlayer(parent=self.ui.audio_player_widget)
        
        self.ui.btn_choose_audio.clicked.connect(self.choose_audio)
        
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
        
        ap.load_audio(str(path))
        
def main():
    import sys
    app = QtGui.QApplication(sys.argv)    
    vp = AudioContent()
    vp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()