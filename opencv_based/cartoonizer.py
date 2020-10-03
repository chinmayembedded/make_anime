import cv2
import numpy as np
import time
from scipy import ndimage
from scipy.ndimage.filters import convolve


class Cartoonizer: 

    def __init__(self): 
        pass


    def gaussian_kernel(self, size, sigma=1):
        size = int(size) // 2
        x, y = np.mgrid[-size:size+1, -size:size+1]
        normal = 1 / (2.0 * np.pi * sigma**2)
        g =  np.exp(-((x**2 + y**2) / (2.0*sigma**2))) * normal
        return g


    def bilateral_filter(self, image):
        num_filters = 10
        for _ in range(num_filters):
            img_color = cv2.bilateralFilter(image, 15, 30, 20) 
        return img_color
    

    def edge_detection(self, image):
        img_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        # img_edge = cv2.Canny(img_gray,100,220)
        # img_smoothed = convolve(img_gray, self.gaussian_kernel(9, 1.4))
        img_smoothed = cv2.medianBlur(img_gray, 5)
        img_edge = cv2.adaptiveThreshold(img_smoothed, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
            cv2.THRESH_BINARY, 9, 11)
        # img_edge = cv2.Canny(img_smoothed,100,200)
        return img_edge


    def render(self, img_rgb):   
        img_color = self.bilateral_filter(img_rgb) 
        img_edge = self.edge_detection(img_rgb)
        # img_color[img_edge == 255] = [53, 53, 53]
        # img_color = cv2.bitwise_and(img_color, img_color, mask=img_edge) 
        # img_color = cv2.bitwise_and(img_color, 255-img_edge)

        img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
        img_cartoon = cv2.bitwise_and(img_color, img_edge)
        return img_cartoon

# image = cv2.imread('4.jpg')

# obj = Cartoonizer()
# image2 = obj.render(image)
# # cv2.imwrite('op.jpg', image)
# cv2.imshow("Orig image", image)
# cv2.imshow("Cartoon", image2)

# cv2.waitKey(0)
# cv2.destroyAllWindows() 