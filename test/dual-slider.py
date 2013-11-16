from PyQt4 import QtGui, QtCore
from QxtSpanSlider import QxtSpanSlider

import sys


def main():
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    w.resize(800,600)
    #b = QtGui.QPushButton(w)
    slider = QxtSpanSlider(w)
    slider.setRange(0, 100)
    slider.setSpan(30, 70)
    slider.resize(800,20)
    w.show()
    

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()