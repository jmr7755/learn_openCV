import cv2
import numpy as np

img = cv2.imread("Resources/lambo.PNG")
print(img.shape)

imgResize = cv2.resize(img,(600,200)) #here 600 is width and 200 is height
print(imgResize.shape) #but when shape printed, it the reverse

#Note in open cv function width is first and height is second
#but in img height is first and width is second

imgCropped = img[0:200,200:500] #first height, second width

cv2.imshow("image",img)
cv2.imshow("resized image",imgResize)
cv2.imshow("cropped",imgCropped)
cv2.waitKey(0)