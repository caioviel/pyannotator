from PyQt4 import QtGui, QtCore
import sys

class MovebleImage(QtGui.QLabel):
    def __init__(self, window):
        super(MovebleImage, self).__init__(window)
        self.offset = QtCore.QPoint()
        self.sizeGrip = QtGui.QSizeGrip(self)
        self.setWindowFlags(QtCore.Qt.SubWindow)
        
        
    def mousePressEvent(self, event):
        event.accept() # do not propagate
        if (self.isWindow()):
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

    



def main():
    app = QtGui.QApplication(sys.argv)
    widget = QtGui.QWidget()
    widget.resize(800,600)

    #dock = QtGui.QDockWidget("Hello world", widget)
    #dock.resize(40,40)
    
    image2 = MovebleImage(widget)
    image2.setScaledContents(True)
    image2.setGeometry(0, 0, 800, 600)
    image2.setPixmap(QtGui.QPixmap('/home/caioviel/Pictures/test.png'))
    
    
    image = MovebleImage(widget)
    image.setScaledContents(True)
    image.setGeometry(10, 10, 48, 48)
    image.setPixmap(QtGui.QPixmap('/home/caioviel/Pictures/play.png'))
    
    

    
    
    
    widget.show()
    

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()