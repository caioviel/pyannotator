from pyncl import *
import model
import os
import uuid

show_content_id = 1
media_count = 1

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
        
    
    def create_media(self, conent):
        media_count = self.media_count
        mid = None
        if conent.type == model.Media.IMAGE:
            mid = "image" + str(media_count) 
        elif conent.type == model.Media.VIDEO:
            mid = "video" + str(media_count)
        elif conent.type == model.Media.AUDIO:
            mid = "audio" + str(media_count) 
        elif conent.type == model.Media.TEXT:
            mid = "text" + str(media_count) 
        elif conent.type == model.Media.SLIDES:
            mid = "slides" + str(media_count)
            
        media = Media(mid, self.get_media_path(conent.filename))
        if conent.bondaries is not None:
            media.add_anchor(NodeProperty("bounds", 
                                          self.get_bounds_value(conent.bondaries)))
            
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
            
            port = Port("p" + media.id, component=media)
            self.ncldoc.add_anchor(port)

    def dump_file(self, filename):
        self.ncldoc.dump_file(filename)
    
    
def main():
    import codecs, json
    project_file = '/home/caioviel/AnnotationProjects/PROJETO_NCL/project.json'
    f = codecs.open(project_file, "r", "utf-8")
    json_str = f.read()                        
    project = model.AnnotationProject.parse_json(json.loads(json_str))
    nclgen = NclGenerator(project, GenerationOptions())
    nclgen.generate_ncl()
    nclgen.dump_file('/home/caioviel/AnnotationProjects/PROJETO_NCL/main.ncl')

if __name__ == "__main__":
    main()
    
    