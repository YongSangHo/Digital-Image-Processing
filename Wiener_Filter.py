import cv2
import numpy as np
import matplotlib.pyplot as plt

#src_file  = "cameraman_gaussian_noise.png"
src_file  = "cameraman_motion_blurred.png"
#src_file  = "cameraman_sp_noise.png"
#src_file = "cameraman_original.tif"
src_file2 = "cameraman_motion_blurred.png"

src = cv2.imread(src_file,cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread(src_file2,cv2.IMREAD_GRAYSCALE)

size = 13
kernel_motion_blur = np.zeros((size,size),dtype=src.dtype)
kernel_motion_blur[int((size-1)/2),:] = np.ones(size)
#kernel_motion_blur[:,int((size-1)/2)] = np.ones(size)
kernel_motion_blur = kernel_motion_blur / size

size = 7
kernel_motion_blur_vertical = np.zeros((size,size),dtype=src.dtype)
kernel_motion_blur_vertical[:,int((size-1)/2)] = np.ones(size)
#kernel_motion_blur_vert[:,int((size-1)/2)] = np.ones(size)
kernel_motion_blur_vertical = kernel_motion_blur_vertical / size

# Apply Fourier Transform
src_ft = np.fft.fft2(src)
src_fshift = np.fft.fftshift(src_ft)
#fshift= np.log(fshift)
src_spectrum = (np.abs(src_fshift))


kernel_motion_blur /=np.sum(kernel_motion_blur)
kernel_motion_blur = np.fft.fft2(kernel_motion_blur,s = src.shape)
kernel_motion_blur = np.conj(kernel_motion_blur)/(np.abs(kernel_motion_blur)**2+0.1)
#f = src_ft*kernel_motion_blur
#f = np.abs(np.fft.ifft2(f))




kernel_motion_blur_vertical /=np.sum(kernel_motion_blur_vertical)
kernel_motion_blur_vertical = np.fft.fft2(kernel_motion_blur_vertical,s = src.shape)
kernel_motion_blur_vertical = np.conj(kernel_motion_blur_vertical)/(np.abs(kernel_motion_blur_vertical)**2+0.1)
kernel_motion_blur_vertical *= kernel_motion_blur
f = 0.5*src_ft*kernel_motion_blur_vertical
f = np.abs(np.fft.ifft2(f))

plt.imshow(f+50,cmap = 'gray', vmin = 0, vmax = 255)
plt.show()