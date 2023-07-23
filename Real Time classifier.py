import cv2
import numpy as np

vid = cv2.VideoCapture("day to night video 2.mp4")
threshold = 120
while(True):
    
    check, frame = vid.read()
    resizedframe = cv2.resize(frame,(500,500))
    hsv = cv2.cvtColor(resizedframe, cv2.COLOR_RGB2HSV)

    # Add up all the pixel values in the V channel from the parameters (H,S and V)
    brightness = np.sum(hsv[:,:,2])
    area = 500*500
    avg = brightness/area
    if(avg >= threshold):
        cv2.putText(resizedframe,"DAY",(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),3)
    else:
        cv2.putText(resizedframe,"NIGHT",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),3)
    cv2.imshow("VIDEO",resizedframe)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
vid.release()
cv2.destroyAllWindows()