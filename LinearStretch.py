import random
import numpy as np
from skimage import data
from skimage.transform import resize

im = data.coffee()
im = resize(im, (im.shape[0] // 8, im.shape[1] // 8), mode='reflect', preserve_range=True, anti_aliasing=True).astype(np.uint8)
im = np.swapaxes(np.swapaxes(im, 0, 2), 1, 2)

a = random.uniform(0,2)
b = random.uniform(-50,50)

out = np.float32(im) * a + b
out = np.around(out)
out = np.clip(out,0,255)
out = np.uint8(out)
