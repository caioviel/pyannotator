from ui.ui_WaitingDialog import Ui_WaitingDialog
from PySide import QtGui, QtCore

class WaitingDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(WaitingDialog, self).__init__(parent)
        self.ui = Ui_WaitingDialog()
        self.ui.setupUi(self)