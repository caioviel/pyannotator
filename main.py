#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from widget.ProjectChooseWidget import ProjectChooseWidget
import os
import sys
import getpass

import logging
logger = logging.getLogger('pyannotator')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(levelname)s - %(name)s: %(message)s'))
logger.addHandler(handler)

real_path, _ = os.path.split(os.path.realpath(__file__))
home_directory = os.getenv('USERPROFILE') or os.getenv('HOME')
username = getpass.getuser()


def create_project_directory():
    directory_to_create = os.path.join(home_directory, 
                                       ProjectChooseWidget.PROJECTS_DIRECTORY)
    
    if not os.path.exists(directory_to_create):
        os.mkdir(directory_to_create)
    elif not os.path.isdir(directory_to_create):
        print 'There is a file named AnnotationProjects into your home folder. Impossible to continue.'
        sys.exit(1)
    
                    
if __name__ == "__main__":
    create_project_directory()
    
    app = QtGui.QApplication(sys.argv)
    widget = ProjectChooseWidget(real_path, home_directory, username)
    sys.exit(app.exec_())