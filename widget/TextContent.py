#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Nov 16, 2013

@author: caioviel
'''

from ui.ui_TextContent import Ui_TextContent
from LayoutSelector import LayoutSelector
from PyQt4 import QtGui, QtCore
import util
import model

class TextContent(QtGui.QDialog):
    def __init__(self, project=None, annotation=None, content=None, parent=None):
        super(TextContent, self).__init__(parent)
        self.ui = Ui_TextContent()
        self.project = project
        self.annotation = annotation
        self.content = content
        
        if content is not None:
            print content, content.text
        
        self.result = None
        
        self.ui.setupUi(self)
        self.align_array = [QtCore.Qt.AlignLeft, QtCore.Qt.AlignCenter, QtCore.Qt.AlignRight]
        self.text_alligment = QtCore.Qt.AlignCenter
        
        self.bg_color = QtGui.QColor(QtCore.Qt.white)
        self.font_color = QtGui.QColor(QtCore.Qt.black)
        self.current_font = self.ui.textEdit.font()
        self.transparency_bg = False
        self.text_content = ""
        
        #TODO:
        self.init_ui()
        self.load_content()
        
    def get_result(self):
        return self.result
            
    def load_content(self):
        if self.annotation is not None:
            self.ui.time_begin.setTime(self.annotation.annotation_time)
            
        if self.content is not None:
            self.ui.textEdit.append(self.content.text)
            
            begin = util.sec_to_qtime(self.content.showtime)
            
            self.ui.time_begin.setTime(begin)
            
            self.ui.time_end.setTime(begin.addSecs(self.content.duration))
            
            if self.content.bondaries is not None:
                self.layout_selector.set_content_bondaires(
                                            self.content.bondaries)
            
            if self.content.resize_main_video is not None:
                self.layout_selector.set_main_video_bondaries(
                                            self.content.resize_main_video)
                
            print self.content.bg_color
            if self.content.bg_color is not None:
                self.bg_color = self.content.bg_color
                self.ui.lbl_bg_color.setStyleSheet("background-color: rgb"+str(self.bg_color.getRgb())+";")
                
            if self.content.font_color is not None:
                self.font_color = self.content.font_color
                self.ui.lbl_font_color.setStyleSheet("background-color: rgb"+str(self.font_color.getRgb())+";")
                
            font = QtGui.QFont()
            if self.content.font is not None:
                print 'font family', self.content.font
                font.setFamily(self.content.font)
            
            if self.content.fontSize is not None:
                print 'font fontSize', self.content.fontSize
                font.setPointSize(self.content.fontSize)
            
            if self.content.bold is not None:
                print 'font bold', self.content.bold
                font.setBold(self.content.bold)
                
            if self.content.italic is not None:
                print 'font italic', self.content.italic
                font.setItalic(self.content.italic)
                
            if self.content.underlined is not None:
                print 'font underlined', self.content.underlined
                font.setUnderline(self.content.underlined)
                
            self.current_font = font
            self.transparency_bg = self.content.bg_transparency
            self.text_content = self.content.text
            
            if self.content.alignment is not None:
                self.text_alligment = self.align_array[self.content.alignment]
                self.ui.cmb_alligment.setCurrentIndex(self.content.alignment)
            
            self.update_text()
                

    def init_ui(self):
        self.layout_selector = LayoutSelector(parent=self.ui.layout_selection_holder)
        
        lbl_content = self.layout_selector.lbl_content
        lbl_content.resize(self.layout_selector.width(),50)
        self.update_text()
        self.ui.cmb_alligment.setCurrentIndex(1)
        
        self.ui.btn_bg_color.clicked.connect(self.select_bg_color)
        self.ui.btn_font_color.clicked.connect(self.select_font_color)
        self.ui.btn_Font.clicked.connect(self.select_font)
        self.ui.ckb_transparency.stateChanged.connect(self.transparency_selected)
        self.ui.btn_reset_layout.clicked.connect(self.reset_layout)
        self.ui.cmb_alligment.currentIndexChanged.connect(self.allign_selected)
        self.ui.textEdit.textChanged.connect(self.text_changes)
        
        self.ui.btn_ok.clicked.connect(self.ok_pressed)
        self.ui.btn_cancel.clicked.connect(self.cancel_pressed)
        
        self.ui.time_begin.timeChanged.connect(self.calc_duration)
        self.ui.time_end.timeChanged.connect(self.calc_duration)
        
    @QtCore.pyqtSlot()   
    def calc_duration(self):
        begin = util.qtime_to_sec(self.ui.time_begin.time())
        end = util.qtime_to_sec(self.ui.time_end.time())
        
        self.ui.txt_duration.clear()
        if end >= begin:
            duration = end - begin
            self.ui.txt_duration.appendPlainText(str(duration))
        else:
            self.ui.txt_duration.appendPlainText('---')
            
    @QtCore.pyqtSlot()
    def ok_pressed(self):
        import uuid
        import os
    
        showtime = util.qtime_to_sec(self.ui.time_begin.time())
        duration = util.qtime_to_sec(self.ui.time_end.time()) - showtime
        text = None
        if self.content is None:
            filename = os.path.join(self.project.directory, 
                                    'medias', 
                                    str(uuid.uuid4()) + '.jpg')
            finalpath = util.copy_to_directory(self.project, filename)
            text = model.Text(filename, finalpath, showtime)
            text.duration = duration
        else:
            text = self.content
            text.showtime = showtime
            text.duration = duration

        pixmap = QtGui.QPixmap.grabWindow(self.layout_selector.lbl_content.winId())
        pixmap.save(text.filename)
        text.bondaries = self.layout_selector.get_content_bondaries()
        
        if self.layout_selector.is_main_video_resized():
            text.resize_main_video = self.layout_selector.get_main_video_bondaries()
        
        text.alignment = self.align_array.index(self.text_alligment)
        text.bg_color = self.bg_color
        text.font_color = self.font_color
        text.font = unicode(self.current_font.family())
        text.fontSize = self.current_font.pointSize()
        text.bg_transparency = self.ui.ckb_transparency.isChecked()
        text.text = unicode(self.ui.textEdit.toPlainText())
        text.bold = self.current_font.bold()
        text.italic = self.current_font.italic()
        text.underlined = self.current_font.underline()
        
        self.result = text
        
        self.close()
        
        
    
    @QtCore.pyqtSlot()
    def cancel_pressed(self):
        self.close()
    
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
        print 'update text'
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