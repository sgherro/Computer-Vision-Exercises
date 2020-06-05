import random
import numpy as np

n = random.randint(2, 6)
iC = random.randint(2, 6)
oC = random.randint(2, 6)
H = random.randint(10, 20)
W = random.randint(10, 20)
kH = random.randint(2, 6)
kW = random.randint(2, 6)

input = np.random.rand(n, iC, H, W).astype(np.float32)
kernel = np.random.rand(oC, iC, kH, kW).astype(np.float32)

iH = input.shape[2]
iW = input.shape[3]
oH = iH - (kernel.shape[2] -1)
oW = iW - (kernel.shape[3] -1)
oC = kernel.shape[0]
out = np.zeros((input.shape[0],kernel.shape[0],oH,oW))
for n in range(input.shape[0]): #for each pattern
    for row in range(oH): #for each row
        for col in range(oW):   #for each column
                    for bias in range(oC): # for each bias
                        for depth in range(input.shape[1]): # for each level
                            ker = kernel[bias,depth,:,:]
                            i = input[n,depth,row:row+kernel.shape[2],col:col+kernel.shape[3]]
                            out[n,bias,row,col] += np.sum(ker * i)
