
import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import time


os.chdir("C:/Users/abdul/OneDrive/Pictures/New folder")
cap = cv2.VideoCapture(0)
_, frame = cap.read()
old_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

lk_params = dict( winSize=(15, 15),
                  maxLevel=4,
                  criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))


def mouse(event, x, y, flags, params):
    global point, select, old_point
    if event == cv2.EVENT_LBUTTONDOWN:
        select = True
        point = (x, y)
        old_point = np.array([[x, y]], dtype=np.float32)



point = []
old_point = np.array([[]])
select = False

cv2.namedWindow("frame")
cv2.setMouseCallback("frame", mouse)
while True:
    _, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if select is True:
        cv2.circle(frame, point, 5, (0, 0, 255), 2)
        new_points, status, error = cv2.calcOpticalFlowPyrLK(old_gray, gray_frame, old_point, None, **lk_params)
        old_gray = gray_frame.copy()
        old_point = new_points
        x, y = new_points.ravel()
        a, b = old_point.ravel()
        cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
