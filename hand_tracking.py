"""
    This is a demo that use hand tracking module in mediapipe.
    todo: Hands model is unsupported. Try to use hand_landmarker instead.
"""

import cv2
import mediapipe as mp
from common.com_func import get_fps
import common.system as system


def get_lms(src_img):
    """
    Get landmarks information from source image
    :param src_img: original image
    :return: landmarks information
    """
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    result = hands.process(src_img)
    hand_lms = result.multi_hand_landmarks
    return hand_lms


def draw_landmarks(src_img, hand_lms):
    """
    Draw landmarks on image
    :param src_img: where the landmarks draw
    :param hand_lms: landmarks information
    :return: None
    """
    img_height, img_width = src_img.shape[0], src_img.shape[1]
    mp_draw = mp.solutions.drawing_utils
    # style
    hand_lm_style = mp_draw.DrawingSpec(color=(0, 0, 255), thickness=5)
    hand_con_style = mp_draw.DrawingSpec(color=(255, 0, 0), thickness=10)

    if hand_lms:
        for hand_lm in hand_lms:
            mp_draw.draw_landmarks(src_img, hand_lm, mp.solutions.hands.HAND_CONNECTIONS,
                                   hand_lm_style, hand_con_style)
            for i, lm in enumerate(hand_lm.landmark):
                x_pos = int(lm.x * img_width)
                y_pos = int(lm.y * img_height)
                cv2.putText(src_img, str(i), (x_pos - 25, y_pos + 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                print(i, x_pos, y_pos)


def add_fps_watermark(src_img):
    """
    Add FPS to image in left up corner
    :param src_img: where the watermark draw
    :return: None
    """
    fps = get_fps()
    cv2.putText(src_img, f"FPS: {fps}", (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


def process_img(img, lms):
    pass


def hand_tracking():
    camera_list = system.get_avail_cam()
    print("Available cameras list:")
    for camera_index, camera_name in camera_list.items():
        print(f"ID: {camera_index}, Name: {camera_name}")
    camera_id = int(input("Select camera ID: "))
    camera = system.Camera(camera_id)
    cap = camera.get_cap()

    while True:
        ret, img = cap.read()
        if not ret:
            print("Error: cap read error!")
            camera.release_camera()
            break

        # prev process: convert image format to rgb
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        hand_lms = get_lms(img_rgb)

        process_img(img, hand_lms)

        draw_landmarks(img, hand_lms)
        add_fps_watermark(img)

        cv2.imshow('frame', img)
        cv2.setWindowProperty('frame', cv2.WND_PROP_TOPMOST, 1)

        if cv2.waitKey(1) == ord('q'):
            break

    camera.release_camera()


if __name__ == "__main__":
    hand_tracking()
