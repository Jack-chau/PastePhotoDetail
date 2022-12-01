import os
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime, date
# from path import Path 

img_path = "./Photo/Location1/photo3.jpg"

image = Image.open ( img_path )
exif = {}

for tag, value in image.getexif().items():
    if tag in TAGS:
        exif[ TAGS[tag] ] = value

taken_time =  exif.get ( "DateTime" )
img_datetime = datetime.strptime ( taken_time, '%Y:%m:%d %H:%M:%S')
x = datetime.now()
y = [x,img_datetime]
y = sorted( y )
print(y)


img_taken_time = datetime.strftime ( img_datetime, '%d-%m-%Y' )

# print ( img_taken_time )
