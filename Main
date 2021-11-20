###IMPORTS
import sys
import functions.py
import numpy as np
from PIL import Image
import cv2 as cv
from getconfidence import *
from getconfidence import mp_drawing
from getconfidence import mp_face_detection
from getconfidence import mp_face_mesh
from functions import *
import glob
import time
###IMPORTS


###VARIABLES
width, height = 341,512
###VARIABLES


###FILES
#in my person project files, i have 60 lines of opening different files from the very extensive database i'm using.
Final_Data_database_confidence_file = open("C:\\path to confidence file\\databaseconfidence_file.txt","w")
###FILES
#PATHS AND LISTS
database_path = "C:\\path to images\\"
images_list = []


local_confidence_variable = 0.0
get_images(databasepath,tenkfacelist)


get_confidence(images_list,Final_Data_database_confidence_file)

# cv.destroyAllWindows()



