import cv2
import numpy as np
import time

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
        img_edge = cv2.Canny(img_gray,150,220)

         
        img_color[img_edge == 255] = [53, 52, 52]
        return img_color

