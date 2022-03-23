import os
import sys
#allows the use of a python file from another folder.
sys.path.append("C:\\Users\\9nbuchanan1\\OneDrive - Rockdale County Public Schools\\10th grade\\research\\Coding\\AlphaTesting\\functions\\")
import numpy as np
import pandas as pd
from PIL import Image
import cv2 as cv
from functions import get_images_fromfile
from getconfidence import mp_drawing
from getconfidence import mp_face_detection
from getconfidence import mp_face_mesh
from openpyxl import load_workbook
from functions import *
import glob
import time

def create_data(list,file,path):
    get_images(path, list)
    get_confidence(list, file)

'''
###FILES
#surveillance FACE FILES
surveillance_exception_face_file = open("C:\\Users\\9nbuchanan1\\Documents\\research\\Coding\\files\\surveillance_empty_face_file.txt","w")
surveillance_empty_face_file = open("C:\\Users\\9nbuchanan1\\Documents\\research\\Coding\\files\\surveillance_empty_face_file.txt","w")
surveillance_1_face_file = open("C:\\Users\\9nbuchanan1\\Documents\\research\\Coding\\files\\surveillance_1_face_file.txt","w")
surveillance_2_face_file = open("C:\\Users\\9nbuchanan1\\Documents\\research\\Coding\\files\\surveillance_2_face_file.txt","w")
surveillance_3_face_file = open("C:\\Users\\9nbuchanan1\\Documents\\research\\Coding\\files\\surveillance_3_face_file.txt","w")

#surveillance EYE FILES
surveillance_execption_eye_file = open("C:\\Users\\9nbuchanan1\\Documents\\research\\Coding\\files\\surveillance_EXCEPTION_face_file.txt","w")
surveillance_empty_eye_file = open("C:\\Users\\9nbuchanan1\\Documents\\research\\Coding\\files\\surveillance_empty_eye_file.txt","w")
surveillance_1_eye_file = open("C:\\Users\\9nbuchanan1\\Documents\\research\\Coding\\files\\surveillance_1_eye_file.txt","w")
surveillance_2_eye_file = open("C:\\Users\\9nbuchanan1\\Documents\\research\\Coding\\files\\surveillance_2_eye_file.txt","w")
surveillance_3_eye_file = open("C:\\Users\\9nbuchanan1\\Documents\\research\\Coding\\files\\surveillance_3_eye_file.txt","w")
surveillance_camera_empty_face_file = open("C:\\Users\\9nbuchanan1\\Documents\\research\\Coding\\files\\surveillance_empty_faces.txt","w")

#TENK FACE FILES
tenkfaces_exception_face_file = open("C:\\Users\\9nbuchanan1\\Documents\\research\\Coding\\files\\tenkfaces_empty_face_file.txt","w")
tenkfaces_empty_face_file = open("C:\\Users\\9nbuchanan1\\Documents\\research\\Coding\\files\\tenkfaces_empty_face_file.txt","w")
tenkfaces_1_face_file = open("C:\\Users\\9nbuchanan1\\Documents\\research\\Coding\\files\\tenkfaces_1_face_file.txt","w")
tenkfaces_2_face_file = open("C:\\Users\\9nbuchanan1\\Documents\\research\\Coding\\files\\tenkfaces_2_face_file.txt","w")
tenkfaces_3_face_file = open("C:\\Users\\9nbuchanan1\\Documents\\research\\Coding\\files\\tenkfaces_3_face_file.txt","w")

#TENK EYE FILES
tenkfaces_execption_eye_file = open("C:\\Users\\9nbuchanan1\\Documents\\research\\Coding\\files\\tenkfaces_EXCEPTION_face_file.txt","w")
tenkfaces_empty_eye_file = open("C:\\Users\\9nbuchanan1\\Documents\\research\\Coding\\files\\tenkfaces_empty_eye_file.txt","w")
tenkfaces_1_eye_file = open("C:\\Users\\9nbuchanan1\\Documents\\research\\Coding\\files\\tenkfaces_1_eye_file.txt","w")
tenkfaces_2_eye_file = open("C:\\Users\\9nbuchanan1\\Documents\\research\\Coding\\files\\tenkfaces_2_eye_file.txt","w")
tenkfaces_3_eye_file = open("C:\\Users\\9nbuchanan1\\Documents\\research\\Coding\\files\\tenkfaces_3_eye_file.txt","w")

#FINAL
FINAL_surveillance_1_eye_file = open("C:\\Users\\9nbuchanan1\\Documents\\research\\Coding\\files\\Final_Data_Files\\surveillance final\\surveillance_1_eye_file.txt","r")
FINAL_tenkfaces_1_eye_file = open("C:\\Users\\9nbuchanan1\\Documents\\research\\Coding\\files\\Final_Data_Files\\tenkfaces_1_eye_file.txt","r")
Final_Data_tenkfaces_3_eye_file = open("C:\\Users\\9nbuchanan1\\Documents\\research\\Coding\\files\\Final_Data_Files\\tenkfaces_3_eye_file.txt","r")
Final_Data_tenkfaces_3_eye_file_list = []

#FINAL CONFIDENCE FILES
Final_Data_SCface_surveillancecamerasall_confidencefile = open("C:\\Users\\9nbuchanan1\\Documents\\research\\Coding\\files\\Final_Confidence_files\\Surveillance_cam_all_confidencefile.txt","w")
Final_SCface_mugshot_rotationalall_confidencefile = open("C:\\Users\\9nbuchanan1\\Documents\\research\\Coding\\files\\Final_Confidence_files\\SCface mugshot rotational all.txt","w")
Final_SCface_mugshotcropped_all_confidencefile = open("C:\\Users\\9nbuchanan1\\Documents\\research\\Coding\\files\\Final_Confidence_files\\SCface mugshot_cropped all.txt","w")
Final_Data_tenkfaces_confidence_file = open("C:\\Users\\9nbuchanan1\\Documents\\research\\Coding\\files\\Final_Confidence_files\\tenkconfidence_file.txt","w")
Final_49_images_confidence_file = open("C:\\Users\\9nbuchanan1\\Documents\\research\\Coding\\files\\Final_Confidence_files\\fourtynineimages.txt","w")
#PATHS AND LISTS

###49 IMAGES STUFFF
fourtynine_targetfile = open("C:\\Users\\9nbuchanan1\\Documents\\research\\10k adult database\\49faces\\Publication Friendly 49-Face Database\\target-filenames.txt","r")
fourtynine_list = []
fourtyninte_imagepath = "C:\\Users\\9nbuchanan1\\Documents\\research\\10k adult database\\49faces\\Publication Friendly 49-Face Database\\49 Face Images\\"
fourtynineimage_path = "C:\\Users\\9nbuchanan1\\Documents\\research\\10k adult database\\49faces\\Publication Friendly 49-Face Database\\49 Face Images\\"

'''

