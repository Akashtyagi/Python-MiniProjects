# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 23:21:05 2018

@author: Akash
"""

import cv2
import glob

images = glob.glob("Resize them/*.jpg")

for image in images:
    img = cv2.imread(image,1)
#    cv2.imshow("x",image)
#    cv2.waitKey(0)
    Rimage = cv2.resize(img,(100,100))
    cv2.imwrite(image[:-4]+"_resized.jpg",Rimage)