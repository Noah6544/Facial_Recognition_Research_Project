
import re
import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import statistics
from scipy.stats import binom




###VARIABLES
separator = 0
final_list = []
list = []
indexy = []
total_string = ""

###TEXT FILES:
confidence_path = "C:\\Users\\9nbuchanan1\\Documents\\research\\Coding\\files\\Final_Confidence_files\\COMPLETED\\"
new_confidence_paht = "C:\\Users\\9nbuchanan1\\OneDrive - Rockdale County Public Schools\\10th grade\\research\\Coding\\AlphaTesting\\CONFIDENCE FILES\\COMPLETED\\"
tenkfaces_confidence_file = open(confidence_path + "tenkconfidence_file.txt","r")
white_confidence_file = open(new_confidence_paht + "white_confidence_file.txt","r")
black_confidence_file = open(new_confidence_paht + "black_confidence_file.txt","r")
male_confidence_file = open(new_confidence_paht + "male_confidence_file.txt","r")
female_confidence_file = open(new_confidence_paht + "female_confidence_file.txt","r")

#data
tenkface_data = []
white_data =  []
black_data = []
male_data = []
female_data = []


def get_numerical_data(file,file_data):
    data = file.read()
    data = data.split(",")
    #splits the list so that there are only numerical datas
    file_data = data[1::2]
    #splits the list so that there are only the data paths
    path_data = data[::2]
    return file_data



tenkface_data = get_numerical_data(tenkfaces_confidence_file,tenkface_data)
black_data = get_numerical_data(black_confidence_file,black_data)
white_data = get_numerical_data(white_confidence_file,white_data)
female_data = get_numerical_data(female_confidence_file,female_data)
male_data = get_numerical_data(male_confidence_file,male_data)


def mean(list):
    sum = 0
    for number in list:
        sum += float(number)
    length = len(list)
    mean = sum/length
    return mean


def lowest_score(list):
    lowest_score = float(list[0])
    for idx, number in enumerate(list):
        indexy.append(idx)
        if float(number) < lowest_score:
            lowest_score = float(number)
        else:
            pass

    return lowest_score

def Find_path_for_number(path_data,index):
    print(path_data[index])
    return(path_data[index])


def low_high_percentage(low_or_high,percentage,data):
    if low_or_high == "low":
        length = len(data)
        split_index = round(length * percentage)
        data = data[:split_index:]
       # meandata = statistics.mean(data)
        #print("Low 1%:{} ".format(str(meandata)))
    elif low_or_high == "high":
        length = len(data)
        split_index = round(length * percentage)
        data = data[(length-split_index):(length+split_index):]


    return statistics.mode(data)


new_data = []
def turnfloat2(data):
    new_data  = data
    data = []
    for number in new_data:
        data.append(float(number))




def get_lowandhighandmedian(data):
    print("low 1%: {}".format(low_high_percentage("low",.01,data)))
    print("high 1%: {}".format(low_high_percentage("high",.01,data)))
    print("low 10%: {}".format(low_high_percentage("low",.1,data)))
    print("high 10%: {}".format(low_high_percentage("high",.1,data)))
    print("mode: {}".format(statistics.mode(data)))

def get_meanmedianmode(data):
    mean = statistics.mean(data)
    mode = statistics.mode(data)
    median_high = statistics.median_high(data)
    median_low = statistics.median_low(data)

get_lowandhighandmedian(tenkface_data)
print("WHITE:::\n")
get_lowandhighandmedian(white_data)
print("BLACK:::\n")
get_lowandhighandmedian(black_data)
print("FEMALE")
get_lowandhighandmedian(female_data)
print("MALE:\n\n")
get_lowandhighandmedian(male_data)

#print("mean: {}\nmode: {}\nMedia high: {}\nMedian low:{}".format(mean,mode,median_high,median_low))
#print(lowest_score(tenkface_data))
#variance = statistics.variance(data)

tenkface_data = sorted(tenkface_data,key = float)
black_data = sorted(black_data,key = float)
white_data = sorted(white_data, key=float)
female_data = sorted(female_data,key = float)
male_data = sorted(male_data,key = float)

tenkface_data = [float(x) for x in tenkface_data]
black_data = [float(x) for x in black_data]
white_data = [float(x) for x in white_data]
female_data = [float(x) for x in female_data]
male_data = [float(x) for x in male_data]
#male_data = male_data[:864:]

for index, number in enumerate(tenkface_data):
    indexy.append(index)

md = male_data
fd = female_data
bd = black_data
wd = white_data

fig, ax = plt.subplots()
#ax.hist(x, bins = 250, color='#A0BEC8')

ax.hist(bd,alpha=.5, bins = 10,  color="grey")
ax.hist(wd,alpha=.5, bins = 250, color='blue')

#ax.hist(z, bins = 8, color="blue")


#plt.yticks([50,100,500,1000,1500,2000,3000,4000,4500])
#plt.xticks([10,20,30,40,50,60,70,80,90,100])

plt.title("10kFace Dataset")
plt.xlabel("% Confidence Assesment")
plt.ylabel("Number of Pictures")
plt.legend(["African-America Data", "Caucasian Data"])
plt.tight_layout()

plt.show()


#code for scatter plot
"""
numerical_data = sorted(numerical_data,key = float)
x = numerical_data
y = indexy
sizes = np.random.uniform(15, 80, len(x))
colors = np.random.uniform(31, 41, len(x))
z = [10, 5, 0]
plt.scatter(x ,y, s=sizes, c=colors, vmin=0, vmax=100)

#plt.plot(x,z)
plt.title("10kFace Dataset")
plt.xlabel("% Confidence Assesment")
plt.ylabel("Index")
plt.legend(["This is y", "This is x"])
plt.show()
"""
