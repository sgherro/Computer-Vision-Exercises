import random
import torch
from math import floor, ceil

n = random.randint(1, 3)
C = random.randint(10, 20)
H = random.randint(5, 10)
W = random.randint(5, 10)
oH = random.randint(2, 4)
oW = random.randint(2, 4)
L = random.randint(2, 6)
input = torch.rand(n, C, H, W)
boxes = [torch.zeros(L, 4) for _ in range(n)]
for i in range(n):
  boxes[i][:, 0] = torch.rand(L) * (H-oH)       # y
  boxes[i][:, 1] = torch.rand(L) * (W-oW)       # x
  boxes[i][:, 2] = oH + torch.rand(L) * (H-oH)  # w
  boxes[i][:, 3] = oW + torch.rand(L) * (W-oW)  # h

  boxes[i][:,2:] += boxes[i][:,:2]
  boxes[i][:,2] = torch.clamp(boxes[i][:,2], max=H-1)
  boxes[i][:,3] = torch.clamp(boxes[i][:,3], max=W-1)
output_size = (oH, oW)

out = torch.zeros([n, L, C, output_size[0], output_size[1]], dtype=torch.float32)

for num in range(n):
    for b in range(L):
        y1 = round(boxes[num][b, 0].item())
        x1 = round(boxes[num][b, 1].item())
        y2 = round(boxes[num][b, 2].item())
        x2 = round(boxes[num][b, 3].item())
        for ch in range(C):
            box = input[num, ch, y1:y2, x1:x2]
            for i in range(oH):
                for j in range(oW):
                    y_r = [floor(y1 + i * (y2 - y1 + 1) / oH), ceil(y1 + (i + 1) * (y2 - y1 + 1) / oH)]
                    x_r = [floor(x1 + j * (x2 - x1 + 1) / oW), ceil(x1 + (j + 1) * (x2 - x1 + 1) / oW)]
                    out[num, b, ch, i, j] = input[num, ch, y_r[0]:y_r[1], x_r[0]:x_r[1]].max()
