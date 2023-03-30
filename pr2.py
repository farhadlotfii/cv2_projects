import numpy as np
import cv2

img = cv2.imread("Rex.jpg")
img = cv2.resize(img,(640, 480))
#img[:, :, 2] = 255

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Image",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
