import os

class Path:
    def __init__ ( self, path ):
        self.path = path
    
    def setPath ( self ) :
        folders = os.listdir ( self.path )
        folders.sort ( )
        return folders

class Sorting ( Path ) :
    
    def __init__ ( self, path ):
        super().__init__( path )

    def sortByName ( self ) :
        folders = super().setPath( )
        img_path_dict = {}

        for folder in folders :
            each_folder_path = self.path + folder
            image_paths = os.listdir ( each_folder_path )
            image_paths.sort()
            image_path = [ self.path + folder + "/" + img_path for img_path in image_paths ]
            img_path_dict[folder] = image_path
        return img_path_dict
