#!/usr/bin/env python
# -*- coding: utf-8 -*-

#HTTP_DIRECTORY = "/home/caioviel/public_html"
HTTP_DIRECTORY = "c:/www"
HTTP_PORT = 80
IP_ADDRESS = "192.168.98.198"
BROKER_STOMP = 61613
BROKER_WEB = 61614
CONTROL_TOPIC = '/topic/control'
PRESENTATION_TOPIC = '/topic/presentation'

import logging
logging.basicConfig(level=logging.DEBUG)


import communication
import generation
import os
import logging
import model
import time
import json
import shutil
import codecs

def generate_html(table, broker_add, broker_port, topic):
    
                            
    current_path = os.path.dirname(os.path.realpath(__file__))
    files_path = os.path.join(current_path, 'files')
    header_path = os.path.join(files_path, "exibition_begin.html")
    footer_path = os.path.join(files_path, "exibition_end.html")
    
    f = codecs.open(header_path, "r", "utf-8")
    header = f.read()
    
    f = codecs.open(footer_path, "r", "utf-8")
    footer = f.read()
    
    
    html_code = u'\nBROKER_ADDRESS = "ws://' + broker_add + ':' + str(broker_port)+ '";\n'
    html_code += u'DESTINATION = "' + CONTROL_TOPIC + '";\n'
    if len(table) > 0:
        html_code += u'mobile_nodes = {\n'
        for key, value in table.items():
            html_code += '"' + key + '" : ["' + value[0] + '", "' + value[1] + '"],\n'
    html_code += "};\n\n\n"
    
    html_full = header + html_code + footer
    html_name = os.path.join(HTTP_DIRECTORY, 'project', 'exibition.html')
    f = codecs.open(html_name, "w", "utf-8")
    f.write(html_full)
    

def load_project():
    project_directory = os.path.join(HTTP_DIRECTORY, "project")
    
    project_file = os.path.join(project_directory, 'project.json')
    if os.path.exists(project_file) and not os.path.isdir(project_file):
        import codecs, json

        f = codecs.open(project_file, "r", "utf-8")
        json_str = f.read()                        
        project = model.AnnotationProject.parse_json(json.loads(json_str), project_directory)
        #project = model.AnnotationProject('id', 'name', 'main_media', 'description', 'modification', 'username')
        return project
    

def get_ncl_file_name():
    return os.path.join(HTTP_DIRECTORY, "project", "medias", "main.ncl")

def remove_accents(input_str):
    import unicodedata
    nkfd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nkfd_form.encode('ASCII', 'ignore')
    return only_ascii
    

def put_url(project):
    url_path_base = "http://" + IP_ADDRESS + ":" + str(HTTP_PORT) + "/project/medias/"
    
    for ann in project.annotations:
        if ann.interaction is not None:
            for content in ann.interaction.contents:
                if content.type == model.Media.TEXT:
                    content.filename = filename = create_text_file(content)
                
                dir, filename = os.path.split(content.filename)
                filaname_ascii = remove_accents(filename)
                fullpath_ascii = os.path.join(dir, filaname_ascii)
                if not os.path.exists(fullpath_ascii):
                    shutil.copy(content.filename, fullpath_ascii)
                
                content.url = url_path_base + filaname_ascii
                print 'url:', content.url
                
def create_text_file(content):
    filename = content.filename[:content.filename.find('.')] + '.txt'
    print filename
    f = codecs.open(filename, "w", "utf-8")
    f.write(content.text)
    return filename
    

def publish_project(project, session):
    json_object = project.to_json()
    json_str = json.dumps(json_object)
    print json_str
    session.send_message(json_str)
    

def create_lua_file():
    pass

def main():
    import uuid
    session = communication.CommSession(address=IP_ADDRESS, 
                              port=BROKER_STOMP, 
                              destination=CONTROL_TOPIC)
    session.connect()
    
    project = load_project()
    project.id = str(uuid.uuid4())
    
    print 'project loaded'
    
    filename = get_ncl_file_name()
    print 'NCL Filename:', filename
    
    options = generation.GenerationOptions()
    options.width = 1024
    options.height = 576
    #options.broker_address = IP_ADDRESS
    #options.broker_port = BROKER_STOMP
    #options.topic = PRESENTATION_TOPIC
    
    ncl_generator = generation.NclGenerator(project, options)
    ncl_generator.dump_file(filename)
    
    create_lua_file()
    
    put_url(project)
    
    generate_html(ncl_generator.lua_table, IP_ADDRESS, BROKER_WEB, PRESENTATION_TOPIC)
    
    publish_project(project, session)
    
    while True:
        print 'running...'
        time.sleep(5)
        
        
        
        
    
if __name__ == "__main__":
    main()
    
    
    