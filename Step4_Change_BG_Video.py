# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 09:55:05 2020

@author: sandy
"""

# Imports needed
from pixellib.tune_bg import alter_bg
from pylab import rcParams

#%%
def video_frame_count(filePath):
    import cv2
    cap = cv2.VideoCapture(filePath)
    property_id = int(cv2.CAP_PROP_FRAME_COUNT) 
    length = int(cv2.VideoCapture.get(cap, property_id))
    return length

#%%
rcParams['figure.figsize'] = 10,10
change_bg = alter_bg()   #store the alter_bg() function in a variable

#%%
# Change Background Image of a Video
from pixellib.tune_bg import alter_bg
vid_change_bg = alter_bg(model_type="pb")
vid_change_bg.load_pascalvoc_model("C:\\Image-Video_Changes\\Model\\xception_pascalvoc.pb")

#%%
# Imput & Output video files
vidFile = "C:\\Image-Video_Changes\\Test_Video.mp4"
bg_Img = "C:\\Image-Video_Changes\\Black.png"

#Number of frames to be processed in the video
Number_of_Frames= video_frame_count(vidFile)
print ("Frames to process: "+str(Number_of_Frames))

#%%
#Change the video background. 
# The output file will be stored at the path and with the given name in output_video_name
vid_change_bg.change_video_bg(vidFile, bg_Img, frames_per_second = 30, output_video_name="C:\\Image-Video_Changes\\output_video.mp4", detect = "person")