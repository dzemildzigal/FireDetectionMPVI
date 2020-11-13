import cv2
import glob, os
import numpy as np
import untangle
import shutil

PATH = os.path.dirname(os.path.abspath(__file__))

GT_DIR = "\\ground_truth" 
TEST_DIR = "\\test"
TRAIN_DIR = "\\train"


count=0
for filename in os.listdir(PATH):# + TRAIN_DIR):

    if(filename.endswith(".png") or filename.endswith(".jpg")):
        #slike
        image_rgb =  cv2.imread(PATH + "\\"+filename)
        image = cv2.imread(PATH + "\\"+filename,0) #uzmi sliku
        gt = image*0 #napravi je čitavu crnu
        filename_txt = filename[:-4]+'.txt'
        f = open(PATH  + "\\"+filename_txt, "r")
        f = f.readlines()
        fire = 0
        for i in f:
            data = i.split(' ')
            if int(data[0]) == 1:
                #it's a fire 
                #prebaci u already_done\\fire i ground_truth\\fire
                xmin = int(float(data[1])*gt.shape[0])
                xmax = int(float(data[2])*gt.shape[0])
                ymin = int(float(data[3])*gt.shape[1])
                ymax = int(float(data[4])*gt.shape[1])
                cv2.rectangle(gt,(xmin,ymin),(xmax,ymax),color = 255, thickness=-1)
                #cv2.imshow("GT", gt)
                #cv2.imshow("Original", image_rgb)
                #cv2.waitKey()
                fire += 1
                
        if(fire == 0):
            #not fire
            cv2.imwrite(PATH + GT_DIR +"\\non_fire\\"+filename,gt)
            shutil.move(PATH + "\\"+filename, PATH + "\\already_done\\non_fire\\"+filename)
            shutil.move(PATH + "\\"+filename_txt, PATH + "\\already_done\\non_fire\\txt_files\\"+filename_txt)
        else:
            #fire
            gt = cv2.flip(gt,0)
            cv2.imwrite(PATH + GT_DIR +"\\fire\\"+filename,gt)
            shutil.move(PATH + "\\"+filename, PATH + "\\already_done\\fire\\"+filename)
            shutil.move(PATH + "\\"+filename_txt, PATH + "\\already_done\\fire\\txt_files\\"+filename_txt)

        print(count)
        count += 1    