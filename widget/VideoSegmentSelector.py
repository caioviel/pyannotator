'''
Created on Nov 16, 2013

@author: caioviel
'''

from PyQt4 import QtGui, QtCore
from VideoPlayer import VideoPlayer
from QxtSpanSlider import QxtSpanSlider
import time

class MyLabel(QtGui.QLabel):
    def __init__(self, parent = None):
        super(MyLabel, self).__init__(parent)
    
    CLICKED = QtCore.pyqtSignal()
    
    def mouseReleaseEvent(self, event):
        event.accept()
        self.CLICKED.emit()


class VideoSegmentSelector(QtGui.QWidget):
    '''
    classdocs
    '''
    def __init__(self, video_source, vrange, spam, parent=None):
        '''
        Constructor
        '''
        super(VideoSegmentSelector, self).__init__(parent)
        self.video_source = video_source
        self.range = vrange
        self.spam = spam
        self.init_ui()
        
    @QtCore.pyqtSlot()
    def go_to_segment_begin(self):
        begin_segment = self.slider.lowerValue
        self.player.seek(begin_segment)
    
    @QtCore.pyqtSlot()
    def go_to_segment_end(self):
        end_segment = self.slider.upperValue
        self.player.seek(end_segment)

    @QtCore.pyqtSlot(int)
    def update_left_image(self, value):
        print value
        self.player.pause()
        self.player.seek(value)
        self.lbl_img_left.setPixmap(self.player.get_pixmap())
        #self.lbl_img_left.repaint()
        
    @QtCore.pyqtSlot(int)
    def update_right_image(self, value):
        print value
        self.player.pause()
        self.player.seek(value)
        self.lbl_img_right.setPixmap(self.player.get_pixmap())
        #self.lbl_img_right.repaint()
        
    def init_ui(self):
        layout = QtGui.QVBoxLayout()
        self.setLayout(layout)
        
        self.player = VideoPlayer(self.video_source)
        layout.addWidget(self.player)
        
        self.slider = QxtSpanSlider()        
        self.slider.setRange(*self.range)
        self.slider.setSpan(*self.spam)
        self.slider.lowerPositionChanged.connect(self.update_left_image)
        self.slider.upperPositionChanged.connect(self.update_right_image)
        self.slider.setHandleMovementMode(QxtSpanSlider.NoOverlapping)
        
        layout.addWidget(self.slider)
        
        h_layout = QtGui.QHBoxLayout()
        layout.addLayout(h_layout)
        
        self.lbl_img_left = MyLabel()
        self.lbl_img_left.setFixedSize(280,158)
        self.lbl_img_left.setFrameStyle(3)
        self.lbl_img_left.setScaledContents(True)
        self.lbl_img_left.CLICKED.connect(self.go_to_segment_begin)
        h_layout.addWidget(self.lbl_img_left)
        
        self.lbl_img_right = MyLabel()
        self.lbl_img_right.setFixedSize(280,158)
        self.lbl_img_right.setFrameStyle(3)
        self.lbl_img_right.setScaledContents(True)
        self.lbl_img_right.CLICKED.connect(self.go_to_segment_end)
        h_layout.addWidget(self.lbl_img_right)
        
        self.resize(710,640)
        
        

def main():
    print QtCore.qVersion()
    print QtCore.PYQT_VERSION_STR
    
    
    import sys
    app = QtGui.QApplication(sys.argv)    
    vsl = VideoSegmentSelector('/home/caioviel/Videos/sample-480.mp4',
                               (0,7000), (0,7000))
    vsl.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()