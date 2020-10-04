import argparse
import cv2 
import numpy as np 
from cartoonizer import Cartoonizer
import os

tmp_canvas = Cartoonizer() 


def convert_video(cap, result):
    if (cap.isOpened()== False): 
        print("Error opening video file") 

    while(cap.isOpened()): 	 
        ret, frame = cap.read() 
        if ret == True: 
            cartoonze_image = tmp_canvas.render(frame)
            cartoonze_image = cv2.resize(cartoonze_image, size)
            # cv2.imshow('Frame', cartoonze_image)
            result.write(cartoonze_image.astype('uint8')) 

            if cv2.waitKey(25) & 0xFF == ord('q'): 
                break
        else: 
    	    break

    cap.release() 
    cv2.destroyAllWindows() 



if __name__ == "__main__":
    # ap = argparse.ArgumentParser()
    # ap.add_argument("-file_name", "--file_name", required=True, help="input video file name")
    # args = vars(ap.parse_args())
    # video_file_name = args['file_name']
    folder_path = './videos'
    op_folder_path = './outputs'
    video_list = os.listdir(folder_path)
    print(video_list)
    for a_video in video_list:
        video_path = os.path.join(folder_path, a_video)
        op_video_path = os.path.join(op_folder_path, a_video)
        cap = cv2.VideoCapture(video_path)   
        fps = cap.get(cv2.CAP_PROP_FPS)
        size = (int(cap.get(3)), int(cap.get(4))) 

        fourcc  = cv2.VideoWriter_fourcc(*"MJPG") 
        result = cv2.VideoWriter(op_video_path,  fourcc, fps, size)
        convert_video(cap, result)