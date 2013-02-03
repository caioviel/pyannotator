#!/usr/bin/env python
# -*- coding: utf-8 -*-

from model import Annotation, CONTENT_TYPES
from PySide import QtGui, QtCore
from PySide.phonon import Phonon
from ui.ui_InformationAnnotationWidget import Ui_InformationAnnotationWidget

class InformationAnnotation(Annotation):
    def __init__(self, mid):
        Annotation.__init__(self, mid)
        
        self.notification_icon_file = None
        self.notification_icon_timestamp = None
        self.notification_icon_duration = None
        self.information_media = None
        self.information_media_timestamp = None
        self.information_media_duration = None
        
        

        
    
class InformationAnnotationWidget(QtGui.QDialog):
    
    def __init__(self, annotation=None, target=None, parent=None):
        super(InformationAnnotationWidget, self).__init__(parent)
        self.ui = Ui_InformationAnnotationWidget()
        self.ui.setupUi(self)
        self.annotation = annotation
        self.target = target
        if self.annotation == None:
            self.annotation = InformationAnnotation("MyId")
        else:
            self.load_annotation()
        
        self.init_ui()
        
        self.__original_size = self.size()
        
        import os
        self.home_directory =  os.getenv('USERPROFILE') or os.getenv('HOME')
        
        self.show()
        
    def load_annotation(self):
        print 'load_annotation'
        if self.annotation.notification_icon_timestamp:
            self.ui.time_icon.setTime(self.annotation.notification_icon_timestamp)
        
    def init_ui(self):
        self.ui.btn_choose_icon.clicked.connect(self.choose_icon)
        self.ui.btn_choose_content.clicked.connect(self.choose_content)
        self.occult_content_displays()
        
        
        self.ui.btn_play.clicked.connect(self.start_playback)
        self.ui.btn_stop.clicked.connect(self.stop_playback)
        self.ui.btn_pause.clicked.connect(self.pause_playback)
    
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
        
        
        
        
def test():
    import sys
    app = QtGui.QApplication(sys.argv)
    widget = InformationAnnotationWidget()
    sys.exit(app.exec_())
        
if __name__ == "__main__":
    test()