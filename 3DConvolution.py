import random
import torch

n = random.randint(2, 6)
iC = random.randint(2, 6)
oC = random.randint(2, 6)
T = random.randint(10, 20)
H = random.randint(10, 20)
W = random.randint(10, 20)
kT = random.randint(2, 6)
kH = random.randint(2, 6)
kW = random.randint(2, 6)

input = torch.rand(n, iC, T, H, W)
kernel = torch.rand(oC, iC, kT, kH, kW)
bias = torch.rand(oC)

oT = T - (kT - 1) 
oH = H - (kH - 1)
oW = W - (kW - 1)
out = torch.zeros((num,oC,oT,oH,oW))
for n in range(num): #for each pattern
    for t in range(oT): #for each time
        for row in range(oH): #for each row
            for col in range(oW):   #for each column
                    for b in range(oC): # for each bias
                        for depth in range(iC): # for each level
                            ker = kernel[b,depth,:,:,:]
                            i = input[n,depth,t:t+kT,row:row+kH,col:col+kW]
                            out[n,b,t,row,col] += torch.sum(ker * i)
                        out[n,b,t,row,col] += bias[b]
