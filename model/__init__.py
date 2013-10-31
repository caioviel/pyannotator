#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
#from PySide import QtCore


class AnnotationProject(object):
    def __init__(self, mid, name, main_media=None, description=None, last_modification=None, username=None):
        self.id = mid
        self.name = name
        self.main_media = main_media
        self.description = description
        self.last_modification = last_modification
        self.username = username
        
        self.annotations = []
    
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
        
class SpatialMedia(Media):
    def __init__(self, myid, filename, showtime,
                 top=None, left=None, 
                 height=None, width=None):
        
        super(SpatialMedia, self).__init__(myid, filename, showtime)
        
        self.top = top
        self.left = left
        self.height = height
        self.width = width
        
class Audio(Media):
    def __init__(self, myid, filename, showtime):
        super(Audio, self).__init__(myid, filename, showtime)
        
class Video(SpatialMedia):
    def __init__(self, myid, filename, showtime):
        super(Video, self).__init__(myid, filename, showtime)

class Text(SpatialMedia):
    def __init__(self, myid, filename, showtime, duration=5):
        super(Text, self).__init__(myid, filename, showtime)
        self.duration = duration

class Image(SpatialMedia):
    def __init__(self, myid, filename, showtime, duration=5):
        super(Image, self).__init__(myid, filename, showtime)
        self.duration = duration

class Slides(SpatialMedia):
    def __init__(self, myid, filename, showtime):
        super(Slides, self).__init__(myid, filename, showtime)
        self.slides = []
        self.transition_time = 2
        self.auto_transition = True
    
    def add_slide(self, image, position=None):
        if not isinstance(image, Image):
            raise TypeError('The argument image must be an instance of Image.')
        
        if position is None:
            self.slides.append(image)
        else:
            self.slides.insert(position, image)

class VideoStream(object):
    def __init__(self, media_source):
        self.media_source = media_source
        self.__openned = False
        self.__fps = None
        self.__width = None
        self.__height = None
        self.__duration = None
        
    def open(self):
        pass
    
    @property
    def fps(self):
        return self.__fps
    
    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    @property
    def duration(self):
        return self.__duration
    
class Annotation(object):
    def __init__(self, myid, timestamp):
        self.id = id
        self.timestamp = timestamp
        self.description = None
        self.annotation_time = None
        
class Icon(object):
    #Colocar as imagens aqui no icone como variaveis
    
    def __init__(self, image, relative_time, position):
        self.image = image
        self.relative_time = relative_time
        self.position = position

class Interaction(object):
    def __init__(self):
        self.resize_main_video = None
        self.compulsory = False
        self.pause_main_video = False

class ShowContent(Interaction):
    def __init__(self):
        super(ShowContent, self).__init__()
        self.contents = []
        
        
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
                        
class Skip(Interaction):
    pass

class Poll(Interaction):
    pass

class Replay(Interaction):
    pass

class InternalLink(Interaction):
    pass
    


def test():
    pass

if __name__ == "__main__":
    test()