import cv2
from pygrabber.dshow_graph import FilterGraph


def get_available_cameras() -> {}:
    devices = FilterGraph().get_input_devices()
    available_cameras = {}
    for device_index, device_name in enumerate(devices):
        available_cameras[device_index] = device_name
    return available_cameras


def open_camera():
    camera_list = get_available_cameras()
    print("Available cameras list:")
    for camera_index, camera_name in camera_list.items():
        print(f"ID: {camera_index}, Name: {camera_name}")

    # select which camera to use
    camera_id = int(input("Select camera id: "))
    return cv2.VideoCapture(camera_id)


if __name__ == "__main__":
    print(get_available_cameras())
