import docx
import numpy as np
from docx.text.run import *
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_ALIGN_VERTICAL
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import  WD_ORIENT
from docx.shared import Cm, Inches, Pt
from path import Sorting

doc = docx.Document ( )

# Image format
font_style = "Times New Roman"
font_size  = Pt ( 18 )
image_width = Cm ( 10 )
image_height = Inches ( 3.8 )

# Set margin
margin = Cm ( 2 )
section = doc.sections[ 0 ]
section.top_margin = margin
section.left_margin = margin
section.bottom_margin = margin
section.right_margin = margin

# Set path
path = "./Photo/"
path_dict = Sorting ( path ) .sortByName ( )

# Set Orientation
def setOrientation ( ) :
    section.orientation = WD_ORIENT.LANDSCAPE
    new_width, new_height = section.page_height, section.page_width
    section.page_width = new_width
    section.page_height = new_height
