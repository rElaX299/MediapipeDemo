import sys
import cv2

def get_capture():
    cap = cv2.VideoCapture(0)
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
    return cap
