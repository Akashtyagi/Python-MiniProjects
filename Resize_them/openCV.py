# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 15:14:15 2018

@author: Akash
"""

import cv2

#image = cv2.imread('galaxy.jpg',0)      # To load a grayscale image
image = cv2.imread('galaxy.jpg',1)      # To load a image in RBG color

print(image.shape)

resize_image = cv2.resize(image,(int(image.shape[0]/2),int(image.shape[1]/2)))

cv2.imwrite("New Resized image.jpg",resize_image)
cv2.imshow("Galaxy",resize_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
