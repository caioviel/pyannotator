#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
from ui.ui_AddMediaWidget import Ui_AddMediaWidget
from ui.ui_MediaListItem import Ui_MediaListItem
import os
import model
import util
HOME_DIRECTORY = os.getenv('USERPROFILE') or os.getenv('HOME')

from TextContent import TextContent
from VideoContent import VideoContent
from ImageContent import ImageContent
from AudioContent import AudioContent

def get_media_icon(media_type):
    #TODO: add icon for slides
    if media_type == model.Media.VIDEO:
        return QtGui.QPixmap(":/m/video.png")
    elif media_type == model.Media.AUDIO:
        return QtGui.QPixmap(":/m/audio.png")
    elif media_type == model.Media.TEXT:
        return QtGui.QPixmap(":/m/plain_text.png")
    elif media_type == model.Media.IMAGE:
        return QtGui.QPixmap(":/m/image.png")
    elif media_type == model.Media.SLIDES:
        return QtGui.QPixmap(":/i/slides.png")

class MediaListItem(QtGui.QWidget):
    def __init__(self, content, parent=None):
        super(MediaListItem, self).__init__(parent)
        self.ui = Ui_MediaListItem()
        self.content = content
        self.ui.setupUi(self)
        self.init_ui()
        
    def init_ui(self):
        self.ui.lbl_content_icon.setPixmap(get_media_icon(self.content.type))
        begin_time = util.sec_to_qtime(self.content.showtime)
        end_time = util.sec_to_qtime(self.content.showtime + self.content.duration)
        print begin_time, end_time
        description = u'De ' + begin_time.toString() + u' até ' + end_time.toString()
        self.ui.lbl_description.setText(description)
        


class AddMediaWidget(QtGui.QDialog):
    def __init__(self, project=None, annotation=None, parent=None):
        super(AddMediaWidget, self).__init__(parent)
        self.ui = Ui_AddMediaWidget()
        self.ui.setupUi(self)
        self.medias = []
        self.project = project
        self.annotation = annotation
        
        self.init_ui()
        self.show()
        
    def init_ui(self):
        self.ui.btn_audio.clicked.connect(self.add_audio)
        self.ui.btn_image.clicked.connect(self.add_image)
        self.ui.btn_video.clicked.connect(self.add_video)
        self.ui.btn_text.clicked.connect(self.add_text)
        self.ui.btn_slides.clicked.connect(self.add_slides)
        
        self.ui.btn_delete.clicked.connect(self.delete_media)
        self.ui.btn_edit.clicked.connect(self.edit_media)
        
        self.ui.btn_slides.setEnabled(False)
        
    @QtCore.pyqtSlot()
    def delete_media(self):
        item = self.ui.lst_medias.currentItem()
        content = self.ui.lst_medias.itemWidget(item).content
        reply = QtGui.QMessageBox.question(self, u"Excluindo mídia...", 
                                           u"Tem certeza que deseja excluir está mídia?",
                                           QtGui.QMessageBox.Yes|QtGui.QMessageBox.No);
                                           
        if reply == QtGui.QMessageBox.No:
            return
        
        self.medias.remove(content)
        self.update_media_list()
        
    @QtCore.pyqtSlot()
    def edit_media(self):
        item = self.ui.lst_medias.currentItem()
        content = self.ui.lst_medias.itemWidget(item).content
        if content.type == model.Media.AUDIO:
            myclass = AudioContent(self.project, self.annotation, 
                                   content, self)
            myclass.exec_()
        elif content.type == model.Media.VIDEO:
            myclass = VideoContent(self.project, self.annotation, 
                                   content, self)
            myclass.exec_()
        elif content.type == model.Media.IMAGE:
            myclass = ImageContent(self.project, self.annotation, 
                                   content, self)
            myclass.exec_()
        elif content.type == model.Media.TEXT:
            myclass = TextContent(self.project, self.annotation, 
                                   content, self)
            myclass.exec_()
    
    def add_media_item(self, new_media):
        self.medias.append(new_media)
        
    @QtCore.pyqtSlot()
    def update_media_list(self):
        self.ui.lst_medias.clear()
        if len(self.medias) == 0:
            return
        
        sorted_medias = sorted(self.medias, 
                                    key=lambda media: media.showtime)
        
        print self.medias
        print sorted_medias
        
        for media in sorted_medias:
            mediaItem = MediaListItem(media, self)
            item = QtGui.QListWidgetItem()
            item.setSizeHint(QtCore.QSize(40,60))
            self.ui.lst_medias.addItem(item)
            self.ui.lst_medias.setItemWidget(item, mediaItem)
        
    @QtCore.pyqtSlot()
    def add_audio(self):
        myclass = AudioContent(self.project, self.annotation, 
                               parent=self)
        myclass.exec_()
        result = myclass.get_result()
        if result is not None:
            self.add_media_item(result)    
            self.update_media_list()
        
    @QtCore.pyqtSlot()
    def add_image(self):
        myclass = ImageContent(self.project, self.annotation, 
                               parent=self)
        myclass.exec_()
        result = myclass.get_result()
        if result is not None:
            self.add_media_item(result)    
            self.update_media_list()
            
    @QtCore.pyqtSlot()
    def add_video(self):
        myclass = VideoContent(self.project, self.annotation, 
                               parent=self)
        myclass.exec_()
        result = myclass.get_result()
        if result is not None:
            self.add_media_item(result)    
            self.update_media_list()
        
    @QtCore.pyqtSlot()
    def add_text(self):
        myclass = TextContent(self.project, self.annotation, 
                               parent=self)
        myclass.exec_()
        result = myclass.get_result()
        if result is not None:
            print result, result.text
            
            self.add_media_item(result)    
            self.update_media_list()
        
    @QtCore.pyqtSlot()
    def add_slides(self):
        print 'add add_slides'
        
def main():
    import sys
    app = QtGui.QApplication(sys.argv)    
    vp = AddMediaWidget()
    vp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()