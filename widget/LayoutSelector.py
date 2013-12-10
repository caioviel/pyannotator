#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Nov 16, 2013

@author: caioviel
'''

from PyQt4 import QtGui, QtCore

from model import Bondaries

class MovebleLabel(QtGui.QLabel):
    def __init__(self, text=None, parent=None):
        super(MovebleLabel, self).__init__(text, parent)
        self.offset = QtCore.QPoint()
        self.sizeGrip = QtGui.QSizeGrip(self)
        self.setWindowFlags(QtCore.Qt.SubWindow)
        
        
    def mousePressEvent(self, event):
        event.accept() # do not propagate
        if (self.isWindow()):
            print 'isWinow'
            self.offset = event.globalPos() - self.pos()
        else:
            self.offset = event.pos()
            
    def mouseMoveEvent(self, event):
        event.accept() # do not propagate
        if (self.isWindow()):
            self.move(event.globalPos() - self.offset)
        else:
            self.move(self.mapToParent(event.pos() - self.offset))
            
    def mouseReleaseEvent(self, event):
        event.accept() # do not propagate
        self.offset = QtCore.QPoint()

class LayoutSelector(QtGui.QWidget):
    def __init__(self, base_size=(700, 394), base_pos=(8,20), parent=None):
        super(LayoutSelector, self).__init__(parent)
        self.base_size = base_size
        self.base_pos = base_pos
        self.init_ui()
        
    def init_ui(self):
        self.resize(721,531)
        self.lbl_screen = QtGui.QLabel("Tela", self)
        self.lbl_screen.resize(*self.base_size)
        self.lbl_screen.move(*self.base_pos)
        self.lbl_screen.setStyleSheet('background-color: rgb(0, 0, 0); \
                                        border-color: rgb(255, 255, 255);\
                                        font: 75 28pt "Ubuntu";\
                                        color: rgb(255, 255, 127);')
        self.lbl_screen.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_screen.setText("Tela")
        
        
        self.lbl_main_video = MovebleLabel("Vídeo Principal", self)
        self.lbl_main_video.resize(*self.base_size )
        self.lbl_main_video.move(*self.base_pos)
        self.lbl_main_video.setStyleSheet('background-color: rgb(61, 60, 59);; \
                                        border-color: rgb(255, 255, 255);\
                                        font: 75 28pt "Ubuntu";\
                                        color: rgb(255, 255, 127);')
        self.lbl_main_video.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_main_video.setWordWrap(True)
        self.lbl_main_video.setText(u"Vídeo Principal")
        
        
        self.lbl_content = MovebleLabel(u"Conteúdo Complementar", self)
        self.lbl_content.resize(200, 150)
        self.lbl_content.move(*self.base_pos)
        self.lbl_content.setStyleSheet('background-color: rgb(255, 255, 0);\
                                            border-color: rgb(255, 255, 255);\
                                            font: 75 16pt "Ubuntu";\
                                            color: rgb(0, 0, 0);')
        self.lbl_content.setScaledContents(True)
        self.lbl_content.setMinimumSize(1, 1)
        self.lbl_content.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_content.setWordWrap(True)
        self.lbl_content.setText(u"Conteúdo Complementar")
        
        self.btn_reset_position = QtGui.QPushButton(u"Resetar Posição", self)
        self.btn_reset_position.clicked.connect(self.reset_position)
        self.btn_reset_position.move(580, 460)
        
        
    def load_image(self, path):
        self.lbl_content.setScaledContents(True)
        self.lbl_content.setPixmap(QtGui.QPixmap(path))
        self.lbl_content.setStyleSheet('background-color: rgba(0, 0, 0, 0);')
        self.sizeGrip = QtGui.QSizeGrip(self)
        
        
    def is_main_video_resized(self):
        qsize = self.lbl_main_video.size()
        size = (qsize.width(), qsize.height())
        return size != self.base_size
    
    def get_main_video_bondaries(self):
        bound = Bondaries()
        qpoint = self.lbl_main_video.pos()
        qsize = self.lbl_main_video.size()
        bound.width = qsize.width()
        bound.height = qsize.height()
        bound.left = qpoint.x() - self.base_pos[0]
        bound.top = qpoint.y() - self.base_pos[1]
        bound.screen_width, bound.screen_height = self.base_size
        
        return bound
    
    def get_content_bondaries(self):
        bound = Bondaries()
        qpoint = self.lbl_content.pos()
        qsize = self.lbl_content.size()
        bound.width = qsize.width()
        bound.height = qsize.height()
        bound.left = qpoint.x() - self.base_pos[0]
        bound.top = qpoint.y() - self.base_pos[1]
        bound.screen_width, bound.screen_height = self.base_size
        
        return bound
    
    def set_content_bondaires(self, bound):
        self.lbl_content.resize(bound.width, bound.height)
        self.lbl_content.move(bound.left + self.base_pos[0],
                                 bound.top + self.base_pos[1])
    
    def set_main_video_bondaries(self, bound):
        self.lbl_main_video.resize(bound.width, bound.height)
        self.lbl_main_video.move(bound.left + self.base_pos[0],
                                 bound.top + self.base_pos[1])
        
        
    
    
    @QtCore.pyqtSlot()
    def reset_position(self):
        print self.is_main_video_resized()
        print self.get_main_video_bondaries()
        print self.get_content_bondaries()
        
        
        self.lbl_main_video.resize(700, 394)
        self.lbl_main_video.move(8,20)
        self.lbl_content.resize(200, 150)
        self.lbl_content.move(8,20)

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)    
    vp = LayoutSelector()
    vp.load_image('/home/caioviel/Pictures/icon_no.png')
    vp.show()
    sys.exit(app.exec_())