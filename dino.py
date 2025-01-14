import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import pyautogui as auto


cap = cv2.VideoCapture(0)
hd = HandDetector(maxHands=1)

while 1:
    rt, frame = cap.read()
    frame = cv2.resize(frame, (1080, 720))

    cvzone.putTextRect(frame, 'ELnubi the GOAT', [360, 40], scale=3, thickness=3, border=2, colorR=(0, 0, 0))

    hands, frame = hd.findHands(frame)

    if hands:
        hand = hands[0]
        lmlist = hand['lmList']

        length, info, frame = hd.findDistance(lmlist[4][:2], lmlist[8][:2], frame)
        length = round(length)

        if length < 25:
            auto.press('up')

    cv2.imshow('frame', frame)
    cv2.waitKey(1)