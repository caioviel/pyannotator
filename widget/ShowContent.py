#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from ui.ui_ShowContent import Ui_ShowContent
from AddMediaWidget import AddMediaWidget

import model
import os
HOME_DIRECTORY = os.getenv('USERPROFILE') or os.getenv('HOME')
from LayoutSelector import *

class ShowContent(QtGui.QDialog):
    def __init__(self, parent=None):
        super(ShowContent, self).__init__(parent)
        self.ui = Ui_ShowContent()
        self.ui.setupUi(self)
        
        self.init_ui()
        
    def init_ui(self):
        self.ui.radio_info.setChecked(True)
        self.ui.radio_tl.setChecked(True)
        self.ui.btn_choose_icon.setEnabled(False)
        
        
        layout = QtGui.QHBoxLayout()
        self.ui.tab_content.setLayout(layout)
        self.add_media_widget = AddMediaWidget()
        layout.addWidget(self.add_media_widget)
        
        self.ui.radio_personalized.toggled.connect(self.personalized_choosed)
        self.ui.btn_choose_icon.clicked.connect(self.choose_icon)
        
        self.lbl_screen = QtGui.QLabel(self.ui.widget_icon)
        self.lbl_screen.resize(self.ui.widget_icon.size())
        self.lbl_screen.setStyleSheet('background-color: rgb(0, 0, 0); \
                                        border-color: rgb(255, 255, 255);\
                                        font: 75 28pt "Ubuntu";\
                                        color: rgb(255, 255, 127);')
        self.lbl_screen.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_screen.setText("Tela")
        
        self.lbl_icon = MovebleLabel(u"", self.ui.widget_icon)
        self.lbl_icon.resize(30,30)
        self.lbl_icon.move(10,10)
        self.lbl_icon.setStyleSheet('background-color: rgb(255, 255, 0);\
                                            border-color: rgb(255, 255, 255);\
                                            font: 75 8pt "Ubuntu";\
                                            color: rgb(0, 0, 0);')
        self.lbl_icon.setEnabled(False)
        
        self.ui.radio_bl.toggled.connect(self.selected_bl)
        self.ui.radio_br.toggled.connect(self.selected_br)
        self.ui.radio_tr.toggled.connect(self.selected_tr)
        self.ui.radio_tl.toggled.connect(self.selected_tl)
        self.ui.radio_free_position.toggled.connect(self.selected_free_position)
        
    @QtCore.pyqtSlot(bool)
    def selected_bl(self, value):
        self.lbl_icon.resize(30,30)
        self.lbl_icon.move(10,150)
        self.lbl_icon.setEnabled(False)
    
    @QtCore.pyqtSlot(bool)
    def selected_br(self, value):
        self.lbl_icon.resize(30,30)
        self.lbl_icon.move(300,150)
        self.lbl_icon.setEnabled(False)
    
    @QtCore.pyqtSlot(bool)
    def selected_tr(self, value):
        self.lbl_icon.resize(30,30)
        self.lbl_icon.move(300,10)
        self.lbl_icon.setEnabled(False)
    
    @QtCore.pyqtSlot(bool)
    def selected_tl(self, value):
        self.lbl_icon.resize(30,30)
        self.lbl_icon.move(10,10)
        self.lbl_icon.setEnabled(False)
    
    @QtCore.pyqtSlot(bool)
    def selected_free_position(self, value):
        self.lbl_icon.setEnabled(True)
        
        
        
        
    @QtCore.pyqtSlot()
    def choose_icon(self):
        path = QtGui.QFileDialog.getOpenFileName(self, 
                                                 u'Selecione uma imagem',
                                                 HOME_DIRECTORY,
                                                 model.CONTENT_TYPES[model.Media.IMAGE])
        if path == None:
            return
        
        self.icon_path = path
        self.ui.radio_personalized.setIcon(QtGui.QIcon(path))
        self.ui.radio_personalized.setText("...")
    
    @QtCore.pyqtSlot(bool)
    def personalized_choosed(self, checked):
        if checked:
            self.ui.btn_choose_icon.setEnabled(True)
        else:
            self.ui.btn_choose_icon.setEnabled(False)
            
        
def main():
    import sys
    app = QtGui.QApplication(sys.argv)    
    vp = ShowContent()
    vp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()