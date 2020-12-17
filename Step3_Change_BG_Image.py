# Imports needed
from pixellib.tune_bg import alter_bg
from matplotlib import pyplot as plt
from PIL import Image
from pylab import rcParams

#%%
rcParams['figure.figsize'] = 10,10
change_bg = alter_bg()   #store the alter_bg() function in a variable

#%%
# Pre-trained model you will need. "deeplabv3_xception_tf_dim_ordering_tf_kernels.h5"
#load pascalvoc model in the variable change_bg 

change_bg.load_pascalvoc_model("C:\\Image-Video_Changes\\Model\\deeplabv3_xception_tf_dim_ordering_tf_kernels.h5") 

filename = "C:\\Image-Video_Changes\\Obama.jpg"
bg_filename = "C:\\Image-Video_Changes\\Black.png"

#%%
#Change the background to a different image

change_bg.change_bg_img(f_image_path = filename,
                        b_image_path = bg_filename,
                        output_image_name = "C:\\Image-Video_Changes\\BG-Changed.jpg")
#Show the image
plt.imshow(Image.open('C:\\Image-Video_Changes\\BG-Changed.jpg'))