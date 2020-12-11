from natsort import os_sorted

import numpy as np
import PIL
import cv2 
import os

class Stacker():

    def __init__(self, img_dir,
                 sampling_rate=1,
                 start_idx=0,
                 end_idx=-1):
        self.img_dir = img_dir
        self.sampling_rate = sampling_rate
        self.start_idx = start_idx
        self.end_idx = end_idx
        self.img_paths = os.listdir(self.img_dir)
        self.img_paths = os_sorted(self.img_paths)
        if self.end_idx == -1:
            self.end_idx = len(self.img_paths)

    def stack(self):

        for idx, img_path in enumerate(self.img_paths):
            img_path = self.img_dir + img_path
            if idx < self.start_idx:
                continue
            if idx >= self.start_idx:
                if idx == self.start_idx:
                    img = cv2.imread(img_path)
                    mean_img = np.zeros_like(img, np.float32)

                if idx % self.sampling_rate == 0:
                    img = cv2.imread(img_path)
                
                mean_img += img

                if idx % 10 == 0:
                    print("Processed {} images".format(idx))
            
            if idx >= self.end_idx:
                print("Finished processing!")
                break
        
        mean_img /= idx
        return mean_img
                
