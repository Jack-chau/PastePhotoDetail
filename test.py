import os
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime, date
from path import Path 

path = "./Photo/"

img_path = Path( path ).setPath ( )


class TAG :
    def __init__(self, open_image ) :
        self.open_image = open_image
    
    def getImageDateTime ( self ) :


for folders, images in img_path.items ( ) :
    for image in images :
        open_img = Image.open ( open_img )


