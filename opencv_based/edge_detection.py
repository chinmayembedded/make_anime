import numpy as np
import cv2
vertical_filter = [[-1,-2,-1], [0,0,0], [1,2,1]]
horizontal_filter = [[-1,0,1], [-2,0,2], [-1,0,1]]


class Edge_detection:

    def __init__(self): 
        pass

    def edge_detection(self, image):
        n,m,d = image.shape
        edges_img = image.copy()
        #loop over all pixels in the image
        for row in range(3, n-2):
            for col in range(3, m-2):
                
                #create little local 3x3 box
                local_pixels = image[row-1:row+2, col-1:col+2, 0]
                
                #apply the vertical filter
                vertical_transformed_pixels = vertical_filter*local_pixels
                #remap the vertical score
                vertical_score = vertical_transformed_pixels.sum()/4
                
                #apply the horizontal filter
                horizontal_transformed_pixels = horizontal_filter*local_pixels
                #remap the horizontal score
                horizontal_score = horizontal_transformed_pixels.sum()/4
                
                #combine the horizontal and vertical scores into a total edge score
                edge_score = (vertical_score**2 + horizontal_score**2)**.5
                
                #insert this edge score into the edges image
                edges_img[row, col] = [edge_score]*3

        edges_img = edges_img/edges_img.max()
        edges_img = edges_img * 255
        return edges_img.astype(np.uint8)
        # return edges_img