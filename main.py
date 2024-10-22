import cv2
import mediapipe as mp
import time
import HandTrackingModule as mpt
Ptime = 0
Ctime = 0

detector = mpt.HandDetector()
cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    img = detector.findHands(img)  # landmarks drawing false if set to draw=False
    lmList = detector.findPosition(img, draw=False) # landmark custom drawing false.
    if len(lmList) != 0:
        print(lmList[4])

    Ctime = time.time()
    fps = 1 / (Ctime - Ptime)
    Ptime = Ctime

    cv2.putText(img, str(int(fps)), (10, 50), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 0, 255), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
