import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from vidgear.gears import CamGear
import time

video_path = 'C:\\Users\\gaana\\Downloads\\vid1\\freeroad.mp4'
cap = cv2.VideoCapture(video_path)
count = 0
delay = 0.05  # Adjust this value to control the delay between frames (in seconds)

while True:
    ret, frame = cap.read()  # Read frames from the video capture object
    if not ret:
        break

    count += 1
    if count % 6 != 0:
        continue

    if frame is None:
        continue




    cv2.imshow("FRAME", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

    time.sleep(1)  # Introduce a delay between frames

cap.release()
cv2.destroyAllWindows()