mugshot_frontal_cropped_all = "C:\\Users\\9nbuchanan1\\Documents\\research\\SCface_database\\SCface_database\\mugshot_frontal_cropped_all\\"
mugshot_rotation_all= "C:\\Users\\9nbuchanan1\\Documents\\research\\SCface_database\\SCface_database\\mugshot_rotation_all\\"
testing_images_path = "C:\\Users\\9nbuchanan1\\Documents\\research\\Images\\"
surveillance_cameras_all = "C:\\Users\\9nbuchanan1\\Documents\\research\\SCface_database\\SCface_database\\surveillance_cameras_all\\"
tenkfacespath = "C:\\Users\\9nbuchanan1\\Documents\\research\\10k adult database\\10kfaces\\10k US Adult Faces Database\\Face Images\\"
facelist = []
tenkfaces_editedtotwok_list = []
twoktarget_pathfiles = open("C:\\Users\\9nbuchanan1\\Documents\\research\\10k adult database\\2kattributes\\Full Attribute Scores\\target-filenames.txt","r")
newtwokfaces = open("newtwokfaces","w")

race_file = open("race_file.txt","rb") #do not un-comment
race_filex = open("str_race_file.txt","w")
gender_filex = open("str_gender_file.txt","w")
gender_file = open("gender_file.txt","rb")# do not un-comment

###races

