#!/usr/bin/env python
# -*- coding: utf-8 -*-

from model import Annotation, CONTENT_TYPES
from PySide import QtGui, QtCore
from PySide.phonon import Phonon
from ui.ui_InformationAnnotationWidget import Ui_InformationAnnotationWidget 
    
class InformationAnnotationWidget(QtGui.QDialog):
    
    def __init__(self, annotation=None, target=None, parent=None):
        super(InformationAnnotationWidget, self).__init__(parent)
        self.ui = Ui_InformationAnnotationWidget()
        self.ui.setupUi(self)
        self.annotation = annotation
        self.target = target
        
        self.content_type = None
        self.content_path = None
        self.icon_path = None
        
        if self.annotation == None:
            self.annotation = InformationAnnotation("MyId")
        
        self.init_ui()
        self.__original_size = self.size()
        
        import os
        self.home_directory =  os.getenv('USERPROFILE') or os.getenv('HOME')
        
        self.load_annotation()
        self.show()
    
    @QtCore.Slot()
    def save_annotation(self):
        if not self.icon_path:
            QtGui.QMessageBox.information(self, u"Informações Insuficientes", 
                              u"Por favor, selecione o ícone de notificação desejado.")
            return
        
        
        if self.content_type == None or self.content_path == None:
            QtGui.QMessageBox.information(self, u"Informações Insuficientes", 
                              u"Por favor, selecione o conteúdo que deseja adicionar")
            return
        
        annotation = self.annotation
        annotation.notification_icon_file = self.icon_path
        try:
            annotation.notification_icon_duration = int(self.ui.cmb_icon_duration.currentText())
        except:
            QtGui.QMessageBox.Warning(self, u"Informações Incorretas", 
                              u"O tempo de duração do ícone de notificação deve ser um número inteiro")
            return
        
        annotation.notification_icon_timestamp = self.ui.time_icon.time()
        annotation.type = self.content_type
        annotation.information_media = self.content_path
        try:
            text = self.ui.cmb_content_durartion.currentText()
            if text == "":
                annotation.information_media_duration = None
            else:
                annotation.information_media_duration = int(text)
        except:
            QtGui.QMessageBox.Warning(self, u"Informações Incorretas", 
                              u"O tempo de duração do conteúdo deve ser vázio ou um número inteiro")
            return
        
        annotation.information_media_timestamp = self.ui.time_content.time()
        self.target.save_annotation(self, annotation)
        self.close()
        
    
    @QtCore.Slot()
    def cancel_annotation(self):
        if self.target:
            self.target.cancel_annotation(self)
            
        self.close()
        
    def load_annotation(self):
        if self.annotation.notification_icon_file:
            self.icon_path = self.annotation.notification_icon_file
            pixelmap = QtGui.QPixmap(self.annotation.notification_icon_file)
            pixelmap.scaledToHeight(self.ui.lbl_icon_display.height())
            self.ui.lbl_icon_display.setPixmap(pixelmap)
            self.ui.lbl_icon_display.setScaledContents(True)
            
        if self.annotation.notification_icon_timestamp:
            self.ui.time_icon.setTime(self.annotation.notification_icon_timestamp)     
            
        if self.annotation.notification_icon_duration:
            self.ui.cmb_icon_duration.setEditText(str(self.annotation.notification_icon_duration))
            
        if self.annotation.information_media:
            self.content_type = self.annotation.type
            self.content_path = self.annotation.information_media
            
            self.ui.cmb_content_type.setCurrentIndex(self.annotation.type)
            self.occult_content_displays()
        
            self.ui.txt_content.clear()
            self.ui.txt_content.appendPlainText(self.annotation.information_media)
        
            if self.annotation.type == Annotation.IMAGE:
                self.open_image(self.annotation.information_media)
            elif self.annotation.type == Annotation.AUDIO:
                self.open_music(self.annotation.information_media)
            elif self.annotation.type == Annotation.VIDEO:
                self.open_video(self.annotation.information_media)
            elif self.annotation.type == Annotation.HTML:
                self.open_html(self.annotation.information_media)
            
        if self.annotation.information_media_timestamp:
            self.ui.time_content.setTime(self.annotation.information_media_timestamp)
            
        if self.annotation.information_media_duration:
            print 'information_media_duration', self.annotation.information_media_duration
            self.ui.cmb_content_durartion.setEditText(
                                    str(self.annotation.information_media_duration))
        
    def init_ui(self):
        self.ui.btn_choose_icon.clicked.connect(self.choose_icon)
        self.ui.btn_choose_content.clicked.connect(self.choose_content)
        self.ui.btn_save.clicked.connect(self.save_annotation)
        self.ui.btn_cancel.clicked.connect(self.cancel_annotation)
        self.ui.btn_play.clicked.connect(self.start_playback)
        self.ui.btn_stop.clicked.connect(self.stop_playback)
        self.ui.btn_pause.clicked.connect(self.pause_playback)
        
        self.occult_content_displays()
    
    @QtCore.Slot()
    def start_playback(self):
        player = self.ui.video_player
        player.play()
        self.ui.btn_pause.setVisible(True)
        self.ui.btn_play.setVisible(False)
        self.ui.btn_stop.setEnabled(True)
        
    
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
        
        
    def occult_content_displays(self):
        self.ui.web_content.setVisible(False)
        self.ui.lbl_image_display.setVisible(False)
        self.ui.video_player.setVisible(False)
        self.ui.video_player.stop()
        self.ui.seek_slider.setVisible(False)
        self.ui.volume_slider.setVisible(False)
        self.ui.txt_content_display.setVisible(False)
        self.ui.btn_pause.setVisible(False)
        self.ui.btn_play.setVisible(False)
        self.ui.btn_stop.setVisible(False)
        
    
    @QtCore.Slot()
    def choose_icon(self):
        path, _ = QtGui.QFileDialog.getOpenFileName(self, 
                                                 u'Selecione o Ícone de notificação',
                                                 self.home_directory,
                                                 CONTENT_TYPES[Annotation.IMAGE])
        if path != None:            
            self.icon_path = path
            pixelmap = QtGui.QPixmap(path)
            pixelmap.scaledToHeight(self.ui.lbl_icon_display.height())
            self.ui.lbl_icon_display.setPixmap(pixelmap)
            self.ui.lbl_icon_display.setScaledContents(True)
            
    
    @QtCore.Slot()
    def choose_content(self):
        types = self.get_content_types()
        path, str_type = QtGui.QFileDialog.getOpenFileName(self, 
                                                 u'Selecione o conteúdo complementar',
                                                 self.home_directory,
                                                 types)
        file_type = self.parse_type(str_type)
        if not path:
            return
        
        self.ui.cmb_content_type.setCurrentIndex(file_type)
        self.occult_content_displays()
        
        self.ui.txt_content.clear()
        self.ui.txt_content.appendPlainText(path)
        
        self.content_type = file_type
        self.content_path = path
        
        if file_type == Annotation.IMAGE:
            self.open_image(path)
        elif file_type == Annotation.AUDIO:
            self.open_music(path)
        elif file_type == Annotation.VIDEO:
            self.open_video(path)
        elif file_type == Annotation.HTML:
            self.open_html(path)
    
    def open_image(self, path):
        pixelmap = QtGui.QPixmap(path)
        pixelmap.scaledToHeight(self.ui.lbl_image_display.height())
        self.ui.lbl_image_display.setPixmap(pixelmap)
        self.ui.lbl_image_display.setVisible(True)
        self.ui.lbl_image_display.setAlignment(QtCore.Qt.AlignCenter)
        #self.ui.setScaledContents(True)
        
    def open_video(self, path):
        print 'open_video'
        player = self.ui.video_player
        
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
        
    
    def open_music(self, path):
        player = self.ui.video_player
        
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
    
    def open_html(self, path):
        web = self.ui.web_content
        web.setVisible(True)
        web.setUrl(path)
    
    def open_plain_text(self, path):
        pass
        
    def parse_type(self, str_type):
        
        if str_type.count(u'Áudio') > 0:
            return Annotation.AUDIO
        elif str_type.count(u'Vídeo') > 0:
            return Annotation.VIDEO
        elif str_type.count(u'Imagens') > 0:
            return Annotation.IMAGE
        elif str_type.count(u'Texto Plano') > 0:
            return Annotation.PLAIN_TEXT
        elif str_type.count(u'Html') > 0:
            return Annotation.HTML
        
    def get_content_types(self):
        index = self.ui.cmb_content_type.currentIndex()        
        types = CONTENT_TYPES[index]
        for key, value in CONTENT_TYPES.items():
            if key != index:
                types += ';;' + value
        return types
        
        
