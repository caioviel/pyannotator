from PySide import QtGui, QtCore
from ui_PreviewWidget import Ui_PreviewWidget


class Previewidget(QtGui.QWidget):
    
    def __init__(self, parent=None):
        super(Previewidget, self).__init__(parent)
        self.ui = Ui_PreviewWidget()
        self.ui.setupUi(self)
        self.ui.webView.setUrl('http://webncl.org')
        self.show()
        
        
def test():
    import sys
    app = QtGui.QApplication(sys.argv)
    widget = Previewidget()
    sys.exit(app.exec_())
        
if __name__ == "__main__":
    test()