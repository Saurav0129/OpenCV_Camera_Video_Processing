import cv2

source = "C:/Users/skbis/Videos/WaterFall.mp4"
cap = cv2.VideoCapture(source)
if not cap.isOpened():
    print("Error opening video file")

import matplotlib.pyplot as plt
ret, frame = cap.read()
if ret:  
    plt.imshow(frame[..., ::-1])
    plt.show()
else:
    print("Error reading first frame")

win_name = 'Camera Preview'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
while cv2.waitKey(1) != 27:
    has_frame, frame = cap.read()
    if not has_frame:
        break
    cv2.imshow(win_name, frame)

cap.release()
cv2.destroyWindow(win_name)
