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
    
    def get_full_screen_bounds(self):
        return "0,0," + str(self.options.width) + "," + str(self.options.height)
    
    def get_volume_float(self, value):
        fvalue = float(value)/100.0
        return "%.2f" % fvalue
        
    
    def __init__(self, project, options):
        import pyncl
        pyncl.clear()
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
        
        return "%d,%d,%d,%d" % (abs(left), abs(top), 
                                abs(width), abs(height))
        
    
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
        
        try:
            if content.media_volume is not None:
                media.add_anchor(NodeProperty("soundLevel", 
                                              self.get_volume_float(content.media_volume)))
        except:
            pass
            
        if content.duration is not None and content.duration > 0:
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
        
        self.mainVideo.add_anchor(NodeProperty("bounds"))
        self.mainVideo.add_anchor(NodeProperty("soundLevel", "1.0"))
        
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
        
        icon, sound = self.add_icon(ann)
        
        area_skip = None
        area_back = None
        area_internal_link = None
        
        area_ann = Area('area_annotation_' + icon.id,
                               begin=util.qtime_to_sec(ann.annotation_time))
        self.mainVideo.add_anchor(area_ann)
        
        area_ann_return = Area('area_annotation_ret' + icon.id,
                               begin=util.qtime_to_sec(ann.annotation_time) + 1)
        self.mainVideo.add_anchor(area_ann_return)
        
        if ann.interaction.interaction_type == model.ShowContent.SKIP:
            area_skip = Area('area_skip_' + icon.id, begin=ann.interaction.skip_point)
            self.mainVideo.add_anchor(area_skip)
            if ann.interaction.compulsory:
                link = Link(xconnector='conn#onBeginAbortStart')
                link.add_bind(Bind(role="onBegin", component=self.mainVideo, interface=area_ann))
                link.add_bind(Bind(role="abort", component=self.mainVideo))
                link.add_bind(Bind(role="start", component=self.mainVideo, interface=area_skip))
                self.ncldoc.add_link(link)
            else:
                link = Link(xconnector='conn#onBeginTestAbortStart')
                link.add_bind(Bind(role="onBegin", component=self.mainVideo, interface=area_ann))
                bind = Bind(role="propertyType", component=icon, interface="wasPressed")
                bind.add_param("testValue", "YES")
                link.add_bind(bind)
                link.add_bind(Bind(role="abort", component=self.mainVideo))
                link.add_bind(Bind(role="start", component=self.mainVideo, interface=area_skip))
                self.ncldoc.add_link(link)
            
        elif ann.interaction.interaction_type == model.ShowContent.BACK_5:
            area_back = Area('area_back_' + icon.id, begin=util.qtime_to_sec(ann.annotation_time)-5)
            self.mainVideo.add_anchor(area_back)
            
            if ann.interaction.compulsory:
                link = Link(xconnector='conn#onBeginTestSetAbortStart')
                link.add_bind(Bind(role="onBegin", component=self.mainVideo, interface=area_ann))
                bind = Bind(role="propertyType", component=icon, interface="isInteraction")
                bind.add_param("testValue", "NO")
                link.add_bind(bind)
                bind = Bind(role="set", component=icon, interface="isInteraction")
                bind.add_param("setValue", "YES")
                link.add_bind(bind)
                link.add_bind(Bind(role="abort", component=self.mainVideo))
                link.add_bind(Bind(role="start", component=self.mainVideo, interface=area_back))
                self.ncldoc.add_link(link)
            else:
                link = Link(xconnector='conn#onBeginTestSetAbortStart')
                link.add_bind(Bind(role="onBegin", component=self.mainVideo, interface=area_ann))
                bind = Bind(role="propertyType", component=icon, interface="wasPressed")
                bind.add_param("testValue", "YES")
                link.add_bind(bind)
                bind = Bind(role="set", component=icon, interface="isInteraction")
                bind.add_param("setValue", "YES")
                link.add_bind(bind)
                bind = Bind(role="set", component=icon, interface="wasPressed")
                bind.add_param("setValue", "NO")
                link.add_bind(bind)
                link.add_bind(Bind(role="abort", component=self.mainVideo))
                link.add_bind(Bind(role="start", component=self.mainVideo, interface=area_back))
                self.ncldoc.add_link(link)
            
            
            
        elif ann.interaction.interaction_type == model.ShowContent.BACK_TO:
            
            area_internal_link = Area('area_internal_link_' + icon.id, 
                             begin=ann.interaction.back_point,
                             end=ann.interaction.back_limite)
            self.mainVideo.add_anchor(area_internal_link)
            
            if ann.interaction.compulsory:
                link = Link(xconnector='conn#onBeginSetAbortStart')
                link.add_bind(Bind(role="onBegin", component=self.mainVideo, interface=area_ann))
                bind = Bind(role="set", component=icon, interface="isInteraction")
                bind.add_param("setValue", "YES")
                link.add_bind(bind)
                link.add_bind(Bind(role="abort", component=self.mainVideo))
                link.add_bind(Bind(role="start", component=self.mainVideo, interface=area_internal_link))
                self.ncldoc.add_link(link)
            else:
                link = Link(xconnector='conn#onBeginTestSetAbortStart')
                link.add_bind(Bind(role="onBegin", component=self.mainVideo, interface=area_ann))
                bind = Bind(role="propertyType", component=icon, interface="wasPressed")
                bind.add_param("testValue", "YES")
                link.add_bind(bind)
                bind = Bind(role="set", component=icon, interface="isInteraction")
                bind.add_param("setValue", "YES")
                link.add_bind(bind)
                link.add_bind(Bind(role="abort", component=self.mainVideo))
                link.add_bind(Bind(role="start", component=self.mainVideo, interface=area_internal_link))
                self.ncldoc.add_link(link)
                
                
            link = Link(xconnector='conn#onEndTestAbortStart')
            link.add_bind(Bind(role="onEnd", component=self.mainVideo, interface=area_internal_link))
            bind = Bind(role="propertyType", component=icon, interface="isInteraction")
            bind.add_param("testValue", "YES")
            link.add_bind(bind)
            link.add_bind(Bind(role="abort", component=self.mainVideo))
            link.add_bind(Bind(role="start", component=self.mainVideo, interface=area_ann_return))
            self.ncldoc.add_link(link)
                
            
            
        
        if ann.interaction.compulsory:
            link = Link(xconnector="conn#onBeginSet")
            link.add_bind(Bind(role="onBegin", component=self.mainVideo, interface=area_ann))
            b = Bind(role="set", component=icon, interface="isInteraction")
            b.add_param("setValue", "YES")
            link.add_bind(b)
            self.ncldoc.add_link(link)
            
            
            for c, m, a in medias:
                link = Link(xconnector='conn#onBeginStart')
                link.add_bind(Bind(role="onBegin", component=self.mainVideo, interface=a))
                link.add_bind(Bind(role="start", component=m))
                self.ncldoc.add_link(link)
                
            
        else:
            icon.add_anchor(NodeProperty("wasPressed", "NO"))
            link = Link(xconnector='conn#onKeySelectionSetStop')
            bind = Bind(role="onSelection", component=icon)
            bind.add_param("theKey", ann.interaction.button)
            link.add_bind(bind)
            bind = Bind(role="set", component=icon, interface="wasPressed")
            bind.add_param("setValue", "YES")
            link.add_bind(bind)
            bind = Bind(role="set", component=icon, interface="isInteraction")
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
                
        #Resize de medias
        for c, m, a in medias:
            try:
                if c.resize_main_video is not None:
                    link = Link(xconnector="conn#onBeginSet")
                    link.add_bind(Bind(role="onBegin", component=m))
                    bind = Bind(role="set", component=self.mainVideo, 
                                interface="bounds")
                    bind.add_param("setValue", self.get_bounds_value(c.resize_main_video))
                    link.add_bind(bind)
                    self.ncldoc.add_link(link)
                    
                    
                    link = Link(xconnector="conn#onEndSet")
                    link.add_bind(Bind(role="onEnd", component=m))
                    bind = Bind(role="set", component=self.mainVideo, 
                                interface="bounds")
                    bind.add_param("setValue", self.get_full_screen_bounds())
                    link.add_bind(bind)
                    self.ncldoc.add_link(link)
            except:
                pass
            
            try:
                if c.main_video_volume is not None and \
                        c.media_volume is not None:
                    
                    link = Link(xconnector="conn#onBeginSet")
                    link.add_bind(Bind(role="onBegin", component=m))
                    bind = Bind(role="set", component=self.mainVideo, 
                                interface="soundLevel")
                    bind.add_param("setValue", self.get_volume_float(c.main_video_volume))
                    link.add_bind(bind)
                    self.ncldoc.add_link(link)
                    
                    
                    link = Link(xconnector="conn#onEndSet")
                    link.add_bind(Bind(role="onEnd", component=m))
                    bind = Bind(role="set", component=self.mainVideo, 
                                interface="soundLevel")
                    bind.add_param("setValue", "1.0")
                    link.add_bind(bind)
                    self.ncldoc.add_link(link)
            except:
                pass
            
        if ann.interaction.pause_main_video == True:
            for c, m, a in medias:
                link = Link(xconnector="conn#onBeginPause")
                link.add_bind(Bind(role="onBegin", component=m))
                link.add_bind(Bind(role="pause", component=self.mainVideo))
                self.ncldoc.add_link(link)
                        
                link = Link(xconnector="conn#onEndResume")
                link.add_bind(Bind(role="onEnd", component=m))
                link.add_bind(Bind(role="resume", component=self.mainVideo))
                self.ncldoc.add_link(link)
                
                
        if ann.interaction.allow_end_content == True:
            for c, m, a in medias:
                link = Link(xconnector="conn#onKeySelectionStop")
                b = Bind(role="onSelection", component=m)
                b.add_param("theKey", "RED")
                link.add_bind(b)
                link.add_bind(Bind(role="stop", component=m))
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
        icon_media.add_anchor(NodeProperty("isInteraction", "NO"))
        
        self.ncldoc.add_node(icon_media)
        
        
        
        aux = util.qtime_to_sec(ann.annotation_time) - icon.relative_time
        icon_area = Area('area_' + icon_id, begin=aux)
        self.mainVideo.add_anchor(icon_area)
        
        link = Link(xconnector='conn#onBeginStart')
        link.add_bind(Bind(role="onBegin", component=self.mainVideo, interface=icon_area))
        link.add_bind(Bind(role="start", component=icon_media))
        self.ncldoc.add_link(link)
        
        audio_media = None
        sound_alert = ann.interaction.sound_alert
        if sound_alert is not None:
            audio_media = Media(icon_id + '_audio', 
                            src=self.get_media_path(sound_alert))
            
            self.ncldoc.add_node(audio_media)
            
            link = Link(xconnector='conn#onBeginStart')
            link.add_bind(Bind(role="onBegin", component=icon_media))
            link.add_bind(Bind(role="start", component=audio_media))
            self.ncldoc.add_link(link)
            
            link = Link(xconnector='conn#onEndStop')
            link.add_bind(Bind(role="onEnd", component=icon_media))
            link.add_bind(Bind(role="stop", component=audio_media))
            self.ncldoc.add_link(link)
        
        return icon_media, audio_media

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
    
    
