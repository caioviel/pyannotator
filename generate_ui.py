#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess as sp

DIRECTORY = "ui"
RCC = "pyrcc4"
UIC = "pyuic4"

if __name__ == "__main__":
    all_files = os.listdir(DIRECTORY)
    all_files.sort()
    for mfile in all_files:
        if ".qrc" in mfile and not "~" in mfile:
            print mfile
            oname = mfile[:mfile.find(".")] + '_rc.py'
            f = open(os.path.join(DIRECTORY, oname), 'w')
            
            sp.call(args=[RCC, os.path.join(DIRECTORY, mfile)], stdout=f)
            f.close()
    
    for mfile in all_files:
        if ".ui" in mfile and not "~" in mfile:
            print mfile
            oname = "ui_" +  mfile[:mfile.find(".")] + '.py'
            f = open(os.path.join(DIRECTORY, oname), 'w')
            
            sp.call(args=[UIC, os.path.join(DIRECTORY, mfile)], stdout=f)
            f.close()