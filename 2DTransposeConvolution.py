import random
import torch

n = random.randint(2, 6)
iC = random.randint(2, 6)
oC = random.randint(2, 6)
H = random.randint(10, 20)
W = random.randint(10, 20)
kH = random.randint(2, 6)
kW = random.randint(2, 6)
s = random.randint(2, 6)

input = torch.rand(n, iC, H, W)
kernel = torch.rand(iC, oC, kH, kW)
oH = (H - 1)*s + kH 
oW = (W - 1)*s + kW
out = torch.zeros((num,oC,oH,oW))
for row in range(H):
    outR = row * s
    for col in range(W):
        outC = col *s
        i = input[:,:,row,col,None,None,None]
        ker = kernel[None,:,:,:,:]
        out[:,:,outR:outR + kH, outC:outC + kW] += torch.sum(ker * i, dim=1)
