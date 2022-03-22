## Facial Recognition Research Project
## Research Question:
# What is the Effect of Facial Recognition on Racial Bias?

## Abstract

Facial recognition inherently is biased to different demographic groups, due to machine learning not having enough data from other demographics being tested in facial recognition’s initial creation. This created a cascade of biases as other models were being built on previous ones. These biases can make criminal investigation inaccurate if facial assessment is incorrect.
Using the 2 databases I was granted access to; I could run trials on over 10,000 images. For each image in each database, I used Google’s facial recognition solution, MediaPipe, to perform facial recognition and return a numerical value of how confident the program was in its facial assessment in a numerical percentage value. I repeated this when splitting the databases into different demographic groups (white/black, male/female), and used python’s file managing systems, to store the data of each image in each demographic group.
Using matplotlib, NumPy, and pandas (python packages specializing in data visualization/analysis), I was able to find the median, mean, and mode of the different demographics, and create different graphs to visualize the data. 
Over a total of 10,168 images analyzed, and different conclusions were made for all images as well for each specific demographic. I found that the accuracy was slightly skewed in favor of females, while male face detection typically performed worse. 
In conclusion, the research conducted supported the hypothesis that not only is facial recognition biased to different demographics groups, but also that technology may not be ready to be solely responsible for facial assessments, especially in criminal cases. 

