#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Feb 3, 2013

@author: caioviel
'''
from datetime import datetime
import logging
logger = logging.getLogger('pyannotator')
logger.setLevel(logging.DEBUG)

import model
from model import Annotation
from PyQt4 import QtGui, QtCore
from PyQt4.phonon import Phonon
from ui.ui_MainProjectWidget import Ui_MainProjectWidget
from ui.ui_AnnotationListItem import Ui_AnnotationListItem
from VideoPlayer import VideoPlayer
import os
import sys
import getpass

real_path, _ = os.path.split(os.path.realpath(__file__))
home_directory = os.getenv('USERPROFILE') or os.getenv('HOME')
username = getpass.getuser()


class AnnotationListItem(QtGui.QWidget):
    def __init__(self, annotation, main_widget, parent=None):
        super(AnnotationListItem, self).__init__(parent)
        self.annotation = annotation
        self.ui = Ui_AnnotationListItem()
        self.ui.setupUi(self)
        self.main_widget = main_widget
        
        self.init_ui()
        
        self.load_annotation()
        
    def init_ui(self):
        self.pop_menu = QtGui.QMenu(self)
        action = QtGui.QAction(QtGui.QIcon(":/i/comment_edit.png"), u'Alterar', self)
        action.triggered.connect(self.main_widget.edit_annotation)
        self.pop_menu.addAction(action)
        
        action = QtGui.QAction(QtGui.QIcon(":/i/comment_delete.png"), u'Excluir', self)
        action.triggered.connect(self.main_widget.delete_annotation)
        self.pop_menu.addAction(action)
        self.pop_menu.addSeparator()
        
        if self.annotation.interaction is None:
            sub_menu = QtGui.QMenu(u"Definir Interação", self)
            self.pop_menu.addMenu(sub_menu)
            
            
            action = QtGui.QAction(u'Exibir conteúdo', self)
            action.triggered.connect(self.main_widget.show_content_widget)
            sub_menu.addAction(action)
            sub_menu.addAction(QtGui.QAction(u'Pular Cena', self))
            sub_menu.addAction(QtGui.QAction(u'Retroceder Cena', self))
            sub_menu.addAction(QtGui.QAction(u'Inserir Enquete', self))
        else:
            action = QtGui.QAction(u'Editar exibir conteúdo', self)
            action.triggered.connect(self.main_widget.show_content_widget)
            self.pop_menu.addAction(action)
            
            sub_menu = QtGui.QMenu(u"Alterar Interação", self)
            self.pop_menu.addMenu(sub_menu)
            
            
            #action = QtGui.QAction(u'Exibir conteúdo', self)
            #action.triggered.connect(self.main_widget.show_content_widget)
            #sub_menu.addAction(action)
            sub_menu.addAction(QtGui.QAction(u'Pular Cena', self))
            sub_menu.addAction(QtGui.QAction(u'Retroceder Cena', self))
            sub_menu.addAction(QtGui.QAction(u'Inserir Enquete', self))
        
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        #self.connect(self.connect(self.button, QtCore.SIGNAL('customContextMenuRequested(const QPoint&)'), self.on_context_menu)
        
        self.customContextMenuRequested.connect(self.on_context_menu)
    
    @QtCore.pyqtSlot(QtCore.QPoint)
    def on_context_menu(self, point):
        # show context menu
        self.pop_menu.exec_(self.mapToGlobal(point)) 
    
    
    def load_annotation(self):
        #icon = get_media_icon(self.annotation.content_type)
        #self.ui.lbl_content_type.setPixmap(icon)
        self.ui.lbl_type.setText(self.annotation.pt_type)
        self.ui.lbl_timestamp.setText(self.annotation.annotation_time.toString())
        if len(unicode(self.annotation)) > 20:
            self.ui.lbl_description.setText((self.annotation.description)[:20] + "...")
        else:
            self.ui.lbl_description.setText(unicode(self.annotation.description))
        
        
        self.setToolTip(self.annotation.description)

class MainProjectWidget(QtGui.QWidget):
    
    annotation_list_chaged = QtCore.pyqtSignal()
    
    def __init__(self, project, parent=None):
        super(MainProjectWidget, self).__init__(parent)
        self.ui = Ui_MainProjectWidget()
        self.ui.setupUi(self)
        self.project_diretory = project.directory
        self.main_video_path = None
        self.is_editing_time = False
        self.open_widgets = []
        self.project = project

        
        self.init_ui()
        self.load_project()
        
        self.show()
    
    #@QtCore.pyqtSlot(int)
    #def on_video_seek(self, point):
        
        
    def init_ui(self):
        self.setWindowTitle(u'Projeto - ' + self.project.name)
        
        player_holder = self.ui.player_widget
        layout = QtGui.QVBoxLayout()
        self.player = VideoPlayer()
        layout.addWidget(self.player)
        player_holder.setLayout(layout)
        
        #self.player.ui.seek_slider.mouse_released.connect(self.update_time_edit)
        
        self.ui.frame_edit.setVisible(False)
        
        self.ui.btn_choose_video.clicked.connect(self.choose_video)
        
        self.ui.btn_add_annotation.clicked.connect(self.add_annotation)
        #self.ui.btn_delete.clicked.connect(self.delete_annotation)
        #self.ui.btn_edit.clicked.connect(self.edit_annotation)
        self.annotation_list_chaged.connect(self.update_annotation_list)
        self.ui.txt_description.textChanged.connect(self.description_changed)
        #self.ui.list_notes.doubleClicked.connect(self.click_over_list)
        
        #self.player.mediaObject().tick.connect(self.update_time_edit)
        self.ui.time_edit.timeChanged.connect(self.editing_time)
        self.ui.time_edit.installEventFilter(self)
        
        self.ui.btn_save_project.clicked.connect(self.save_project)
        self.ui.btn_generate_ncl.clicked.connect(self.generate_ncl)
        self.ui.btn_close_project.clicked.connect(self.close_project)
        
        self.ui.btn_ok.clicked.connect(self.save_edit)
        self.ui.btn_cancel.clicked.connect(self.cancel_edit)
        
    def load_project(self):
        project = self.project
        if project.main_media:
            self.main_video_path = project.main_media           
            self.player.load_video(self.main_video_path)
            self.player.player.mediaObject().tick.connect(self.update_time_edit)
            self.ui.txt_main_video.appendPlainText(self.main_video_path)
            self.update_annotation_list()
        
    def eventFilter(self, myObject, event):
        if myObject == self.ui.time_edit:
            if event.type() == QtCore.QEvent.FocusIn:
                self.timer_focus_in()
            elif event.type() == QtCore.QEvent.FocusOut:
                pass
            
        return False
    
    @QtCore.pyqtSlot()
    def close_project(self):
        reply = QtGui.QMessageBox.question(self, u"Fechando o projeto...", 
                                           u"Tem certeza que deseja fechar este projeto?",
                                           QtGui.QMessageBox.Yes|QtGui.QMessageBox.No);
                                           
        if reply == QtGui.QMessageBox.No:
            return
        from ProjectChooseWidget import ProjectChooseWidget
        self._choose_widget = ProjectChooseWidget(real_path, home_directory, username)
        self.close()
        
        
        
    
    @QtCore.pyqtSlot()
    def save_project(self):
        print self.main_video_path
        self.project.main_media = self.main_video_path
        from datetime import datetime
        self.project.last_modification = datetime.now()
        project_path = os.path.join(unicode(self.project_diretory), 'project.json')
        json_object = self.project.to_json()
        myfile = open(project_path, "w")
        
        import json
        myfile.write(json.dumps(json_object, indent=4, sort_keys=True))
        
    
    @QtCore.pyqtSlot()
    def description_changed(self):
        self.player.pause()
    
    @QtCore.pyqtSlot()
    def generate_ncl(self):
        raise NotImplementedError()   
        
    @QtCore.pyqtSlot()
    def update_annotation_list(self):
        self.ui.list_notes.clear()
        sorted_annotations = sorted(self.project.annotations, 
                                    key=lambda ann: ann.annotation_time)
        
        for annotation in sorted_annotations:
            anotationItem = AnnotationListItem(annotation, self)
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
            
            
    @QtCore.pyqtSlot()
    def delete_annotation(self):
        item = self.ui.list_notes.currentItem()
        annotation = self.ui.list_notes.itemWidget(item).annotation
        if self.project.remove_annotation(annotation):
            self.annotation_list_chaged.emit()
            
            
    @QtCore.pyqtSlot()
    def show_content_widget(self):
        item = self.ui.list_notes.currentItem()
        annotation = self.ui.list_notes.itemWidget(item).annotation
        
        from ShowContent import ShowContent
        widget = ShowContent(self.project, annotation, self)
        widget.exec_()
        self.update_annotation_list()
        
    
    @QtCore.pyqtSlot()
    def edit_annotation(self):
        item = self.ui.list_notes.currentItem()
        self.editing_annotation = self.ui.list_notes.itemWidget(item).annotation
        self.ui.txt_description.setText(self.editing_annotation.description)
        self.ui.time_edit.setTime(self.editing_annotation.annotation_time)
        self.ui.frame_edit.setVisible(True)
        self.ui.txt_description.setFocus()
        
        self.ui.frame_notes.setEnabled(False)
        self.ui.btn_add_annotation.setVisible(False)
        self.ui.btn_save_project.setVisible(False)
        self.ui.btn_generate_ncl.setVisible(False)
        
        
    @QtCore.pyqtSlot()
    def cancel_edit(self):
        self.ui.frame_edit.setVisible(False)
        self.ui.frame_notes.setEnabled(True)
        self.ui.btn_add_annotation.setVisible(True)
        self.ui.btn_save_project.setVisible(True)
        self.ui.btn_generate_ncl.setVisible(True)
        self.ui.txt_description.setText("")
        
        
    @QtCore.pyqtSlot()
    def save_edit(self):
        self.editing_annotation.description = unicode(self.ui.txt_description.toPlainText())
        self.editing_annotation.annotation_time = self.ui.time_edit.time()
        
        self.ui.frame_edit.setVisible(False)
        self.ui.frame_notes.setEnabled(True)
        self.ui.btn_add_annotation.setVisible(True)
        self.ui.btn_save_project.setVisible(True)
        self.ui.btn_generate_ncl.setVisible(True)
        self.ui.txt_description.setText("")
        self.annotation_list_chaged.emit()
    
        
    @QtCore.pyqtSlot()
    def add_annotation(self):
        self.player.pause()
        print self.ui.time_edit.time()
        annotation = model.Annotation(self.project.generate_annotation_id(), 
                                      datetime.now())
        description = self.ui.txt_description.toPlainText()
        
        if description != "":
            annotation.description = description
            
        print self.ui.time_edit.time()
        annotation.annotation_time = self.ui.time_edit.time()
        
        self.project.add_annotation(annotation)
        self.ui.txt_description.setText("")
        self.annotation_list_chaged.emit()
        
        
        
        
    @QtCore.pyqtSlot(int)
    def update_time_edit(self, time):
        if not self.is_editing_time:
            time_edit = self.ui.time_edit
            time_edit.setTime(QtCore.QTime().addMSecs(time))
        
        
    @QtCore.pyqtSlot()
    def start_playback(self):
        player = self.ui.video_player
        player.play()
        self.ui.btn_pause.setVisible(True)
        self.ui.btn_play.setVisible(False)
        self.ui.btn_stop.setEnabled(True)
        self.is_editing_time = False
        
    
    @QtCore.pyqtSlot(QtCore.QTime)
    def editing_time(self, time):
        '''if self.is_editing_time:
            total_time = self.player.player.mediaObject().totalTime()
            max_time = QtCore.QTime(0,0,0).addMSecs(total_time)
            self.ui.time_edit.setTimeRange(QtCore.QTime(0,0,0), max_time)
            
            
            msec = time.hour()
            msec = time.minute() + msec*60
            msec = time.second() + msec*60
            msec = msec*1000 + time.msec()
            self.ui.video_player.seek(msec)'''
        pass
            
            
    def timer_focus_in(self):
        self.player.pause()
        self.is_editing_time = True
        
    
    @QtCore.pyqtSlot()
    def choose_video(self):
        path = QtGui.QFileDialog.getOpenFileName(self, 
                                                 u'Selecione o Vídeo Principal',
                                                 unicode(self.project_diretory),
                                                 model.CONTENT_TYPES[model.Media.VIDEO])
        
        print path
        if path == None:
            return
        
        import util
        
        
        self.main_video_path = util.copy_to_directory(self.project, unicode(path))           
        self.ui.txt_main_video.clear()
        self.ui.txt_main_video.appendPlainText(self.main_video_path)
        
        self.player.stop()
        self.player.load_video( self.main_video_path )
        self.player.player.mediaObject().tick.connect(self.update_time_edit)
        self.player.play()


def test():
    import sys
    from datetime import datetime
    app = QtGui.QApplication(sys.argv)
    project = model.AnnotationProject('meu_id', 'meu_nome', None, '', datetime.now(), 'username')
    project.directory = '/home/caioviel/AnnotationProjects/MeuProjeto'
    widget = MainProjectWidget(project)
    sys.exit(app.exec_())
        
if __name__ == "__main__":
    test()