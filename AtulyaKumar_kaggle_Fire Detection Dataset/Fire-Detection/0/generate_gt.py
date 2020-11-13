import cv2
import glob, os
import numpy as np
PATH = os.path.abspath('')

output = './ground_truth'

dimenzije = []

i=0
for filename in os.listdir(PATH+"\\0\\"):
    image = cv2.imread(PATH+"\\0\\"+filename,0)
    if(image is None):
        continue
    gt = image*0
    cv2.imwrite(PATH+"\\0\\ground_truth\\"+filename,gt)
    print(i)
    i += 1
