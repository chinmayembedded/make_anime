import cv2
import argparse
import cv2 
import numpy as np 
from cartoonizer import Cartoonizer
from edge_detection import Edge_detection
import os
import time
anime_obj = Cartoonizer() 
edge_obj = Edge_detection()

def apply_mask(img, mask):
    img = np.where(mask < 200, 0, img)
    return img

if __name__ == "__main__":
    # ap = argparse.ArgumentParser()
    # ap.add_argument("-file_name", "--file_name", required=True, help="input video file name")
    # args = vars(ap.parse_args())
    # image_file_name = args['file_name']
    folder_path = './images'
    op_folder_path = './output_images'
    image_list = os.listdir(folder_path)
    for image in image_list:
        t1 = time.time()
        print(image)
        image_path = os.path.join(folder_path, image)
        op_image_path = os.path.join(op_folder_path, image)
        
        image  = cv2.imread(image_path)
        img_smoothed = anime_obj.bilateral_filter(image)
        img_edge = edge_obj.edge_detection(image)
        anime_img = apply_mask(img_smoothed, 255-img_edge)
        t2 = time.time()
        print(image.shape, (t2-t1))
        cv2.imwrite(op_image_path, anime_img)