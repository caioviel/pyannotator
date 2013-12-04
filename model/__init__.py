#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
from PyQt4 import QtGui, QtCore
#from PySide import QtCore


class AnnotationProject(object):
    def __init__(self, mid, name, main_media=None, description=None, last_modification=None, username=None, directory=None):
        self.id = mid
        self.name = name
        self.main_media = main_media
        self.description = description
        self.last_modification = last_modification
        self.username = username
        self.directory = directory
        self.annotations = []
        
    @staticmethod
    def parse_json(json_object):
        project =  AnnotationProject(json_object['AnnotationProject']['id'],
                                         json_object['AnnotationProject']['name'],
                                         json_object['AnnotationProject']['main_media'],
                                         json_object['AnnotationProject']['description'])
        
        for json_ann in json_object['AnnotationProject']['annotations']:
            project.add_annotation(Annotation.parse_json(json_ann))
            
        return project
    
    def to_json(self):
        json_annotations = []
        json_object = {'AnnotationProject' : {
                                              "id" : self.id,
                                              "name" : self.name,
                                              "main_media" : self.main_media,
                                              "description" : self.description,
                                              "annotations" : json_annotations}}
        for ann in self.annotations:
            print ann
            json_annotations.append(ann.to_json())
            
        return json_object
        
    def generate_annotation_id(self):
        if len(self.annotations) > 0:
            return self.annotations[len(self.annotations)-1].id + 1
        else:
            return 1
    
    def remove_annotation(self, annotation):
        if not isinstance(annotation, Annotation):
            raise TypeError('The argument annotation must be an instance of Annotation.')
        
        #Its a new annotation
        try:
            self.annotations.remove(annotation)
        except:
            return False
        return True    
        
        
    def add_annotation(self, annotation):
        if not isinstance(annotation, Annotation):
            raise TypeError('The argument annotation must be an instance of Annotation.')
        
        #Its a new annotation
        if annotation not in self.annotations:
            self.annotations.append(annotation)
        else:
            raise Exception('This annotation is already inserted.') 
        
class Annotation(object):
    def __init__(self, myid, description=None, timestamp=None):
        self.id = myid
        self.timestamp = timestamp
        self.description = description
        self.annotation_time = None
        self.interaction = None
        
    @staticmethod
    def parse_json(json_object):
        ann =  Annotation(json_object['Annotation']['id'],
                              json_object['Annotation']['description'])
        
        
        ann.annotation_time = QtCore.QTime.fromString(json_object['Annotation']['annotation_time'])
        if json_object['Annotation'].has_key('interaction'):
            ann.interaction = Interaction.parse_json(json_object['Annotation']['interaction'])
        
        return ann
    
    def to_json(self):
        json_object = {'Annotation' : {
                                              "id" : self.id,
                                              "annotation_time" : unicode(self.annotation_time.toString()),
                                              "description" : unicode(self.description)}}
        
        if self.interaction is not None:
            json_object['Annotation']['interaction'] = self.interaction.to_json()
            
        return json_object
    
    @property
    def type(self):
        if self.interaction is None:
            return "Annotation"
        else:
            return self.interaction.type
        
        
    @property
    def pt_type(self):
        if self.interaction is None:
            return u"Anotação"
        else:
            return self.interaction.pt_type
        
        
class Media(object):
    AUDIO = 1
    VIDEO = 2
    IMAGE = 3
    TEXT = 4
    SLIDES = 5 
    
    def __init__(self, myid, filename, showtime):
        self.id = myid
        self.filename = filename
        
        #time configurations
        self.showtime = showtime
        self.begintime = None
        self.duration = None
        
CONTENT_TYPES = {Media.AUDIO : u'Áudio (*.wav *.mp3 *.ogg *.oga)',
                 Media.VIDEO : u'Vídeo (*.avi *.mp4 *.ogg *.webm *.mpeg)',
                 Media.IMAGE : u'Imagens (*.png *.jpg *.ico *.gif)',
                 Media.TEXT : u'Texto (*.txt *.html *.htm)',
                 Media.SLIDES : u''}

class Bondaries(object):
    def __init__(self, top=-1, left=-1, width=-1, height=-1):
        self.top = top
        self.left = left
        self.width = width
        self.height = height
        
    def __str__(self):
        return str((self.left, self.top, self.width, self.height))
        
        
class Audio(Media):
    def __init__(self, myid, filename, showtime):
        super(Audio, self).__init__(myid, filename, showtime)
        self.main_video_volume = None
        self.media_volume = None
        
class Video(Media):
    def __init__(self, myid, filename, showtime):
        super(Video, self).__init__(myid, filename, showtime)
        self.bondaries = None
        self.resize_main_video = None
        self.main_video_volume = None
        self.media_volume = None

class Text(Media):
    def __init__(self, myid, filename, showtime, duration=5):
        super(Text, self).__init__(myid, filename, showtime)
        self.duration = duration
        self.bondaries = None
        self.resize_main_video = None
        self.text = None
        self.font = None
        self.fontSize = None
        self.bold = None
        self.italic = None
        self.sublimed = None
        self.font_color = None
        self.bg_color = None
        self.bg_transparency = False
        self.alling = False
        
        

class Image(Media):
    def __init__(self, myid, filename, showtime, duration=5):
        super(Image, self).__init__(myid, filename, showtime)
        self.duration = duration
        self.bondaries = None
        self.resize_main_video = None

class Slides(Media):
    def __init__(self, myid, filename, showtime):
        super(Slides, self).__init__(myid, filename, showtime)
        self.slides = []
        self.transition_time = 2
        self.auto_transition = True
        self.resize_main_video = None
    
    def add_slide(self, image, position=None):
        if not isinstance(image, Image):
            raise TypeError('The argument image must be an instance of Image.')
        
        if position is None:
            self.slides.append(image)
        else:
            self.slides.insert(position, image)
        
class Icon(object):
    #Colocar as imagens aqui no icone como variaveis
    
    def __init__(self, image, relative_time, duration_time):
        self.image = image
        self.relative_time = relative_time
        self.duration_time = duration_time
        self.bondaries = None

class Interaction(object):
    def __init__(self):
        pass

class ShowContent(Interaction):
    def __init__(self):
        super(ShowContent, self).__init__()
        self.contents = []
        self.icon = None
        self.compulsory = False
        self.pause_main_video = False
        self.allow_end_content = True
        self.tv = True
        self.mobile = False
        
        
        
    def add_content(self, content):
        if not isinstance(content, Media):
            raise TypeError('The argument content must be an instance of Media.')
        
        if content not in self.contents:
            self.contents.append(content)
        else:
            raise Exception('This content is already inserted.')
        
    def remove_content(self, content):
        if not isinstance(content, Media):
            raise TypeError('The argument content must be an instance of Media.')
        
        self.contents.remove(content)
        
    @property
    def type(self):
        return "Content"
        
        
    @property
    def pt_type(self):
        return u"Conteúdo"

                        
class Skip(Interaction):
    @property
    def type(self):
        return "Skip"
        
        
    @property
    def pt_type(self):
        return u"Pular"

class Poll(Interaction):
    @property
    def type(self):
        return "Poll"
        
    @property
    def pt_type(self):
        return u"Enquete"

class Replay(Interaction):
    @property
    def type(self):
        return "Replay"
        
    @property
    def pt_type(self):
        return u"Retroceder"
    


def test():
    pass

if __name__ == "__main__":
    test()