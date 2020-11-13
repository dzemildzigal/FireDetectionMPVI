import cv2
import glob, os
import numpy as np
import untangle


PATH = os.path.dirname(os.path.abspath(__file__))

GT_DIR = "\\ground_truth"
TEST_DIR = "\\test"
TRAIN_DIR = "\\train"

count=0
for filename in os.listdir(PATH + TRAIN_DIR):

    if(filename.endswith(".png") or filename.endswith(".jpg")):
        #slike
        #image_rgb =  cv2.imread(PATH + TEST_DIR + "\\"+filename)
        image = cv2.imread(PATH + TRAIN_DIR + "\\"+filename,0) #uzmi sliku
        gt = image*0 #napravi je čitavu crnu
        filename_xml = filename[:-4]+'.xml'
        obj = untangle.parse(PATH + TRAIN_DIR + "\\"+filename_xml)
        box = None
        try:
            box = obj.annotation.object.bndbox
            x_min = int(box.xmin.cdata)
            x_max = int(box.xmax.cdata)
            y_min = int(box.ymin.cdata)
            y_max = int(box.ymax.cdata)
            cv2.rectangle(gt,(x_min,y_min),(x_max,y_max),color = 255, thickness=-1)
        except:
            boxes = obj.annotation.object
            xmin = None
            xmax = None
            ymin = None
            ymax = None
            for i in boxes:
                xmin = int(i.bndbox.xmin.cdata)
                xmax = int(i.bndbox.xmax.cdata)
                ymin = int(i.bndbox.ymin.cdata)
                ymax = int(i.bndbox.ymax.cdata)
                cv2.rectangle(gt,(xmin,ymin),(xmax,ymax),color = 255, thickness=-1)
        cv2.imwrite(PATH + GT_DIR + TRAIN_DIR+"\\"+filename,gt)
        print(count)
        count += 1
    else:
        #xml-ovi
        continue

    