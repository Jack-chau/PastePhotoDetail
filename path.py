import os
import numpy as np

class Path:
    def __init__ ( self, path ):
        self.path = path
    
    def setPath ( self ) :
        get_folders = os.listdir ( self.path )
        get_folders.sort ( )

        img_path_dict = {}

        for folder in get_folders :
            each_folder_path = self.path + folder
            image_path = os.listdir ( each_folder_path )
            image_path.sort()
            image_path = [ self.path + path for path in image_path ]
            img_path_dict[folder] = image_path
        return img_path_dict

path = "./Photo/"
    
dict = Path (path)

print ( dict.setPath() )