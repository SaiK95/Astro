import numpy as np
import PIL
import cv2 
import os

def extract_images_from_video(video_path, out_path):
    # Read the video from specified path 
    cam = cv2.VideoCapture(video_path) 
    
    if not os.path.exists(out_path): 
        os.makedirs(out_path)
      
    current_frame = 0
    
    while(True): 
        
        ret, frame = cam.read() 
    
        if ret: 

            name = out_path + str(current_frame) + '.jpg'
            if current_frame % 10 == 0:
                print ('Creating...' + name) 
    
            cv2.imwrite(name, frame) 
    
            current_frame += 1
        else: 
            break
    
    cam.release() 
    cv2.destroyAllWindows()

