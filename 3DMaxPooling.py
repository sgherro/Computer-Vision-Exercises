import random
import torch

n = random.randint(2, 6)
iC = random.randint(2, 6)
T = random.randint(10, 20)
H = random.randint(10, 20)
W = random.randint(10, 20)
kT = random.randint(2, 5)
kH = random.randint(2, 5)
kW = random.randint(2, 5)
s = random.randint(2, 3)
input = torch.rand(n, iC, T, H, W)
oT = (T - kT)//s + 1
oH = (H - kH)//s + 1 
oW = (W - kW)//s + 1 
out = torch.zeros((n,iC,oT,oH,oW), dtype = torch.float32)
for num in range(n):
    t = 0
    for time in range(oT):
        r = 0
        for row in range(oH):
            c = 0
            for col in range(oW):
                for channel in range(iC):
                    out[num,channel,time,row,col]= torch.max(input[num,channel,t:t+kT,r:r+kH,c:c+kW])
                c += s
            r += s
        t +=s
