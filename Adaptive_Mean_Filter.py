import cv2
import numpy as np
import matplotlib.pyplot as plt

src_file  = "cameraman_gaussian_noise.png"

#src_file  = "cameraman_sp_noise.png"
src = cv2.imread(src_file,cv2.IMREAD_GRAYSCALE)




result = np.zeros(src.shape,dtype=np.float32)
size = 7
box = np.zeros((size,size),dtype=src.dtype)


for i in range(src.shape[0]):
    for j in range(src.shape[1]):
        for k in range(size):
            for l in range(size):
                x = i+k
                y = j+l
                if x>0 and x<src.shape[0]-1 and y>0 and y<src.shape[0]-1:
                    box[k,l] = src[x,y]
        
            
            
        mean = np.mean(box)
        var = np.var(box)
        result[i,j] = src[i,j]-(1000/var)*(src[i,j]-mean)
        
#result = padding-(300/dev)*(padding-mean)
result.astype('uint8')
plt.imshow(result,cmap='gray',vmin=0,vmax=255)
plt.show()