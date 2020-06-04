import cv2
import numpy as np
import matplotlib.pyplot as plt

src_file  = "cameraman_gaussian_noise.png"
#src_file  = "cameraman_motion_blurred.png"
#src_file  = "cameraman_sp_noise.png"
src = cv2.imread(src_file,cv2.IMREAD_GRAYSCALE)

size = 15
box = np.zeros((size,size),dtype=src.dtype)

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
        ordinal[i,j] = med
plt.imshow(ordinal,cmap = plt.cm.gray)
plt.show()
