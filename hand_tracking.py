import sys
import cv2
import mediapipe as mp

cap = 0

if sys.platform.startswith("win"):
    # Windows 默认摄像头为0
    cap = cv2.VideoCapture(0)
elif sys.platform.startswith("darwin"):
    # macos 默认摄像头为1, 0为iphone摄像头
    cap = cv2.VideoCapture(1)
elif sys.platform.startswith("linux"):
    pass
else:
    pass

mpHands = mp.solutions.hands
hands = mpHands.Hands()

while True:
    ret, img = cap.read()
    if ret:
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hands.process(imgRGB)
        print(result.multi_hand_landmarks)
        cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break
