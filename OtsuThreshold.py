import random
import numpy as np
from skimage import data
from skimage.transform import resize

im = data.camera()
im = resize(im, (im.shape[0] // 2, im.shape[1] // 2), mode='reflect', preserve_range=True, anti_aliasing=True).astype(np.uint8)
maxval= 0
tr = 0
h, bins= np.histogram(im,256,[0,256])
bins = bins[:256]
for t in range(256):
    o1 = np.sum(h[:t+1])
    o2 = np.sum(h[t+1:])
    if o1 and o2:
        mu1 = (np.sum(h[:t+1] * bins[:t+1]))/o1
        mu2 = (np.sum(h[t+1:] * bins[t+1:]))/o2
    else:
        mu1 = mu2 = 0
    sigma = o1 * o2 * (mu1 - mu2)**2

    if sigma > maxval:
        maxval = sigma
        tr = t
out = tr
