import cv2
print("package Imported")

#code for reading image
"""
img = cv2.imread("Resources/lena.png")
cv2.imshow("Output", img)
cv2.waitKey(0)
"""

#code for reading a video
"""
cap = cv2.VideoCapture("Resources/test_video.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
"""

#code for capturing the webcam


cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
    success, img = cap.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): #enter q to exit
        break
