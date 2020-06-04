import cv2
import numpy as np
import matplotlib.pyplot as plt

src_file  = "cameraman_gaussian_noise.png"
#src_file  = "cameraman_motion_blurred.png"
#src_file  = "cameraman_sp_noise.png"
src = cv2.imread(src_file,cv2.IMREAD_GRAYSCALE)

size = 3
box = np.zeros((size,size),dtype=src.dtype)
result = np.zeros((src.shape),dtype = src.dtype)
ordinal = np.zeros((src.shape),dtype = src.dtype)
for i in range(src.shape[0]):
    for j in range(src.shape[1]):
        for k in range(size):
            for l in range(size):
                x = i+k
                y = j+l
                if x>0 and x<src.shape[0]-1 and y>0 and y<src.shape[0]-1:
                    box[k,l] = src[x,y]
        med = np.median(box)
        #B
        if med-np.max(box)!=0 or med-np.min(box)!=0:
            B1 = src[i,j]-np.min(box)
            B2 = src[i,j]-np.max(box)
            if B1>0 and B2<0:
                result[i,j] = src[i,j]
            else:
                result[i,j] = med
            ordinal[i,j] = med
        else:
            size = size + 1
            box = np.zeros((size,size),dtype = src.dtype)
            if size > src.shape[0] or size > src.shape[1]:
                result[i,j] = med
            else:
                i = i-1
                j = j-1

plt.imshow(result,cmap = plt.cm.gray)
plt.show()