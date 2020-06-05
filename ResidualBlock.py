import torch.nn as nn
import torch.nn.functional as F

class ResidualBlock(nn.Module):
    def __init__(self,inplanes,planes,stride):
        super(ResidualBlock, self).__init__()
        self.bn1 = nn.BatchNorm1d(planes)
        self.bn2 = nn.BatchNorm1d(planes)
        self.bn3 = nn.BatchNorm1d(planes)
        self.conv1 = nn.Conv2d(inplanes,planes, kernel_size=3,stride=stride,padding=1,bias=False)
        self.conv2 = nn.Conv2d(planes,planes,kernel_size=3,stride=1,padding=1,bias=False)
        self.conv3 = nn.Conv2d(self.inplanes,self.planes,1,bias=False,stride=self.stride,padding=0)
        self.relu = nn.ReLU()
    
    def forward(self,x):
        out = self.relu(self.bn1(self.conv1(x)))
        y = self.bn2(self.conv2(out))
        if x.shape == out.shape:
            g = x
        else:
            g = self.conv3(x)
            y = self.bn3(g)
        return self.relu(y + g)
