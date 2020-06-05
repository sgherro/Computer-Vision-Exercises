from io import BytesIO
import numpy as np
import cv2
from skimage import data
import matplotlib.pyplot as pl

bio = BytesIO(data_files["question-data/gallery_1.jpg"])
bytes = np.asarray(bytearray(bio.read()), dtype=np.uint8)
im_b = cv2.imdecode(bytes, cv2.IMREAD_COLOR)
im_b = np.swapaxes(np.swapaxes(im_b, 0, 2), 1, 2)
im_b = im_b[::-1, :, :]  # from BGR to RGB
im_b_cv = np.swapaxes(im_b,0,1)
im_b_cv = np.swapaxes(im_b_cv,1,2)
#Points are manually taken
point_a = np.float32([[192,34],[318,94],[181,237],[310,210]]).reshape(-1,1,2)
point_b = np.float32([[137,50],[339,59],[132,191],[335,199]]).reshape(-1,1,2)

H,mask = cv2.findHomography(point_b,point_a,cv2.RANSAC,5.0)
W_b = cv2.warpPerspective(im_b_cv,np.float32(H),(550,500))
W_b = np.swapaxes(W_b,1,2)
W_b = np.swapaxes(W_b,0,1)
W_b[:,0:im_a.shape[1],0:im_a.shape[2]] = im_a
out = W_b
out = np.swapaxes(out,0,1)
out = np.swapaxes(out,1,2)
pl.imshow(out)
