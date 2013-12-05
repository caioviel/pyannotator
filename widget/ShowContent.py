#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from ui.ui_ShowContent import Ui_ShowContent
from AddMediaWidget import AddMediaWidget

import model
import os
import util

HOME_DIRECTORY = os.getenv('USERPROFILE') or os.getenv('HOME')
from LayoutSelector import *

class ShowContent(QtGui.QDialog):
    def __init__(self, project=None, annotation=None, interaction=None, parent=None):
        super(ShowContent, self).__init__(parent)
        self.project = project
        self.annotation = annotation
        self.interaction = interaction
        
        self.ui = Ui_ShowContent()
        self.ui.setupUi(self)
        self.init_ui()
        
        self.load_annotation()
        
        self.result = None
        
    def load_annotation(self):
        if self.project is not None and \
                self.annotation is not None:
            
            self.ui.time_begin.setTime(self.annotation.annotation_time)
            self.ui.textEdit.append(self.annotation.description)
            
        if self.interaction is not None:
            pass
        
    def get_result(self):
        return self.result
    
    def get_icon_bondaries(self):
        pass
        
    def init_ui(self):
        self.setFixedSize(self.size())
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
        
        self.ui.btn_ok.clicked.connect(self.ok_pressed)
        self.ui.btn_cancel.clicked.connect(self.cancel_pressed)
        
    @QtCore.pyqtSlot()
    def ok_pressed(self):
        show_content = model.ShowContent()
        show_content.compulsory =  self.ui.ckb_compulsory.isChecked()
        show_content.allow_end_content = self.ui.ckb_allows_end_content.isChecked()
        show_content.tv = self.ui.ckb_show_on_tv
        show_content.mobile = self.ui.ckb_show_on_mobile
        show_content.pause_main_video = self.ui.ckb_pause_main_video
        
        icon = model.Icon()
        self.icon_path = util.copy_to_directory(self.project, self.icon_path)
        icon.image = self.icon_path
        icon.relative_time = int(self.ui.cmb_icon_before.itemText(0))
        icon.duration_time = int(self.ui.cmb_icon_duration.itemText(0))
            
        
        
        filename = unicode(self.ui.txt_media_name.toPlainText())
        #finalpath = util.copy_to_directory(self.project, filename)
        finalpath = filename
        showtime = util.qtime_to_sec(self.ui.time_begin.time())
        duration = util.qtime_to_sec(self.ui.time_end.time()) - showtime
        image_content = model.Image(filename, finalpath, showtime, duration)
        image_content.bondaries = self.layout_selector.get_content_bondaries()
        
        if self.layout_selector.is_main_video_resized():
            image_content.resize_main_video = self.layout_selector.get_main_video_bondaries()
            
        self.result = image_content
        
        self.close()
    
    @QtCore.pyqtSlot()
    def cancel_pressed(self):
        self.close()
        
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
    app = QtGui.QApplication(sys.argv)    
    vp = ShowContent()
    vp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()