class InformationAnnotation(Annotation):
    TYPE = "InformationAnnotation"
    
    def __init__(self, mid):
        Annotation.__init__(self, mid, 
                            name=u"Informação Simples",
                            mtype=InformationAnnotation.TYPE)
        
        self.notification_icon_file = None
        self.notification_icon_duration = None
        self.information_media = None
        self.information_media_timestamp = None
        self.information_media_duration = None
    
    def code_json(self):
        json_annotation = {}
        json_object = {"Annotation" : json_annotation}
        json_annotation['id'] = self.id
        json_annotation['content_type'] = Annotation.str_to_type[self.content_type]
        json_annotation['timestamp'] = self.timestamp.toString()
        json_annotation['type'] = self.type
        json_annotation['notification_icon_file'] = self.notification_icon_file
        json_annotation['notification_icon_duration'] = self.notification_icon_duration
        json_annotation['information_media'] = self.information_media
        json_annotation['information_media_timestamp'] = self.information_media_timestamp
        json_annotation['information_media_duration'] = self.information_media_duration
        return json_object
    
    @staticmethod
    def parse_json(json_object):
        json_annotation = json_object['Annotation']
        mid = json_annotation['id']
        mtype = json_annotation['type']
        if mtype != InformationAnnotation.TYPE:
            raise ValueError('The annotatoin is not a ' + InformationAnnotation.TYPE)
        
        annotation = InformationAnnotation(mid)
        annotation.content_type = Annotation.str_to_type[json_annotation['content_type']]
        annotation.timestamp = QtCore.QTime.fromString(json_annotation['timestamp'])
        
        annotation.notification_icon_file = json_annotation['notification_icon_file']
        annotation.notification_icon_duration = json_annotation['notification_icon_duration']
        annotation.information_media = json_annotation['information_media']
        annotation.information_media_timestamp = json_annotation['information_media_timestamp']
        annotation.information_media_duration = json_annotation['information_media_duration']
        return annotation
    
    @staticmethod
    def get_widget_class():
        return InformationAnnotationWidget
        
def test():
    import sys
    app = QtGui.QApplication(sys.argv)
    widget = InformationAnnotationWidget()
    sys.exit(app.exec_())
        
if __name__ == "__main__":
    test()