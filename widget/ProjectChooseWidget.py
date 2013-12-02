#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
import os

from ui.ui_ProjectChooseWidget import Ui_ProjectChooseWidget
from MainProjectWidget import MainProjectWidget
import model
from datetime import datetime

class ProjectChooseWidget(QtGui.QWidget):
    PROJECTS_DIRECTORY = "AnnotationProjects"
    
    def __init__(self, real_path, home_directory, username, parent=None):
        super(ProjectChooseWidget, self).__init__(parent)
        self.real_path = real_path
        self.home_directory = home_directory
        self.username = username
         
        self.ui = Ui_ProjectChooseWidget()
        self.ui.setupUi(self)
        self.init_ui()
        self.show()
        
    def init_ui(self):
        self.ui.btn_create_project.setEnabled(False)
        self.ui.btn_open_project.setEnabled(False)
        
        self.ui.btn_create_project.clicked.connect(self.create_project)
        self.ui.btn_open_project.clicked.connect(self.open_project)
        self.ui.lst_projects.itemSelectionChanged.connect(self.atualize_open_button)
        
        self.ui.txt_project_id.textChanged.connect(self.atualize_create_button)
        self.ui.txt_project_name.textChanged.connect(self.atualize_create_button)
        
        
        
        self.detect_projects()    
    
        
    def detect_projects(self):        
        found_files = []
        existent_projects = []
        
        for file_name in os.listdir(os.path.join(self.home_directory, self.PROJECTS_DIRECTORY)):
            found_files.append(file_name)
            file_path = os.path.join(self.home_directory, self.PROJECTS_DIRECTORY, file_name)
            
            if os.path.isdir(file_path):
                project_file = os.path.join(file_path, 'project.json')
                if os.path.exists(project_file) and not os.path.isdir(project_file):
                    import codecs, json
                    try:
                        f = codecs.open(project_file, "r", "utf-8")
                        json_str = f.read()                        
                        project = model.AnnotationProject.parse_json(json.loads(json_str))
                        #project = model.AnnotationProject('id', 'name', 'main_media', 'description', 'modification', 'username')
                        existent_projects.append(project)
                    except:
                        print 'Problems reading the file', project_file
                    
                    
        #TODO: Order the projects by last modification
        lst_projects = self.ui.lst_projects
        for project in existent_projects:
            item = QtGui.QListWidgetItem()
            item.setText(project.id + ': ' + project.name)
            item.setSizeHint(QtCore.QSize(50,50))
            item._project = project
            lst_projects.addItem(item)
        
                
        candidate_index = 1
        candidate_id = 'myProject1'
        while found_files.count(candidate_id) > 0:
            candidate_index += 1
            candidate_id = 'myProject' + str(candidate_index)
            
        self.ui.txt_project_id.appendPlainText(candidate_id)

                
    @QtCore.pyqtSlot()
    def atualize_open_button(self):
        #selected = self.ui.lst_projects.currentItem()
        self.ui.btn_open_project.setEnabled(True)
        
    @QtCore.pyqtSlot()
    def atualize_create_button(self):
        if self.ui.txt_project_id.toPlainText() == "" or self.ui.txt_project_name.toPlainText() == "":
            self.ui.btn_create_project.setEnabled(False)
        else:
            self.ui.btn_create_project.setEnabled(True)
        
        
    @QtCore.pyqtSlot()
    def create_project(self):
        project_id = self.ui.txt_project_id.toPlainText()
        project_name = self.ui.txt_project_name.toPlainText()
        description = self.ui.txt_description_2.toPlainText()
        
        project_directory = os.path.join(self.home_directory, self.PROJECTS_DIRECTORY, str(project_id))
        if os.path.exists(project_directory):
            QtGui.QMessageBox.warning(self, u"Erro criando projeto.", 
                                      u"Já existe um arquivo ou diretório chamado %s. Por favor escolha outro identificador para o projeto." % project_id)
            
            self.ui.txt_project_id.clear()
            self.ui.txt_project_id.setFocus()
            return
        
        os.mkdir(project_directory)
        project = model.AnnotationProject(str(project_id), str(project_name), None, str(description), datetime.now(), self.username)
        project.directory = project_directory
        
        self.width = MainProjectWidget(project)
        self.close()

    
    @QtCore.pyqtSlot()
    def open_project(self):
        selected = self.ui.lst_projects.currentItem()
        print selected
        project = selected._project
        project_directory = os.path.join(self.home_directory, self.PROJECTS_DIRECTORY, project.id)
        
        self.width = MainProjectWidget(project, project_directory, self.serializator, self.plugins_manager)
        self.close()

 