#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Nov 16, 2013

@author: caioviel
'''

from ui.ui_TextContent import Ui_TextContent
from LayoutSelector import LayoutSelector
from PyQt4 import QtGui, QtCore

class TextContent(QtGui.QDialog):
    def __init__(self, text_content=None, parent=None):
        super(TextContent, self).__init__(parent)
        self.ui = Ui_TextContent()
        self.ui.setupUi(self)
        self.text_content = text_content
        self.align_array = [QtCore.Qt.AlignLeft, QtCore.Qt.AlignCenter, QtCore.Qt.AlignRight]
        self.text_alligment = QtCore.Qt.AlignLeft
        
        self.bg_color = QtGui.QColor(QtCore.Qt.white)
        self.font_color = QtGui.QColor(QtCore.Qt.black)
        self.current_font = self.ui.textEdit.font()
        self.transparency_bg = False
        self.text_content = ""
        
        if text_content is not None:
            self.load_content()
        
        self.init_ui()
            
    def load_content(self):
        pass

    def init_ui(self):
        self.layout_selector = LayoutSelector(self.ui.layout_selection_holder)
        
        lbl_content = self.layout_selector.lbl_content
        lbl_content.resize(self.layout_selector.width(),50)
        self.update_text()
        
        self.ui.btn_bg_color.clicked.connect(self.select_bg_color)
        self.ui.btn_font_color.clicked.connect(self.select_font_color)
        self.ui.btn_Font.clicked.connect(self.select_font)
        self.ui.ckb_transparency.stateChanged.connect(self.transparency_selected)
        self.ui.btn_reset_layout.clicked.connect(self.reset_layout)
        self.ui.cmb_alligment.currentIndexChanged.connect(self.allign_selected)
        self.ui.textEdit.textChanged.connect(self.text_changes)
    
    @QtCore.pyqtSlot()
    def text_changes(self):
        text = self.ui.textEdit.toPlainText()
        if text != self.text_content:
            self.text_content = text
            self.update_text()
        
        
    @QtCore.pyqtSlot(int)
    def allign_selected(self, index):
        self.text_alligment = self.align_array[index]
        self.update_text()
        
    @QtCore.pyqtSlot(int)
    def transparency_selected(self, state):
        if state == QtCore.Qt.Checked:
            self.transparency_bg = True
        elif state == QtCore.Qt.Unchecked:
            self.transparency_bg = False
            
        self.update_text()
        
    @QtCore.pyqtSlot()
    def reset_layout(self):
        self.layout_selector.reset_position()
        lbl_content = self.layout_selector.lbl_content
        lbl_content.resize(self.layout_selector.width(),50)

    @QtCore.pyqtSlot()
    def select_bg_color(self):
        color = QtGui.QColorDialog.getColor(self.bg_color, self)
        self.bg_color = color
        self.ui.lbl_bg_color.setStyleSheet("background-color: rgb"+str(self.bg_color.getRgb())+";")
        self.update_text()
    
    @QtCore.pyqtSlot()
    def select_font_color(self):
        color = QtGui.QColorDialog.getColor(self.bg_color, self)
        self.font_color = color
        self.ui.lbl_font_color.setStyleSheet("background-color: rgb"+str(self.font_color.getRgb())+";")
        self.update_text()
    
    @QtCore.pyqtSlot()
    def select_font(self):
        font, ok = QtGui.QFontDialog.getFont(self.ui.textEdit.font(), self)
        if ok:
            self.current_font = font
            self.update_text()

    @QtCore.pyqtSlot()
    def update_text(self):
        self.ui.textEdit.setFont(self.current_font)
        self.ui.textEdit.setStyleSheet("background-color: rgb"+str(self.bg_color.getRgb())+";"+\
                                       "color: rgb"+str(self.font_color.getRgb())+";")
        self.ui.textEdit.setAlignment(self.text_alligment)
        
        lbl_content = self.layout_selector.lbl_content
        lbl_content.setFont(self.current_font)
        lbl_content.setAlignment(QtCore.Qt.AlignBottom)
        lbl_content.setAlignment(self.text_alligment)
        
        if self.transparency_bg:
            lbl_content.setStyleSheet("background-color: rgba(0,0,0,0);"+\
                                       "color: rgb"+str(self.font_color.getRgb())+";")
            
        else:
            lbl_content.setStyleSheet("background-color: rgb"+str(self.bg_color.getRgb())+";"+\
                                       "color: rgb"+str(self.font_color.getRgb())+";")
        
        if self.ui.textEdit.toPlainText() == "":
            lbl_content.setText(u"Conteúdo Adicional")
        else:
            lbl_content.setText(self.ui.textEdit.toPlainText())
        
def main():
    import sys
    app = QtGui.QApplication(sys.argv)    
    tc = TextContent()
    tc.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()