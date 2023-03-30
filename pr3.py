import cv2
import numpy as np
import time


t0 = time.time()

cap = cv2.VideoCapture(0)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS)

print(width, height, fps)

while True:
    ret, frame = cap.read()
    
    if ret:
        frame = cv2.flip(frame, 1)
        t1 = str(round((time.time() -t0),2))
        cv2.putText(frame,
                    t1, 
                    (100, 100), # location 
                    cv2.FONT_HERSHEY_SIMPLEX, # font style 
                    1, # size
                    (0,0,255), #color 
                    1)
        #frame_little = frame[200:300, 200:400]
        #frame = 255 - frame
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("WebCamTest", frame)
        q = cv2.waitKey(1)
        if q == ord('q'):
            break
        
cv2.destroyAllWindows()
cap.release()
        
