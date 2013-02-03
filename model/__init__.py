#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def invert_type_maps(original):
    inverted = {}
    for key, value in original.items():
        inverted[value] = key
            
    return inverted

class EnhancedMedia(object):
    def __init__(self, mid, name, main_media=None, description=None, last_modification=None, user_name=None):
        self.id = mid
        self.name = name
        self.description = description
        self.last_modification = last_modification
        self.user_name = user_name
        self.main_media = main_media
        self.__annotations = []
        
        
    def add_annotation(self, annotation):
        if not isinstance(annotation, Annotation):
            raise TypeError('The argument annotation must be an instance of Annotation.')
        
        #Its a new annotation
        if annotation not in self.__annotations:
            self.__annotations.append(annotation)
            self.__annotations_by_timestamp[annotation.timestamp] = annotation
        else:
            raise Exception('This annotation is already inserted.')            

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
    AUDIO = 0
    VIDEO = 1
    IMAGE = 2
    PLAIN_TEXT = 3
    HTML = 4
    
    type_to_str = {VIDEO : 'VIDEO',
                   PLAIN_TEXT : 'PLAIN_TEXT',
                   HTML : 'HTML',
                   AUDIO : 'AUDIO',
                   IMAGE : 'IMAGE'}
    
    str_to_type = invert_type_maps(type_to_str)
    
    def __init__(self, mid):
        self.__id = mid
        self.__type = Annotation.AUDIO
        
    @property
    def type(self):
        return self.__type
    
    @type.setter
    def type(self, value):
        if not Annotation.type_to_str.has_key(value):
            raise ValueError('The argument is a invalid Annotation type')
        
        self.__type = value
            
        
    @property
    def id(self):
        return self.__id
    
    @property
    def timestamp(self):
        return self.__timestamp
    
    @timestamp.setter
    def timestamp(self, new_timestap):
        if not isinstance(new_timestap, float):
            raise TypeError('The argument new_timestap must be an instance of float.')
        
        self.__timestamp = new_timestap
        
class AnnotationFactory(object):
    
    def __init__(self):
        self.__annotation_types = {}
        
    def add_annotation_type(self, ann_type, file_name=None, class_name=None):
        if self.__annotation_types.has_key(ann_type):
            raise Exception("There is another annotation with this type known.")
        
        if file_name == None:
            file_name = ann_type
        if class_name == None:
            class_name = ann_type
            
        self.__annotation_types[ann_type] = (file_name, class_name)
    
    def create_annotation(self, ann_type, mid):
        
        if not self.__annotation_types.has_key(ann_type):
            raise IndexError('There is no %s type of annotation known' % ann_type)
        
        file_name, class_name = self.__annotation_types[ann_type]
        __import__('model.' + file_name)
        mymodule = sys.modules['model.' + file_name]
        myclass = mymodule.__dict__[class_name]
        return myclass(mid)
    

CONTENT_TYPES = {Annotation.AUDIO : u'Áudio (*.wav *.mp3 *.ogg *.oga)',
                 Annotation.VIDEO : u'Vídeo (*.avi *.mp4 *.ogg *.webm *.mpeg)',
                 Annotation.HTML : u'Html (*.html *.htm)',
                 Annotation.IMAGE : u'Imagens (*.png *.jpg *.ico *.gif)',
                 Annotation.PLAIN_TEXT : u'Texto Plano (*.txt)'}
        

def test():
    ann_factory = AnnotationFactory()
    ann_factory.add_annotation_type('InformationAnnotation')
    annotation = ann_factory.create_annotation('InformationAnnotation', 'note 1')
    #annotation.test()
    
    annotation = ann_factory.create_annotation('InformationAnnotation', 'note 2')
    #annotation.test()
    
    
    print Annotation.str_to_type

if __name__ == "__main__":
    test()