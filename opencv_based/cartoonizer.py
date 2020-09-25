import cv2
import numpy as np
import time
from scipy import ndimage
from scipy.ndimage.filters import convolve

def sobel_filters( img):
    Kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], np.float32)
    Ky = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], np.float32)

    Ix = ndimage.filters.convolve(img, Kx)
    Iy = ndimage.filters.convolve(img, Ky)

    G = np.hypot(Ix, Iy)
    G = G / G.max() * 255
    theta = np.arctan2(Iy, Ix)
    return (G, theta)

def gaussian_kernel(size, sigma=1):
    size = int(size) // 2
    x, y = np.mgrid[-size:size+1, -size:size+1]
    normal = 1 / (2.0 * np.pi * sigma**2)
    g =  np.exp(-((x**2 + y**2) / (2.0*sigma**2))) * normal
    return g

class Cartoonizer: 

    def __init__(self): 
        pass

    def render(self, img_rgb):   
        numBilateralFilters = 10 

        img_color = img_rgb 
       
        for _ in range(numBilateralFilters): 
            img_color = cv2.bilateralFilter(img_color, 7, 9, 9) 

        # Canny edge detector
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
        # img_edge = cv2.Canny(img_gray,150,220)


        img_smoothed = convolve(img_gray, gaussian_kernel(9, 1.4))
        img_edge = cv2.Canny(img_smoothed,150,220)
         
        img_color[img_edge >=255] = [53, 53, 53]
        return img_color

