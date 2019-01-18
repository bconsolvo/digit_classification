#!/usr/bin/env python3

from moviepy.editor import *
import sys
import os

def crop(filename,x1,y1,x2,y2):
    clip = VideoFileClip(filename)
    title = filename.split('.')[-2]   
    clip_crop.write_videofile(title+'_cutvid.mp4',progress_bar=False)
