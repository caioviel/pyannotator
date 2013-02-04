#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Feb 3, 2013

@author: caioviel
'''
import os

import logging
logger = logging.getLogger('pyannotator')
logger.setLevel(logging.DEBUG)


from model import Annotation, CONTENT_TYPES
from PySide import QtGui, QtCore
from PySide.phonon import Phonon
from ui.ui_MainProjectWidget import Ui_MainProjectWidget
from ui.ui_AnnotationListItem import Ui_AnnotationListItem
import model

def get_media_icon(media_type):
    if media_type == model.Annotation.VIDEO:
        return QtGui.QPixmap(":/m/video.png")
    elif media_type == model.Annotation.AUDIO:
        return QtGui.QPixmap(":/m/audio.png")
    elif media_type == model.Annotation.HTML:
        return QtGui.QPixmap(":/m/html.png")
    elif media_type == model.Annotation.PLAIN_TEXT:
        return QtGui.QPixmap(":/m/plain_text.png")
    elif media_type == model.Annotation.IMAGE:
        return QtGui.QPixmap(":/m/image.png")


class AnnotationListItem(QtGui.QWidget):
    def __init__(self, annotation, parent=None):
        super(AnnotationListItem, self).__init__(parent)
        self.ui = Ui_AnnotationListItem()
        self.ui.setupUi(self)
        
        self.annotation = annotation
        self.load_annotation()
        
    def load_annotation(self):
        icon = get_media_icon(self.annotation.content_type)
        self.ui.lbl_content_type.setPixmap(icon)
        self.ui.lbl_type.setText(self.annotation.name)
        self.ui.lbl_timestamp.setText(self.annotation.timestamp.toString())

class MainProjectWidget(QtGui.QWidget):
    
    annotation_list_chaged = QtCore.Signal()
    
    def __init__(self, project, project_directory, serializator, plugin_manager, parent=None):
        super(MainProjectWidget, self).__init__(parent)
        self.ui = Ui_MainProjectWidget()
        self.ui.setupUi(self)
        self.project_diretory = project_directory
        self.main_video_path = None
        self.is_editing_time = False
        self.open_widgets = []
        self.project = project
        self.serializator = serializator
        self.plugin_manager = plugin_manager

        
        self.init_ui()
        self.load_project()
        
        self.show()
        
    def load_project(self):
        project = self.project
        if project.main_media:
            self.main_video_path = project.main_media           
            player = self.ui.video_player
            self.ui.txt_main_video.clear()
            self.ui.txt_main_video.appendPlainText(project.main_media)
        
            player.stop()
            media_source = Phonon.MediaSource(project.main_media)
            player.load( media_source )
            self.ui.seek_slider.setMediaObject(player.mediaObject())
            self.ui.volume_slider.setAudioOutput(player.audioOutput())
        
            player.setVisible(True)
            self.ui.seek_slider.setVisible(True)
            self.ui.volume_slider.setVisible(True)
            self.ui.btn_play.setVisible(True)
            self.ui.btn_stop.setVisible(True)
            self.ui.btn_stop.setEnabled(False)
        
            self.update_annotation_list()
        
    def eventFilter(self, myObject, event):
        if myObject == self.ui.time_edit:
            if event.type() == QtCore.QEvent.FocusIn:
                self.timer_focus_in()
            elif event.type() == QtCore.QEvent.FocusOut:
                pass
            
        return False
        
    
    def init_ui(self):
        self.setWindowTitle(u'Projeto - ' + self.project.name)
        
        player = self.ui.video_player
        
        self.ui.btn_choose_video.clicked.connect(self.choose_video)
        self.ui.btn_play.clicked.connect(self.start_playback)
        self.ui.btn_stop.clicked.connect(self.stop_playback)
        self.ui.btn_pause.clicked.connect(self.pause_playback)
        
        self.ui.btn_add_annotation.clicked.connect(self.add_annotation)
        self.ui.btn_delete.clicked.connect(self.delete_annotation)
        self.ui.btn_edit.clicked.connect(self.edit_annotation)
        self.annotation_list_chaged.connect(self.update_annotation_list)
        
        player.mediaObject().tick.connect(self.update_time_edit)
        self.ui.time_edit.timeChanged.connect(self.editing_time)
        self.ui.time_edit.installEventFilter(self)
        
        self.ui.btn_save_project.clicked.connect(self.save_project)
        self.ui.btn_generate_ncl.clicked.connect(self.generate_ncl)
    
    @QtCore.Slot()
    def save_project(self):
        print self.main_video_path
        self.project.main_media = self.main_video_path
        from datetime import datetime
        self.project.last_modification = datetime.now()
        project_path = os.path.join(self.project_diretory, 'project.json')
        self.serializator.dump_file(self.project, project_path)
        
    
    @QtCore.Slot()
    def generate_ncl(self):
        raise NotImplementedError()
        
    @QtCore.Slot()
    def update_annotation_list(self):
        self.ui.list_notes.clear()
        for annotation in self.project.annotations:
            anotationItem = AnnotationListItem(annotation)
            item = QtGui.QListWidgetItem()
            item.setSizeHint(QtCore.QSize(40,60))
            self.ui.list_notes.addItem(item)
            self.ui.list_notes.setItemWidget(item, anotationItem)
    
    def save_annotation(self, widget, annotation):
        try:
            self.project.add_annotation(annotation)
        except:
            pass
        try:
            self.annotation_list_chaged.emit()
            self.open_widgets.remove(widget)
        except:
            logger.exception("Error Saving the Annotation.")
    
    def cancel_annotation(self, widget):
        try:
            self.open_widgets.remove(widget)
        except:
            logger.exception("Error Canceling the Annotation.")
            
            
    @QtCore.Slot()
    def delete_annotation(self):
        item = self.ui.list_notes.currentItem()
        annotation = self.ui.list_notes.itemWidget(item).annotation
        if self.project.remove_annotation(annotation):
            self.annotation_list_chaged.emit()
        
    
    @QtCore.Slot()
    def edit_annotation(self):
        item = self.ui.list_notes.currentItem()
        annotation = self.ui.list_notes.itemWidget(item).annotation
        
        widget_class = annotation.get_widget_class()
        widget = widget_class(annotation, self)
        self.open_widgets.append(widget)
        widget.show()
    
        
    @QtCore.Slot()
    def add_annotation(self):
        self.pause_playback()
        annotation_class = self.plugin_manager.get_annotation_class('InformationAnnotation')
        annotation = annotation_class('MyId')
        print annotation.type
        annotation.timestamp = self.ui.time_edit.time()
        
        widget_class = annotation.get_widget_class()
        widget = widget_class(annotation, self)
        self.open_widgets.append(widget)
        widget.show()
        
    @QtCore.Slot(int)
    def update_time_edit(self, time):
        if not self.is_editing_time:
            time_edit = self.ui.time_edit
            time_edit.setTime(QtCore.QTime().addMSecs(time))
        
        
    @QtCore.Slot()
    def start_playback(self):
        player = self.ui.video_player
        player.play()
        self.ui.btn_pause.setVisible(True)
        self.ui.btn_play.setVisible(False)
        self.ui.btn_stop.setEnabled(True)
        self.is_editing_time = False
        
    
    @QtCore.Slot(QtCore.QTime)
    def editing_time(self, time):
        if self.is_editing_time:
            total_time = self.ui.video_player.mediaObject().totalTime()
            max_time = QtCore.QTime(0,0,0).addMSecs(total_time)
            self.ui.time_edit.setTimeRange(QtCore.QTime(0,0,0), max_time)
            
            
            msec = time.hour()
            msec = time.minute() + msec*60
            msec = time.second() + msec*60
            msec = msec*1000 + time.msec()
            self.ui.video_player.seek(msec)
            
            
    def timer_focus_in(self):
        self.pause_playback()
        self.is_editing_time = True
        
    
    @QtCore.Slot()
    def stop_playback(self):
        player = self.ui.video_player
        player.stop()
        self.ui.btn_stop.setEnabled(False)
        self.ui.btn_pause.setVisible(False)
        self.ui.btn_play.setVisible(True)
    
    @QtCore.Slot()
    def pause_playback(self):
        player = self.ui.video_player
        player.pause()
        self.ui.btn_pause.setVisible(False)
        self.ui.btn_play.setVisible(True)
        
    
    @QtCore.Slot()
    def choose_video(self):
        path, _ = QtGui.QFileDialog.getOpenFileName(self, 
                                                 u'Selecione o Vídeo Principal',
                                                 self.project_diretory,
                                                 CONTENT_TYPES[Annotation.VIDEO])
        if path == None:
            return
        
        self.main_video_path = path           
        player = self.ui.video_player
        self.ui.txt_main_video.clear()
        self.ui.txt_main_video.appendPlainText(path)
        
        player.stop()
        media_source = Phonon.MediaSource(path)
        player.load( media_source )
        self.ui.seek_slider.setMediaObject(player.mediaObject())
        self.ui.volume_slider.setAudioOutput(player.audioOutput())
        
        player.setVisible(True)
        self.ui.seek_slider.setVisible(True)
        self.ui.volume_slider.setVisible(True)
        self.ui.btn_play.setVisible(True)
        self.ui.btn_stop.setVisible(True)
        self.ui.btn_stop.setEnabled(False)

def test():
    import sys
    app = QtGui.QApplication(sys.argv)
    widget = MainProjectWidget()
    sys.exit(app.exec_())
        
if __name__ == "__main__":
    test()