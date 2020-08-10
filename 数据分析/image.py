# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 17:22:49 2020

@author: xiaobin
"""

from PIL import Image
import numpy as np

image = Image.open('./timg.jfif') 
image.show()    
image_array = np.array(image)

image_array = np.sum(image_array, axis=2)
image_array[...,:] = image_array[...,:]/3.0