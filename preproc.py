# import the necessary packages
#from PIL import Image
#import pytesseract
#import argparse
import cv2
import os
import sys
import glob

# # construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
# 	help="path to input image to be OCR'd")
# ap.add_argument("-p", "--preprocess", type=str, default="thresh",
# 	help="type of preprocessing to be done")
# args = vars(ap.parse_args())

# load the example image and convert it to grayscale
def preprocess():
    frame_list = 'all_frames_4_1_1_05102017_121841_cutvid/*.jpg'
    
    #prefix = str(frames_folder)+'/*.jpg'
    #prefix = str(prefix)
    #print(prefix)
    jpg_list = glob.glob(frame_list)
    jpg_list = sorted(jpg_list)
    for i in jpg_list:
        image = i
        title = image.split('.')[-2]
        # load the example image and convert it to grayscale
        image = cv2.imread(image)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # apply thresholding to preprocess the image
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        # median blurring to remove noise
        #gray = cv2.medianBlur(gray, 3)
        new_name = title+'_preproc.jpg'
        cv2.imwrite(new_name,gray)
 
# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
#filename = "{}.png".format(os.getpid())
#cv2.imwrite(filename, gray)

# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
#text = pytesseract.image_to_string(Image.open(filename))
#os.remove(filename)
#print(text)

#title = filename.split('.')[-2]
 
#save the output images
#cv2.imwrite(title + '_output.png',gray)

# show the output images
#cv2.imshow("Image", image)
#cv2.imshow("Output", gray)
#cv2.waitKey(0)
