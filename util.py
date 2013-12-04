import shutil
import os
from PyQt4 import QtGui, QtCore


def copy_to_directory(project, path):
    filename = os.path.split(path)[1]
    print filename
    media_directory = os.path.join(unicode(project.directory), "medias")
    print media_directory
    
    if not os.path.exists(media_directory):
        os.mkdir(media_directory)
    
    final_path = os.path.join(media_directory, filename)
    count = 2
    no_extension = filename[:filename.find('.')]
    extension = filename[filename.find('.'):]
    while os.path.exists(final_path):
        final_path = no_extension + str(count)  + extension
        final_path = os.path.join(media_directory, final_path)
        count = count + 1
    
    print final_path
    shutil.copy(path, final_path)
    return final_path

def qtime_to_sec(qtime):
    hour = qtime.hour()
    minute = qtime.minute()
    sec = qtime.second()
    return hour*60*60 + minute*60 + sec

def sec_to_qtime(sec):
    qtime = QtCore.QTime()
    _min = sec/60
    sec = sec%60
    hour = _min/60
    _min = _min%60
    
    qtime.setHMS(hour, _min, sec)
    return qtime
        
                          
    
    