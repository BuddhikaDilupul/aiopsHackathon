import asyncio
import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO
from tracker import*
import cvzone
import time
from call import MakeCall

model = YOLO('yolov8s.pt')

def VIRTUSA(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        colorsBGR = [x, y]
        print(colorsBGR)

cv2.namedWindow('VIRTUSA')
cv2.setMouseCallback('VIRTUSA', VIRTUSA)

cap = cv2.VideoCapture('count.mp4')

my_file = open("coco.txt", "r")
data = my_file.read()
class_list = data.split("\n")

count = 0
tracker = Tracker()

# Define the polygon areas
polygon_points_X = [(10, 225), (123, 5), (561, 17), (598, 225)]
polygon_points_Y = [ (12, 484), (12, 230), (597, 233), (623, 495)]

def point_in_polygon(point, polygon):
    x, y = point
    inside = False
    for i in range(len(polygon)):
        j = (i + 1) % len(polygon)
        xi, yi = polygon[i]
        xj, yj = polygon[j]
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
            inside = not inside
    return inside

last_time = time.time()
display_interval = 5  # seconds

while True:
    ret, frame = cap.read()
    if not ret:
        break
    count += 1
    if count % 3 != 0:
        continue
    frame = cv2.resize(frame, (1020, 500))

    results = model.predict(frame)
    a = results[0].boxes.data
    px = pd.DataFrame(a).astype("float")
    people_count_x = 0
    people_count_y = 0

    for index, row in px.iterrows():
        x1 = int(row[0])
        y1 = int(row[1])
        x2 = int(row[2])
        y2 = int(row[3])
        d = int(row[5])
        c = class_list[d]
        if 'person' in c:
            person_center = ((x1 + x2) // 2, (y1 + y2) // 2)
            if point_in_polygon(person_center, polygon_points_X):
                people_count_x += 1
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 1)
                cv2.putText(frame, str(c), (x1, y1), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
            if point_in_polygon(person_center, polygon_points_Y):
                people_count_y += 1
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
                cv2.putText(frame, str(c), (x1, y1), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)

    for i in range(len(polygon_points_X)):
        j = (i + 1) % len(polygon_points_X)
        cv2.line(frame, polygon_points_X[i], polygon_points_X[j], (255, 255, 255), 2)

    for i in range(len(polygon_points_Y)):
        j = (i + 1) % len(polygon_points_Y)
        cv2.line(frame, polygon_points_Y[i], polygon_points_Y[j], (255, 255, 0), 2)
    cv2.putText(frame, f"People Count Area X: {people_count_x}", (604, 155), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
    cv2.putText(frame, f"People Count Area Y: {people_count_y}", (604, 343), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
    current_time = time.time()
    if current_time - last_time >= display_interval:
        area_count = [{"area":"X","count": people_count_x},{"area":"Y","count": people_count_y}]
        print(area_count,">>>>>>>>>>>>>>>>>>>>>>>>>>>")
        asyncio.run(MakeCall(area_count))
        last_time = current_time

    cv2.imshow("VIRTUSA", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
