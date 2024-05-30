import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from vidgear.gears import CamGear

video_path = 'C:\\Users\\gaana\\Downloads\\vid1\\vid1.mp4'
cap = cv2.VideoCapture(video_path)
count = 0
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
    bbox, label, conf = cv.detect_common_objects(frame)
    frame = draw_bbox(frame, bbox, label, conf)
    c = label.count('car')
    p = label.count('person')
    cv2.putText(frame, "nv:" + str(c), (50, 60), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 225), 3)
    cv2.putText(frame, "np:" + str(p), (450, 60), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 225), 3)
    cv2.imshow("FRAME", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
