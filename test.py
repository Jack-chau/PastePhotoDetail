import os
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime, date
from path import Path 

path = "./Photo/"

img_path = Path( path ).setPath ( )

for folders, images in img_path.items ( ) :
    for image in images :
        print ( image )
    break
    


