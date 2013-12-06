from pyncl import *
import model
import os
import uuid
import util


class GenerationOptions(object):
    def __init__(self):
        self.width = 1280 
        self.height = 720

class NclGenerator():
    show_content_id = 1
    media_count = 1
    icon_count = 1
    
    def __init__(self, project, options):
        self.project = project
        self.options = options
        self.show_content_id = 1
        self.media_count = 1
        self.ncldoc = None
        
    def generate_ncl(self):
        self.ncldoc = NclDocument(self.project.id)
        
        self.ncldoc.add_imported_connector_base(
                        ImportedBase('conn', 'connBase.ncl'))
            
        self.generate_region_base()
            
        self.generate_descriptors()
            
        self.generate_body()
    
    
    def get_media_path(self, name):
        return os.path.split(name)[1]
    
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
        try:
            if content.bondaries is not None:
                media.add_anchor(NodeProperty("bounds", 
                                              self.get_bounds_value(content.bondaries)))
        except:
            pass
            
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
            area = Area('area_' + media.id, begin=content.showtime)
            self.mainVideo.add_anchor(area)
            
            medias.append( (content, media, area) )
        
        icon = self.add_icon(ann)
        
        if ann.interaction.compulsory:
            for c, m, a in medias:
                link = Link(xconnector='conn#onBeginStart')
                link.add_bind(Bind(role="onBegin", component=self.mainVideo, interface=a))
                link.add_bind(Bind(role="start", component=m))
                self.ncldoc.add_link(link)
        else:
            icon.add_anchor(NodeProperty("wasPressed", "NO"))
            link = Link(xconnector='conn#onKeySelectionSetStop')
            bind = Bind(role="onSelection", component=icon)
            bind.add_param("theKey", "GREEN")
            link.add_bind(bind)
            bind = Bind(role="set", component=icon, interface="wasPressed")
            bind.add_param("setValue", "YES")
            link.add_bind(bind)
            link.add_bind(Bind(role="stop", component=icon))
            self.ncldoc.add_link(link)
            
            for c, m, a in medias:
                link = Link(xconnector='conn#onBeginTestStart')
                link.add_bind(Bind(role="onBegin", component=self.mainVideo, interface=a))
                bind = Bind(role="propertyType", component=icon, interface="wasPressed")
                bind.add_param("testValue", "YES")
                link.add_bind(bind)
                link.add_bind(Bind(role="start", component=m))
                self.ncldoc.add_link(link)

    def dump_file(self, filename):
        self.generate_ncl()
        self.ncldoc.dump_file(filename)
        
    def add_icon(self, ann):
        icon = ann.interaction.icon
        url = None
        if icon.image == model.Icon.INFO:
            url = 'icon_info.png'
        elif icon.image == model.Icon.VIOLENCE:
            url = 'icon_violencia.png'
        elif icon.image == model.Icon.SEXUAL:
            url = 'icon_sexual.png'
        elif icon.image == model.Icon.YES:
            url = 'icon_yes.png'
        elif icon.image == model.Icon.NO:
            url = 'icon_no.png'
        else:
            url = self.get_media_path(icon.image)
            
        icon_id = 'icon' + str(self.icon_count)
        self.icon_count = self.icon_count + 1
        icon_media = Media(icon_id, url)
        icon_media.add_anchor(NodeProperty("explicitDur", 
                                          str(icon.duration_time)))
        icon_media.add_anchor(NodeProperty("bounds", 
                                          self.get_bounds_value(icon.bondaries)))
        
        self.ncldoc.add_node(icon_media)
        
        aux = util.qtime_to_sec(ann.annotation_time) - icon.relative_time
        icon_area = Area('area_' + icon_id, begin=aux)
        self.mainVideo.add_anchor(icon_area)
        
        link = Link(xconnector='conn#onBeginStart')
        link.add_bind(Bind(role="onBegin", component=self.mainVideo, interface=icon_area))
        link.add_bind(Bind(role="start", component=icon_media))
        self.ncldoc.add_link(link)
        
        return icon_media
            
        
    
    
def main():
    import codecs, json
    project_file = '/home/caioviel/AnnotationProjects/testeNCL/project.json'
    f = codecs.open(project_file, "r", "utf-8")
    json_str = f.read()                        
    project = model.AnnotationProject.parse_json(json.loads(json_str))
    project.directory = '/home/caioviel/AnnotationProjects/testeNCL'
    nclgen = NclGenerator(project, GenerationOptions())
    nclgen.dump_file('/home/caioviel/AnnotationProjects/testeNCL/medias/main.ncl')

if __name__ == "__main__":
    main()
    
    