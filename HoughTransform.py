from io import BytesIO
import numpy as np
import cv2
from skimage import data
import matplotlib.pyplot as pl

im = data.coins()[160:230, 70:270]
out = im

img = cv2.Canny(im,100,200)
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 0.5, 4.1,param1=150,param2=30,minRadius=15,maxRadius=35)

print (circles)
for i in circles[0,:]:
    cv2.circle(out,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(out,(i[0],i[1]),1,(0,0,255),3)
    
pl.imshow(out,cmap='gray')
