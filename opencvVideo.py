import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# fourcc = cv2.VideoWriter_fourcc(*'MJPG')
# out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
WindowName="Main View"
cv2.namedWindow(WindowName, cv2.WINDOW_NORMAL)
#cv2.setWindowProperty(WindowName,cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
#cv2.setWindowProperty(WindowName,cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_NORMAL)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # frame = cv2.flip(frame, 0)
        # write the flipped frame
        # out.write(frame)
        cv2.namedWindow(WindowName, cv2.WINDOW_NORMAL)
        cv2.imshow(WindowName, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
# out.release()
cv2.destroyAllWindows()