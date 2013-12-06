from pyncl import *
import model
import os
import uuid

show_content_id = 1
media_count = 1
icon_count = 1

class GenerationOptions(object):
    def __init__(self):
        self.width = 1280 
        self.height = 720

class NclGenerator():
    def __init__(self, project, options):
        self.project = project
        self.options = options
        self.show_content_id = 1
        self.media_count = 1
        self.ncldoc = None
        
    def generate_ncl(self):
        self.ncldoc = NclDocument(self.project.id)
            
        self.generate_region_base()
            
        self.generate_descriptors()
            
        self.generate_body()
    
    
    def get_media_path(self, name):
        return os.path.join('medias', os.path.split(name)[1])
    
    def get_bounds_value(self, bounds):
        height = self.options.height * bounds.height / bounds.screen_height
        width = self.options.width * bounds.width / bounds.screen_width
        top = self.options.height * bounds.top / bounds.screen_height
        left = self.options.width * bounds.left / bounds.screen_width
        
        return "%d,%d,%d,%d" % (left, top, width, height)
        
    
    def create_media(self, content):
        media_count = self.media_count
        mid = None
        if content.type == model.Media.IMAGE:
            mid = "image" + str(media_count) 
        elif content.type == model.Media.VIDEO:
            mid = "video" + str(media_count)
        elif content.type == model.Media.AUDIO:
            mid = "audio" + str(media_count) 
        elif content.type == model.Media.TEXT:
            mid = "text" + str(media_count) 
        elif content.type == model.Media.SLIDES:
            mid = "slides" + str(media_count)
            
        media = Media(mid, self.get_media_path(content.filename))
        if content.bondaries is not None:
            media.add_anchor(NodeProperty("bounds", 
                                          self.get_bounds_value(content.bondaries)))
            
        if content.duration is not None:
            media.add_anchor(NodeProperty("explicitDur", 
                                          str(content.duration)))
            
        self.media_count = self.media_count +1
        return media
        
    
    def generate_region_base(self):
        rgScreen = Region("rgScreen", width=self.options.width, 
                          height=self.options.height, zIndex=0)
        self.ncldoc.region_base.append(rgScreen)
    
    def generate_descriptors(self):
        descriptor = Descriptor("dScreen", region="rgScreen")
        self.ncldoc.descriptor_base.append(descriptor)
    
    def generate_body(self):
        self.mainVideo = Media('mainVideo', 
                          src=self.get_media_path(self.project.main_media), 
                          descriptor="dScreen")
        
        self.ncldoc.add_node(self.mainVideo)
        
        port = Port("pMainVideo", component=self.mainVideo)
        self.ncldoc.add_anchor(port)
        
        
        for ann in self.project.annotations:
            if ann.interaction is not None:
                if isinstance(ann.interaction, model.ShowContent):
                    self.generate_show_content(ann)
    
    def generate_show_content(self, ann):
        medias = []
        for content in ann.interaction.contents:
            media = self.create_media(content)
            self.ncldoc.add_node(media)
            medias.append( (medias, content) )
            
        if ann.interaction.icon is not None:
            self.add_icon(ann)
            

    def dump_file(self, filename):
        self.ncldoc.dump_file(filename)
        
    def add_icon(self, ann):
        icon = ann.interaction.icon
        url = None
        if icon.image == model.Icon.INFO:
            url = os.path.join('medias', 'icon_info.png')
        elif icon.image == model.Icon.VIOLENCE:
            url = os.path.join('medias', 'icon_violencia.png')
        elif icon.image == model.Icon.SEXUAL:
            url = os.path.join('medias', 'icon_sexual.png')
        elif icon.image == model.Icon.YES:
            url = os.path.join('medias', 'icon_yes.png')
        elif icon.image == model.Icon.NO:
            url = os.path.join('medias', 'icon_no.png')
        else:
            url = self.get_media_path(icon.image)
            
        icon_id = 'icon' + str(icon_count)
        icon_count = icon_count + 1
        icon_media = Media(icon_id, url)
        icon_media.add_anchor(NodeProperty("explicitDur", 
                                          str(icon.duration_time)))
        
        self.ncldoc.add_node(icon_media)
        
        icon_area = Area('area_' + icon_id, begin=ann.annotation_time - icon.relative_time)
        self.mainVideo.add_anchor(icon_area)
            
        
    
    
def main():
    import codecs, json
    project_file = '/home/caioviel/AnnotationProjects/testeNcl/project.json'
    f = codecs.open(project_file, "r", "utf-8")
    json_str = f.read()                        
    project = model.AnnotationProject.parse_json(json.loads(json_str))
    project.directory = '/home/caioviel/AnnotationProjects/testeNcl'
    nclgen = NclGenerator(project, GenerationOptions())
    nclgen.generate_ncl()
    nclgen.dump_file('/home/caioviel/AnnotationProjects/testeNcl/main.ncl')

if __name__ == "__main__":
    main()
    
    