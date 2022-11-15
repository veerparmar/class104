import cv2

img = cv2.imread("butterfly.jpg")
cv2.imshow("display image",img)
grey = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("display image in grey", grey)
cv2.waitKey(3000)