race_path = "C:\\Users\\9nbuchanan1\\OneDrive - Rockdale County Public Schools\\10th grade\\research\\Coding\\AlphaTesting\\RACES\\"
white_file = open(race_path + "white.txt","w")
black_file = open(race_path + "black.txt","w")                       #!!!!!!!!!!!!!!!!!
east_asian_file = open(race_path + "east_asian.txt","w")             #DO
south_asian_file = open(race_path + "south_asian.txt","w")           #NOT
hispanic_file = open(race_path + "hispanic.txt","w")                 #UNCOMMENT
middle_eastern_file = open(race_path + "middle_eastern.txt","w")     #!!!!!!!!!!!!!!!!!
other_race_file = open(race_path + "other.txt","w")
white = []
black = []
east_asian = []
south_asian = []
hispanic = []
middle_eastern = []

###GENDERS

gender_path = "C:\\Users\\9nbuchanan1\\OneDrive - Rockdale County Public Schools\\10th grade\\research\\Coding\\AlphaTesting\\GENDERS\\"
male_file = open(gender_path + "male_file.txt","w")
female_file = open(gender_path + "female_file.txt","w")
male = []
female = []


###EXCEL SHEET

#creates data, writes
get_images(tenkfacespath,male)
get_confidence(male,male_file)

'''
race_list = []
gender_list = []
gender = pd.read_excel("Demographs.xlsx", usecols=[0,1,14],header=0, sheet_name=1) #reads excel data
race = pd.read_excel("Demographs.xlsx", usecols=[0,1,18],header=0, sheet_name=1)

for item in race["Race"]: #puttin the items in race into a list of just the race info
    race_list.append(item)


for item in gender["Gender"]:  #puttin the items in gender into a list of just the gender info
    gender_list.append(item)


for item in race_list:
    race_file.write(str(item) + ",")

for item in gender_list:
    gender_file.write(str(item) + ",")


print(gender_list)
print("race:")
print(race_list)
#print(nnder_list)



###VARAIBLES]
width, height = 341,512
good_race_list = []
local_confidence_variable = 0.0




twoktarget_files = twoktarget_pathfiles.read()
twoktarget_files = twoktarget_files.replace("\n",",")
twoktarget_files = twoktarget_files.split(",")
twoktarget_files_split = twoktarget_files[1::2]

#do the thing where basically show each image and do it slow so u can check that the output order is good.
race_list = race_file.read()
race_list = race_list.decode('utf-8')
race_list = race_list.split(",")

gender_list = gender_file.read()
gender_list = gender_list.decode('utf-8')
gender_list = gender_list.split(",")

print(len(twoktarget_files_split))
for index, file in enumerate(twoktarget_files_split): # this for loop is sectioning the attributes of race and gender
    # into different files which can be accessed at a later point
    if gender_list[index] == "0": #this means they're female
        female_file.write(tenkfacespath + file + ",")
    elif gender_list[index] == "1": #this means they're male
        male_file.write(tenkfacespath + file + ",")
    if race_list[index] == "1": #this means they're white
        white_file.write(tenkfacespath + file + ",")
    elif race_list[index] == "2": # this means they're black
        black_file.write(tenkfacespath + file + ",")
    elif race_list[index] == "3": # this means they're East Asian
        east_asian_file.write(tenkfacespath + file + ",")
    elif race_list[index] == "4": # this means they're South Asian
        south_asian_file.write(tenkfacespath + file + ",")
    elif race_list[index] == "5": # this means they're Hispanic
        hispanic_file.write(tenkfacespath + file + ",")
    elif race_list[index] == "6": # this means they're Middle Easter
        middle_eastern_file.write(tenkfacespath + file + ",")
    elif race_list[index] == "0": # Other
        other_race_file.write(tenkfacespath+ file + ",")

    print("race: {}".format(race_list[index]))
    print("gender: {}".format(gender_list[index]))
    # file = str(tenkfacespath + file)
    # cvimage = cv.imread(file)
    # cv.imshow("hey",cvimage)
    # cv.waitKey(1)






#gets images and puts the file paths inside a list
#gets images via a text file which stores the paths
#get_images_fromfile(tenkfaces_1_face_file,tenkfacelist)
#get_images_fromfile(FINAL_tenkfaces_1_eye_file,surveillance_cameras_all_list)
displayimage_generic(surveillance_cameras_all_list,"yo man",100,surveillance_empty)







#open all files from 49 faces
#use csv file to get which faces are male/female
#if file == (the male/female file)
#   male_list.append(file)
#elif... u kno
#test with cv2.imshow
#repeat for black/white/asian and other demographics
#run get_confidence on each list, writing to the correct file path for each.
# go into the dataanaylsis and analyze that data boi
'''