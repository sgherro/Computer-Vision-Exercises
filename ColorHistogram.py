import random
import numpy as np
from skimage import data

im = data.astronaut()
im = np.swapaxes(np.swapaxes(im, 0, 2), 1, 2)
nbin = random.randint(32,128)

c_hist = []
for i in range(3):
    histogram = np.zeros((nbin,))
    for row in range(im.shape[1]):
        for col in range(im.shape[2]):
            pixel = im[i,row,col]
            bin = pixel * nbin // 256 #Quantization rule
            histogram[bin] += 1
    c_hist= np.concatenate((c_hist,histogram),axis=None)#Concatentation process

# L1 normalization process
c_hist /= im.size #num tot pixel image
out = c_hist
