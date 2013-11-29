import shutil
import os


def copy_to_directory(project, path):
    filename = os.path.split(path)[1]
    print filename
    media_directory = os.path.join(project.directory, "medias")
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
        
                          
    
    