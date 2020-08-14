# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 09:22:44 2020

@author: xiaobin
"""

import requests
from PIL import Image
import matplotlib

r = requests.get('https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png')
with open('baidu.jpg', 'wb') as f:
    f.write(r.content)

img = Image.open('baidu.jpg')
matplotlib.pyplot.imshow(img)