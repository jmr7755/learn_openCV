#Warp Perspective

import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")

width, height = 250,350 #general card ratio

#part of the main image u can to warp
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]]) #these points can be bought from paint app by moving mouse

#dimension of the destination image
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

#matrix
matrix = cv2.getPerspectiveTransform(pts1,pts2)

#output image
imgOutput = cv2.warpPerspective(img,matrix,(width, height))

cv2.imshow("Image",img)
cv2.imshow("Outut Image", imgOutput)
cv2.waitKey(0)