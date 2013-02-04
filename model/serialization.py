import model
import json


class AnnotationSerializator:
    def parse_json(self, annotation):
        pass
    
    def code_json(self, annotation):
        pass

class ProjectSerializator:
    def __init__(self, plugins_manager):
        self.plugins_manager = plugins_manager
    
    def parse_file(self, filename):
        #open file, get the code
        json_str = ''
        return self.parse_json(json_str)
    
    def dump_file(self, project, filename):
        json_str = self.code_json(project)
        #Create file and write
    
    def code_json(self, project):
        #if not isinstance(project, model.AnnotationProject):
        #    raise TypeError('The argument project must be an instance of AnnotationProject.')
        
  
        json_project = {}
        json_object = {'AnnotationProject' : json_project}
        json_project['id'] = project.id
        json_project['name'] = project.name
        #if project.main_media:
        json_project['main_media'] = project.main_media
            
        #if project.description:
        json_project['description'] = project.description
        
        #if project.last_modification:
        json_project['last_modification'] = project.last_modification
            
        #if project.username:
        json_project['username'] = project.username
            
        json_annotations = []
        json_project['annotations'] = json_annotations
        
        note_serializator = AnnotationSerializator()
        for annotation in project.annotations:
            json_note = note_serializator.code_json(annotation)
            json_annotations.append(json_note)
            
        return json.dumps(json_object)
        
    
    def parse_json(self, json_str):
        json_object = json.loads(json_str)
        json_project = json_object['AnnotationProject']
        mid = json_project['id']
        name = json_project['name']
        project = model.AnnotationProject(mid, name)
        project.main_media = json_project['main_media']
        project.description = json_project['description']
        project.last_modification = json_project['last_modification']
        project.username = json_project['username']
        
        json_annotations = json_project['annotations']
        for json_ann in json_annotations:
            if json_ann == None:
                continue
            mtype = json_ann['Annotation']['type']
            annotation_class = self.plugins_manager.get_annotation_class(mtype)
            annotation = annotation_class.parse_json(json_ann)
            project.add_annotation(annotation)
            
        return project
        
    




def test():
    pass

if __name__ == "__main__":
    test()