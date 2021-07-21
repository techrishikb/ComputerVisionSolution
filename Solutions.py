#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
from skimage import io 
from skimage.transform import rotate, AffineTransform, warp
import matplotlib.pyplot as plt
import random
from skimage import img_as_ubyte
import os
from skimage.util import random_noise


# In[2]:


img = cv2.imread(r'C:\Users\Rishi\Desktop\carimage.jpg')


# In[3]:


plt.imshow(img)
plt.show()


# In[4]:


height, width, dims= img.shape
print(height, width, dims) #print dimensions of original image


# In[10]:


#Transform the image in the +x direction by 25%, and create an image
#Transform the image in the +y direction by 25%, and create an image
quarter_height, quarter_width = height / 4, width / 4
print(quarter_height)
print(quarter_width)


# In[19]:


#quater width being positive would move the image in positive x direction by 25%
#quarter height being negative would move the image in positive y direction by 25%
T = np.float32([[1, 0, quarter_width], [0, 1, -quarter_height]])


# In[20]:


img_translation = cv2.warpAffine(img, T, (width, height))
  
#plt.imshow("Originalimage", img)
plt.imshow(img_translation)
plt.title("shifted Images")
plt.show()


# In[23]:


r_image = rotate(img, angle=90) # angle value is positive for anticlockwise rotation 
r_image1 = rotate(img, angle=-90) #angle value is negative for clockwise rotation


# In[25]:


plt.subplot(131)
plt.imshow(img)
plt.title("Original Image")
plt.subplot(132)
plt.imshow(r_image)
plt.title("90 degree rotated")
plt.subplot(133)
plt.imshow(r_image1)
plt.title("-90 degree rotated")
plt.show()


# In[26]:


#Getting the rgb value of the image
b,g,r = (img[300, 300])
print (r)
print (g)
print (b)


# In[ ]:




