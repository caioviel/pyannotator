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
            
        if self.annotation.interaction is not None:
            show_content = self.annotation.interaction
            self.ui.ckb_compulsory.setChecked(show_content.compulsory)
            self.ui.ckb_allows_end_content.setChecked(show_content.compulsory)
            self.ui.ckb_show_on_tv.setChecked(show_content.tv)
            self.ui.ckb_show_on_mobile.setChecked(show_content.mobile)
            self.ui.ckb_pause_main_video.setChecked(show_content.pause_main_video)
            
            if show_content.icon.image == model.Icon.INFO:
                self.ui.radio_info.setChecked(True)
            elif show_content.icon.image == model.Icon.SEXUAL:
                self.ui.radio_sexual.setChecked(True)
            elif show_content.icon.image == model.Icon.VIOLENCE:
                self.ui.radio_violence.setChecked(True)
            elif show_content.icon.image == model.Icon.YES:
                self.ui.radio_yes.setChecked(True)
            elif show_content.icon.image == model.Icon.NO:
                self.ui.radio_no.setChecked(True)
            else:
                self.ui.radio_personalized.setChecked(True)
                self.icon_path = show_content.icon.image
                self.ui.radio_personalized.setIcon(QtGui.QIcon(self.icon_path))
                
            if show_content.icon.position == model.Icon.BOT_LEFT:
                self.ui.radio_bl.setChecked(True)
            elif show_content.icon.position == model.Icon.BOT_RIGHT:
                self.ui.radio_br.setChecked(True)
            elif show_content.icon.position == model.Icon.TOP_LEFT:
                self.ui.radio_tl.setChecked(True)
            elif show_content.icon.position == model.Icon.TOP_RIGHT:
                self.ui.radio_tr.setChecked(True)
            elif show_content.icon.position == model.Icon.PERSONALIZED:
                self.ui.radio_free_position.setChecked(True)
                
            self.set_icon_boundaries(show_content.icon.bondaries)
            
            before_str = str(show_content.icon.relative_time)
            for index in xrange(self.ui.cmb_icon_before.count()):
                str_index = str(self.ui.cmb_icon_before.itemText(index))
                if before_str == str_index:
                    self.ui.cmb_icon_before.setCurrentIndex(index)
                    break
                
            duration_str = str(show_content.icon.duration_time)
            for index in xrange(self.ui.cmb_icon_duration.count()):
                str_index = str(self.ui.cmb_icon_duration.itemText(index))
                if duration_str == str_index:
                    self.ui.cmb_icon_duration.setCurrentIndex(index)
                    break
                
            for content in show_content.contents:
                self.add_media_widget.add_media_item(content)
                
            self.add_media_widget.update_media_list()
        
    def get_result(self):
        return self.result
    
    def set_icon_boundaries(self, bound):
        self.lbl_icon.move(bound.left, bound.top)
        self.lbl_icon.resize(bound.width, bound.height)
    
    def get_icon_bondaries(self):
        bound = Bondaries()
        qpoint = self.lbl_icon.pos()
        qsize = self.lbl_icon.size()
        bound.width = qsize.width()
        bound.height = qsize.height()
        bound.left = qpoint.x()
        bound.top = qpoint.y()
        qsize = self.lbl_screen.size()
        bound.screen_width, bound.screen_height = qsize.width(), qsize.height()
        print bound
        return bound
        
    def init_ui(self):
        self.setFixedSize(self.size())
        self.ui.radio_info.setChecked(True)
        self.ui.radio_tl.setChecked(True)
        self.ui.btn_choose_icon.setEnabled(False)
        
        
        layout = QtGui.QHBoxLayout()
        self.ui.tab_content.setLayout(layout)
        self.add_media_widget = AddMediaWidget(self.project, self.annotation)
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
        show_content.tv = self.ui.ckb_show_on_tv.isChecked()
        show_content.mobile = self.ui.ckb_show_on_mobile.isChecked()
        show_content.pause_main_video = self.ui.ckb_pause_main_video.isChecked()
        
        icon = model.Icon()
        if self.ui.radio_personalized.isChecked():
            self.icon_path = util.copy_to_directory(self.project, unicode(self.icon_path))
            icon.image = self.icon_path
        elif self.ui.radio_info.isChecked():
            icon.image = model.Icon.INFO
        elif self.ui.radio_sexual.isChecked():
            icon.image = model.Icon.SEXUAL
        elif self.ui.radio_violence.isChecked():
            icon.image = model.Icon.VIOLENCE
        elif self.ui.radio_yes.isChecked():
            icon.image = model.Icon.YES
        elif self.ui.radio_no.isChecked():
            icon.image = model.Icon.NO
            
        icon.relative_time = int(self.ui.cmb_icon_before.itemText(
                                            self.ui.cmb_icon_before.currentIndex()))
        icon.duration_time = int(self.ui.cmb_icon_duration.itemText(
                                            self.ui.cmb_icon_duration.currentIndex()))
        icon.bondaries = self.get_icon_bondaries()
        
        if self.ui.radio_bl.isChecked():
            icon.position == model.Icon.BOT_LEFT
        elif self.ui.radio_br.isChecked():
            icon.position == model.Icon.BOT_RIGHT
        elif self.ui.radio_tl.isChecked():
            icon.position == model.Icon.TOP_LEFT
        elif self.ui.radio_tr.isChecked():
            icon.position == model.Icon.TOP_RIGHT
        elif self.ui.radio_free_position.isChecked():
            icon.position == model.Icon.PERSONALIZED
        
        show_content.icon = icon
        
        for media in self.add_media_widget.medias:
            show_content.add_content(media)
            
        self.annotation.description = unicode(self.ui.textEdit.toPlainText())
        self.annotation.interaction = show_content
        
        self.result = show_content
        
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