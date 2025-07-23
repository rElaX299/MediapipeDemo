import cv2
import mediapipe as mp
from common.system import get_camera_id
from common.com_func import get_fps

camera_id = get_camera_id()
cap = cv2.VideoCapture(camera_id)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
handLandmarkStyle = mpDraw.DrawingSpec(color=(0, 0, 255), thickness=5)
handConnectionStyle = mpDraw.DrawingSpec(color=(255, 0, 0), thickness=10)

while True:
    ret, img = cap.read()
    if ret:
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hands.process(imgRGB)
        # print(result.multi_hand_landmarks)
        handLandMarks = result.multi_hand_landmarks
        imgHeight, imgWidth = img.shape[0], img.shape[1]
        if handLandMarks:
            for handLandmark in handLandMarks:
                mpDraw.draw_landmarks(img, handLandmark,mpHands.HAND_CONNECTIONS,
                                      handLandmarkStyle, handConnectionStyle)
                for i, lm in enumerate(handLandmark.landmark):
                    xPos = int(lm.x * imgWidth)
                    yPos = int(lm.y * imgHeight)
                    cv2.putText(img, str(i), (xPos-25, yPos+5),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    print(i, xPos, yPos)

        fps = get_fps()
        cv2.putText(img, f"FPS: {fps}", (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break
