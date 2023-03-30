import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if ret:
        bgr_frame = cv2.flip(frame, 1)
        
        red_frame = bgr_frame.copy()
        red_frame[:, :, 2] = 255
        
        inv_frame = 255 - bgr_frame
        
        gray_frame = cv2.cvtColor(bgr_frame, cv2.COLOR_BGR2GRAY)
        gray_frame = np.stack((gray_frame,)*3, axis=-1)
        
        
        
        #main_frame = cv2.vconcat([bgr_frame, gray_frame])
        
        main_frame1 = np.concatenate((bgr_frame, red_frame),1)
        main_frame2 = np.concatenate((inv_frame, gray_frame),1)
        main_frame = np.concatenate((main_frame1,main_frame2))
        
        cv2.imshow("WebCamProject", main_frame)
        
        q = cv2.waitKey(1)
        if q == ord('q'):
            break
        
cv2.destroyAllWindows()
cap.release()
        
        