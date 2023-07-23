import cv2
import numpy as np
import os
im_list_day = []
im_list_night = []
corr_day_count = 0
corr_night_count = 0
training_dir_day = "/home/bala/Real-Time-Day-Night-Classisfier/images/day"
training_dir_night = "/home/bala/Real-Time-Day-Night-Classisfier/images/night"
threshold = 100
for images in os.listdir(training_dir_day):
    im_list_day.append(images)
for images in os.listdir(training_dir_night):
    im_list_night.append(images)
def categorize_image(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    # Add up all the pixel values in the V channel from the parameters (H,S and V)
    brightness = np.sum(hsv[:,:,2])
    area = 500*500
    avg = brightness/area
    if(avg > threshold):
        return 1
    else:
        return 0
for i in range(len(im_list_day)):
    path = "images/day/"
    path = path + im_list_day[i]
    image = cv2.imread(path)
    resized_image = cv2.resize(image,(500,500))
    category = categorize_image(resized_image)
    if(category == 1):
       corr_day_count = corr_day_count + 1
for i in range(len(im_list_night)):
    path = "images/night/"
    path = path + im_list_night[i]
    image = cv2.imread(path)
    resized_image = cv2.resize(image,(500,500))
    category = categorize_image(resized_image)
    if(category == 0):
       corr_night_count = corr_night_count + 1
total = corr_day_count+corr_night_count
accuracy = (total/240)*100
print("ACCURACY:",(round(accuracy,2)),"%")