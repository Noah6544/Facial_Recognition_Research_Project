import os
import sys
#allows the use of a python file from another folder.
sys.path.append("C:\\Users\\9nbuchanan1\\OneDrive - Rockdale County Public Schools\\10th grade\\research\\Coding\\AlphaTesting\\functions\\")
import numpy as np
import pandas as pd
from PIL import Image
import cv2 as cv
from getconfidence import get_confidence
from functions import get_images_fromfile
from getconfidence import mp_drawing
from getconfidence import mp_face_detection
from getconfidence import mp_face_mesh
from openpyxl import load_workbook
from functions import *
import glob
import time



###RACES
race_path = "C:\\Users\\9nbuchanan1\\OneDrive - Rockdale County Public Schools\\10th grade\\research\\Coding\\AlphaTesting\\RACES\\"
white_file = open(race_path + "white.txt","r")
black_file = open(race_path + "black.txt","r")
east_asian_file = open(race_path + "east_asian.txt","r")
south_asian_file = open(race_path + "south_asian.txt","r")
hispanic_file = open(race_path + "hispanic.txt","r")
middle_eastern_file = open(race_path + "middle_eastern.txt","r")
other_race_file = open(race_path + "other.txt","r")
white = []
black = []
east_asian = []
south_asian = []
hispanic = []
middle_eastern = []
###GENDERS
gender_path = "C:\\Users\\9nbuchanan1\\OneDrive - Rockdale County Public Schools\\10th grade\\research\\Coding\\AlphaTesting\\GENDERS\\"
male_file = open(gender_path + "male_file.txt","r")
female_file = open(gender_path + "female_file.txt","r")
male = []
female = []

###DATA FILES
confidence_path = "C:\\Users\\9nbuchanan1\\OneDrive - Rockdale County Public Schools\\10th grade\\research\\Coding\\AlphaTesting\\CONFIDENCE FILES\\"
white_confidence_file = open(confidence_path + "white_confidence_file.txt","w")
black_confidence_file = open(confidence_path + "black_confidence_file.txt","w")
east_asian_confidence_file = open(confidence_path + "east_asian_confidence_file.txt","w")
south_asian_confidence_file = open(confidence_path + "south_asian_confidence_file.txt","w")
middle_eastern_confidence_file = open(confidence_path + "middle_eastern_confidence_file.txt","w")
other_race_confidence_file = open(confidence_path + "other_race_confidence_file.txt","w")
hispanic_confidence_file = open(confidence_path + "hispanic_confidence_file.txt","w")
male_confidence_file = open(confidence_path + "male_confidence_file.txt","w")
female_confidence_file = open(confidence_path + "female_confidence_file.txt","w")

#imporatant lists referenced below
list = []
output_list = []


#
def get_listofimages_from_file(file, confidence_file):
    file = file.read()
    list = file.split(",")
    print(list)
    get_confidence(list,confidence_file)


def create_data(list,file,path):
    get_images_fromfile(file, list)
    get_confidence(list, file)


get_listofimages_from_file(male_file, male_confidence_file)
get_listofimages_from_file(female_file, female_confidence_file)
get_listofimages_from_file(white_file, white_confidence_file)
get_listofimages_from_file(black_file, black_confidence_file)
get_listofimages_from_file(east_asian_file, east_asian_confidence_file)
get_listofimages_from_file(south_asian_file, south_asian_confidence_file)
get_listofimages_from_file(hispanic_file, hispanic_confidence_file)
get_listofimages_from_file(other_race_file, other_race_confidence_file)
get_listofimages_from_file(middle_eastern_file, middle_eastern_confidence_file)
