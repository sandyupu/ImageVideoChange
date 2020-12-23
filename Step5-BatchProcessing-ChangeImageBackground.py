# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 11:42:02 2020

@author: sandy
"""
# Imports needed
from pixellib.tune_bg import alter_bg
from pylab import rcParams

#%%
rcParams['figure.figsize'] = 10,10
change_bg = alter_bg()   #store the alter_bg() function in a variable

#%%
#load pascalvoc model in the variable change_bg 
change_bg.load_pascalvoc_model("C://Image-Video_Changes//Model//deeplabv3_xception_tf_dim_ordering_tf_kernels.h5") 

#%%
# Batch processing of images to add a black background in them

import pathlib
from pathlib import PureWindowsPath

bgimage = "C://Image-Video_Changes//Black.png"

for input_img_path in pathlib.Path("C://Image-Video_Changes//input//").iterdir():
    output_img_path = str(input_img_path).replace("input","output")
    input_Windows_Format = PureWindowsPath(input_img_path)

    #convert backslash windows path into forward slash windows path using Pathlib. Needed for proper path recognition 
    p = pathlib.PureWindowsPath(input_img_path)
    print ("Processing: "+str(p.as_posix()))
    
    change_bg.change_bg_img(f_image_path = str(p.as_posix()), 
                               b_image_path = bgimage, 
                               output_image_name = output_img_path)