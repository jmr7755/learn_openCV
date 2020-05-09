import cv2
import numpy  as np

#img  = np.zeros((512,512)) #simple gray scale black image(since using 0's with size 512,512)

img = np.zeros((512,512,3),np.uint8) #this is three channel image BGR in CV2

"""
img[:] = 200,0,0 #blue image as BGR and [:] represents whole image
img[100:200,100:400] = 200,0,0 #coloring only partial image as [height,width]
"""
#line
cv2.line(img,(0,0),(200,400),(0,255,0),2) #its green color BGR, p1(width,height), p2(width,height)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),2) #here img.shape gives shape in height and width format

#rectangle
cv2.rectangle(img,(0,0),(300,100),(0,0,255),2)
#cv2.rectangle(img,(0,0),(300,100),(0,0,255),cv2.FILLED) #for filled rectangle

#circle
cv2.circle(img,(400,50),50,(230,36,78),4)

#Text
cv2.putText(img,"cv2 is cool",(200,300),cv2.FONT_HERSHEY_PLAIN,1.5,(0,200,245),2)

cv2.imshow("Image",img)
cv2.waitKey(0)