import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from vidgear.gears import CamGear
import time

video_path = 'C:\\Users\\gaana\\Downloads\\vid1\\pothole2.mp4'
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

    frame = cv2.resize(frame, (1020, 600))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    pothole_count = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 250:  # Adjust this threshold as needed
            pothole_count += 1
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.putText(frame, "Potholes: " + str(pothole_count), (50, 60), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
    cv2.imshow("FRAME", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

    time.sleep(1)  # Introduce a delay between frames

cap.release()
cv2.destroyAllWindows()
