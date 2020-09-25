# importing libraries 
import cv2 
import numpy as np 
from cartoonizer import Cartoonizer


tmp_canvas = Cartoonizer() 
cap = cv2.VideoCapture('video_4.mp4') 

frame_width = int(cap.get(3)) 
frame_height = int(cap.get(4))  
size = (frame_width, frame_height) 

fourcc  = cv2.VideoWriter_fourcc(*"MJPG") 
result = cv2.VideoWriter('output.avi',  fourcc, 10, size) 

# Check if camera opened successfully 
if (cap.isOpened()== False): 
    print("Error opening video file") 

# Read until video is completed 
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
