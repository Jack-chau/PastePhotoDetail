import os
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime, date

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
        sort_by_name = {}

        for folder in folders :
            each_folder_path = self.path + folder
            images_in_folder = os.listdir ( each_folder_path )
            images_in_folder.sort()
            image_path = [ self.path + folder + "/" + img for img in images_in_folder ]
            sort_by_name[folder] = image_path
        return sort_by_name

    def sortByTime ( self ) :
        folders = super().setPath ( )
        image_path_dict = { }
        img_time_dict = { }

        for folder in folders :
            each_folder_path = self.path + folder
            images_in_folder = os.listdir ( each_folder_path )
            image_path = [ self.path + folder + "/" + img for img in images_in_folder ]
            image_path_dict[ folder ] = image_path

        for folder, image in image_path_dict.items ( ) :
            img_dict = {}
            for img in image:
                img_path = img
                read_img = Image.open ( img_path )
                exif = { }

                # Get MeataData in image return dictionary
                for tag, value in read_img.getexif ( ).items ( ):
                    if tag in TAGS:
                        exif [ TAGS[ tag ] ] = value
                
                time_taken = exif.get ( "DateTime" ) # key in exif dictionary
                img_datetime = datetime.strptime ( time_taken, '%Y:%m:%d %H:%M:%S' )
                img_dict[img] = img_datetime
            img_time_dict[folder] = img_dict
        
        sort_by_time = {}

        for folders, img_time in img_time_dict.items():
            sort_by_time[folders] = { img: time for img, time in sorted( img_time.items( ), key = lambda time : time[1] ) }
        
        return sort_by_time

