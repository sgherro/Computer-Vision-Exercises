import numpy as np
from skimage import data
import matplotlib.pyplot as plt
import cv2

im = data.gravel()
im = im[:128,:128]

#Sobel Mask
Gx = cv2.Sobel(im,cv2.CV_16S,1,0,ksize=3)
Gy = cv2.Sobel(im,cv2.CV_16S,0,1,ksize=3)
#Magnitude and Theta
M = np.hypot(Gx,Gy)
max_m = np.amax(M)
theta = np.arctan2(Gy,Gx)
print(theta)
# Normalization
M *= 255 / max_m
theta += np.pi 
theta *= 90 /np.pi
print(theta)
#create HSV image
hsv = np.ndarray((im.shape[0],im.shape[1],3),dtype=np.uint8)
hsv[:,:,0] = theta
hsv[:,:,1] = np.full((im.shape[0],im.shape[1]),255)
hsv[:,:,2] = M
out = cv2.cvtColor(hsv,cv2.COLOR_HSV2RGB)
plt.imshow(out)
