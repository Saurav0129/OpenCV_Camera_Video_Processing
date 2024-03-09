import cv2
source=0
cap=cv2.VideoCapture(source)
if not cap.isOpened:
    print("Error in Video File")
win_name='Camera Preview'
cv2.namedWindow(win_name,cv2.WINDOW_NORMAL)
frame_width=int(cap.get(3))
frame_height=int(cap.get(4))
print(frame_width)
print(frame_height)
out_mp4=cv2.VideoWriter("new_vid.mp4",cv2.VideoWriter_fourcc(*'XVID'),10,(frame_width,frame_height))
while cv2.waitKey(1)!=27:
    ret,frame=cap.read()
    if ret:
        out_mp4.write(frame)
        cv2.imshow(win_name,frame)
        
    else:
        break

cap.release()
out_mp4.release()
cv2.destroyWindow(win_name)
