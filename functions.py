### IMPORTS
import sys
import numpy as np
from PIL import Image
import cv2 as cv
from getconfidence import *
from functions import *
import glob
import time
import os
### IMPORTS

###VARIABLES
width, height = 341,512
###VARIABLES

#CASCADES:
eye_cascade = cv.CascadeClassifier("C:\\path to eye cascade.xml")
face_cascade_default = cv.CascadeClassifier("C:\\path to face cascade.xml")

#took from online and manipulated a bit
#but basically finds some face parameters and draws the boxes
def find_face(image,emptylist,image_file_name):
    global find_face_data
    emptyfaces = 0
    find_face_data = face_cascade_default.detectMultiScale(image, 1.3, minNeighbors=5)
    #any face which is empty will return as a tuple, which is also empty. This returns all images which are empty.
    #find_face_empty(find_face_data,image_file_name)
    for (x,y,w,h) in find_face_data:
        image = cv.rectangle(image,(x,y), (x+w,y+h), (0, 0, 0),4)
        image = cv.putText(image,"FACE",(x,y+-5),cv.FONT_HERSHEY_PLAIN,3,(0,0,0),5)
    return find_face_data

#finds how many faces the haarcascades discovers
#this was useful to my project in the past to find some data to show where the program messed up
#but I made the switch to mediapipe and just using %confidence
def find_face_empty(face_data, image_file_name,database_face_file,database_empty_face_file,
                   database_2_face_file, database_exception_face_file):
    emptyfaces = 0
    if len(face_data) == 1:
        database_face_file.write(image_file_name + "\n")
    elif len(face_data) == 0:
        print("There are no faces in this image")
        emptyfaces += 1
        database_empty_face_file.write(image_file_name + "\n")
    elif len(face_data) == 2:
        print("2 faces")
        database_2_face_file.write(image_file_name + "\n")
    else:
        database_exception_face_file.write(image_file_name + "\n")
        print("exception" + str(len(face_data)))
        
        
#finds how many eyes the haarcascades discovers and writes to which file it is...yea.
#this was useful to my project in the past to find some data to show where the program messed up
#but I made the switch to mediapipe and just using %confidence
        
def find_eye_empty(eye_data,image_file_name):
    emptyfaces = 0
    if len(eye_data) == 1:
        print("1 eyes")
        surveillance_1_eye_file.write(image_file_name + "\n")
    elif len(eye_data) == 0:
        print("0 eyes")
        emptyfaces += 1
        surveillance_empty_eye_file.write(image_file_name + "\n")
    elif len(eye_data) == 3:
        print("3 eyes")
        surveillance_3_eye_file.write(image_file_name + "\n")
    else:
        surveillance_execption_eye_file.write(image_file_name + "\n")
        print("exception" + str(len(eye_data)))

#took from online and manipulated a bit
#but basically finds some eye parameters and draws the boxes
def find_eye(image,image_file_name):
    find_eye = eye_cascade.detectMultiScale(image, 1.3, minNeighbors=5)
    #find_eye_empty(find_eye,image_file_name)
    for (x, y, w, h) in find_eye:
        left_pupil = int(x + (h / 2))
        right_pupil = int(y + (w / 2))
        image = cv.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 1)
        image = cv.circle(image,(int(left_pupil),int(right_pupil)),3,(255,255,255),thickness=3)


#Sorts and writes all images from cam 8 directly to a list
def get_cam8(path,output_list):
    #finds all files in the database directory.
    for img in os.listdir(path):
        #camera8 is the only camera in the directory we want to display.
        if "cam8" in img:
            #Writes the entire file-path back in front of the img filename so that OpenCv can later find the jpg file and display it.
            output_list.append(path + img)
        elif "cam8" not in img:
            #If it's not from camera 8, it will be ignored.
            pass

#gets images. self explanatory
def get_images(path,output_list):
    for img in os.listdir(path):
        output_list.append(path + img)

#if importing images from a text file with the path to each image use this.
#does the same thing as get_images but for text files.
def get_images_fromfile(file,output_list):
    for image in file:
        print(image)
        image = image.strip("\n")
        output_list.append(image)
    return output_list

#same as display image without any find eye/face so idk why i made this 
def show_image(image, windowname, waitkey):
    image = cv.imread(image)
    image = cv.resize(image, (width, height))
    cv.imshow(windowname, image)
    cv.waitKey(waitkey)

#gets images from a list which has already 'os.listdir'ed them. goes through and shows each and also calculates where the faces are with find_face/find_eye
def displayimage_face_eye(list,windowname,waitkey,emptylist):
    global find_face_data
    count = 0
    for image in list:
        cvimage = cv.imread(image)
        find_eye(cvimage,image)
        cvimage = cv.resize(cvimage, (width, height))
        find_face(cvimage, emptylist, image)
        get_confidence(list,path)

        cv.imshow(windowname, cvimage)
        cv.waitKey(waitkey)
        count+=1
        

def displayimage_generic(list,windowname,waitkey,emptylist):
    for image in list:
        cvimage = cv.imread(image)
        find_eye(cvimage,image)
        find_face(cvimage,emptylist,image)
        cvimage = cv.resize(cvimage, (width, height))
        cv.imshow(windowname, cvimage)
        cv.waitKey(waitkey)

