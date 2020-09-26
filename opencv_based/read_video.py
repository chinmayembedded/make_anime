import argparse
import cv2 
import numpy as np 
from cartoonizer import Cartoonizer


tmp_canvas = Cartoonizer() 


def convert_video(cap, result):
    if (cap.isOpened()== False): 
        print("Error opening video file") 

    while(cap.isOpened()): 	 
        ret, frame = cap.read() 
        if ret == True: 
            cartoonze_image = tmp_canvas.render(frame)
            cartoonze_image = cv2.resize(cartoonze_image, size)
            cv2.imshow('Frame', cartoonze_image)
            result.write(cartoonze_image.astype('uint8')) 

            if cv2.waitKey(25) & 0xFF == ord('q'): 
                break
        else: 
    	    break

    cap.release() 
    cv2.destroyAllWindows() 



if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-file_name", "--file_name", required=True, help="input video file name")
    args = vars(ap.parse_args())
    video_file_name = args['file_name']

    cap = cv2.VideoCapture(video_file_name)   
    size = (int(cap.get(3)), int(cap.get(4))) 

    fourcc  = cv2.VideoWriter_fourcc(*"MJPG") 
    result = cv2.VideoWriter('output.avi',  fourcc, 10, size)
    convert_video(cap, result)