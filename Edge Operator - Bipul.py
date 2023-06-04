

#Library

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

#open the images and converting to grayscale
def imgGray(image,path):
    img = Image.open(image).convert("L")
    #fileName =os.path.splitext(image)[0]
    #ext = os.path.splitext(image)[1]
    fileName = file(image)[0]
    ext = file(image)[1]
    img.save("{}/{}_gray{}".format(path,fileName,ext))
    image = np.array(img)
    return image

def file(image):
    fileName =os.path.splitext(image)[0]
    ext = os.path.splitext(image)[1]
    array = np.array([fileName, ext])
    return array

def createFolder():
    path = "ED-Bipul"
    # Check whether the specified path exists or not
    isExist = os.path.exists(path)
    if not isExist:

       # Create a new directory because it does not exist
       os.makedirs(path)
       print("The new directory is created!")
    return (path)
    

def EdgeDetection(img, kernel):
    
    fileName = file(img)[0]
    ext = file(img)[1]
    path = createFolder()
    #image pixel
    image = imgGray(img,path)
    
    
    k0 = kernel.shape[0]
    k1 = kernel.shape[1]
    k2 = kernel.shape[2]
    h,w = image.shape

    
    m = h-k1+1
    n = w-k2+1
    
    edges_img = np.zeros((m,n))
    superimpose = np.zeros((m,n))
    for ker in range(k0):
        for row in range (m):
            for col in range (n):
                pixel = image[row: row+3, col: col+3]
                ed = (pixel*kernel[ker]).sum()
                # if ed <75:
                #     ed =0
                edges_img[row,col]= ed
                
                
    
               
        edges_img =edges_img/10
        max1 = edges_img.max()
        edges_img =edges_img/max1*255
        edges_img[edges_img <25] = 0
        superimpose = superimpose+edges_img
        im = Image.fromarray(edges_img)
        im = im.convert("L")
        
        im.save("{}/{}_{}.{}".format(path,fileName,int(ker),ext))
        
    
    superimpose = superimpose/12
    max2 = superimpose.max()
    superimpose =superimpose/max2*255
    superimpose[superimpose <25] = 0
    im = Image.fromarray(superimpose)
    im = im.convert("L")
    im.save("{}/{}_superimpose.{}".format(path,fileName,ext))
    
    

#Parameters

image = "blur.jpg" #importing Grayscale image 
padding = "no" # Choose yes or no
Stride = "1" # how you want kernel to move in respect to image
kernel = np.array([  # kernel for convolution
    #Horizontal 
     [[-1 , 3 , -1],
      [-3 , 4 , -3],
      [-1 , 3 , -1]],
    #Vertical
     [[-1 , -3 , -1],
      [3 , 4 , 3],
      [-1 , -3 , -1]],
    #Diagonal 1
     [[-1 , -1 , 3],
      [-3 , 4 , -3],
      [3 , -1 , -1]],
     #Diagonal 2
     [[3 , -1 , -1],
      [-3 , 4 , -3],
      [-1 , -1 , 3]],
    # Corner 1
     [[4 , 3 , -2],
      [3 , 0 , -2],
      [-2 , -2 , -2]],
    # Corner 2
     [[-2 , -2 , -2],
      [3 , 0 , -2],
      [4 , 3 , -2]],
    # Corner 3
     [[-2 , -2 , -2],
      [-2 , 0 , 3],
      [-2 , 3 , 4]],
    # Corner 4
     [[-2 , 3 , 4],
      [-2 , 0 , 3],
      [-2 , -2 , -2]],
     #Angle 1
     [[-2 , 4 , -2],
      [3 , 0 , 3],
      [-2 , -2 , -2]],
     #Angle 2
     [[-2 , 3 , -2],
      [4 , 0 , -2],
      [-2 , 3 , -2]],
     #Angle 3
     [[-2 , -2 , -2],
      [3 , 0 , 3],
      [-2 , 4 , -2]],
     #Angle 4
     [[-2 , 3 , -2],
      [-2 , 0 , 4],
      [-2 , 3 , -2]]
     
     
    
    ])



EdgeDetection(image, kernel)

