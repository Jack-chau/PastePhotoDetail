import cv2
from path import Sorting
path = "./Photo/"
dict = Sorting(path).sortByTime()

for folder, img_time in dict.items ( ) :
    break