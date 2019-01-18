import sys
import os
import cv2

def write_frames(filename):
    vidcap = cv2.VideoCapture(filename)
    title = filename.split('.')[-2]
    success,image = vidcap.read()
    count = 0
    success = True
    directory = 'all_frames_'+title+'/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    while success:
        frame_name = directory + title + '_frame%d.jpg' % count
        cv2.imwrite(frame_name, image)     # save frame as JPEG file
        success,image = vidcap.read()
        count += 1
