from PySide import QtGui, QtCore
import sys

class DiagramScene(QtGui.QGraphicsScene):
    InsertItem, InsertLine, InsertText, MoveItem  = range(4)

    def __init__(self):
        super(DiagramScene, self).__init__()
        self.myLineColor = QtCore.Qt.black
        self.myMode = "Start"
        self.line = None
        rect = QtCore.QRectF(10,10,50,50)
        self.addRect(rect, QtGui.QPen(QtCore.Qt.black, 8))
        rect = QtCore.QRectF(3,3, 20,20)
        self.addRect(rect)
        self.setFont(QtGui.QFont('Times', 18))

    def mousePressEvent(self, mouseEvent):
        if (mouseEvent.button() == QtCore.Qt.LeftButton):
            if self.myMode == "Start":
                self.line = QtGui.QGraphicsLineItem(QtCore.QLineF(mouseEvent.scenePos(), mouseEvent.scenePos()))
                self.addItem(self.line)
        elif (mouseEvent.button() == QtCore.Qt.RightButton):
            self.addText("Hello")
        super(DiagramScene, self).mousePressEvent(mouseEvent)

    def mouseMoveEvent(self, mouseEvent):
        if self.line:
            newLine = QtCore.QLineF(self.line.line().p1(), mouseEvent.scenePos())
            self.line.setLine(newLine)

    def mouseReleaseEvent(self, mouseEvent):
        self.line = None
        super(DiagramScene, self).mouseReleaseEvent(mouseEvent)


def main():
    app = QtGui.QApplication(sys.argv)
    layout = QtGui.QHBoxLayout()
    view = QtGui.QGraphicsView(DiagramScene())
    layout.addWidget(view)
    widget = QtGui.QWidget()
    widget.setLayout(layout)
    widget.show()
    view.update()
    

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()