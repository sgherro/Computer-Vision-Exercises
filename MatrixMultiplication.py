import numpy as np
import random
sha, shb, shc = random.randint(1, 4),  random.randint(1, 4), random.randint(1, 4)
a = np.random.random((sha, shb))
b = np.random.random((shb, shc))

aIndex = a.shape[1]
bIndex =b.shape[0]
out = np.ndarray(shape = (a.shape[0],b.shape[1]))
if (aIndex==bIndex):
    k=0
    m=0
    j=0
    while(1):
        if(m == a.shape[0]): break   
        while(1):
            if (k==b.shape[1]): break
            while(1):
                if (j==a.shape[1]): break
                out[m][k] += a[m][j] * b[j][k]
                j +=1
            k +=1
            j=0
        m+=1
        k=0
        j=0
else:
    print("Error")
    
print(out)
