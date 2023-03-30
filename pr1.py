import numpy as np
import cv2

arr1 = np.ones((500,1000)) * 150
arr2 = np.ones((500,1000)) * 50
arr3 = np.ones((500,1000)) * 50

arr = np.zeros((500, 1000, 3))
arr[:, :, 0] = arr1
arr[:, :, 1] = arr2
arr[:, :, 2] = arr3

img = arr.astype(np.uint8)

#img = arr1.astype(np.uint8)
#img[250:270, :] = 255
#img[:, 500:520] = 255

cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
