#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
from ui.ui_AudioContent import Ui_AudioContent
from VolumeControl import VolumeControl
from AudioPlayer import AudioPlayer


class AudioContent(QtGui.QDialog):
    def __init__(self, parent=None):
        super(AudioContent, self).__init__(parent)
        self.ui = Ui_AudioContent()
        self.ui.setupUi(self)
        
        self.init_ui()
        self.show()
        
    def init_ui(self):
        self.volume_control = VolumeControl(self.ui.volume_control_widget)
        self.audio_player = AudioPlayer(self.ui.audio_player_widget)
        
def main():
    import sys
    app = QtGui.QApplication(sys.argv)    
    vp = AudioContent()
    vp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()