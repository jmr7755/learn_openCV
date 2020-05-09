import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")

kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img,(9,9),0)
imgCanny = cv2.Canny(img,150,200) #it is just the edges of the images
imgDilation = cv2.dilate(imgCanny,kernel,iterations=1) #it increases the thickness of edges
imgEroded = cv2.erode(imgDilation,kernel,iterations=1) #it erodes the thickness of edges

cv2.imshow("Output", img)
cv2.imshow("gray_image",imgGray)
cv2.imshow("blur_image",imgBlur)
cv2.imshow("Canny_img",imgCanny)
cv2.imshow("Dilation", imgDilation)
cv2.imshow("Eroded_Img", imgEroded)
cv2.waitKey(0)
