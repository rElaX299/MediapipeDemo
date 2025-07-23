import cv2
import mediapipe as mp
from common.system import get_camera_id
from common.com_func import get_fps

def get_lms(src_img):
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    result = hands.process(src_img)
    hand_lms = result.multi_hand_landmarks
    return hand_lms

def draw_landmarks(src_img, landmarks):
    img_height, img_width = src_img.shape[0], src_img.shape[1]
    mp_draw = mp.solutions.drawing_utils
    # style
    hand_lm_style = mp_draw.DrawingSpec(color=(0, 0, 255), thickness=5)
    hand_con_style = mp_draw.DrawingSpec(color=(255, 0, 0), thickness=10)

    if landmarks:
        for hand_lm in landmarks:
            mp_draw.draw_landmarks(src_img, hand_lm, mp.solutions.hands.HAND_CONNECTIONS,
                                   hand_lm_style, hand_con_style)
            for i, lm in enumerate(hand_lm.landmark):
                x_pos = int(lm.x * img_width)
                y_pos = int(lm.y * img_height)
                cv2.putText(src_img, str(i), (x_pos - 25, y_pos + 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                print(i, x_pos, y_pos)

def process_img(img, lms):
    pass

def add_fps_watermark(src_img):
    fps = get_fps()
    cv2.putText(src_img, f"FPS: {fps}", (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

def main():
    camera_id = get_camera_id()
    cap = cv2.VideoCapture(camera_id)

    while True:
        ret, img = cap.read()
        img_rgb = 0
        # todo: error process
        if ret:
            # prev process: convert image format to rgb
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        hand_lms = get_lms(img_rgb)

        # todo: process image
        process_img(img, hand_lms)
        draw_landmarks(img, hand_lms)

        # add fps watermark in left up corner
        add_fps_watermark(img)

        cv2.imshow('frame', img)

        if cv2.waitKey(1) == ord('q'):
            break


if __name__ == "__main__":
    main()
