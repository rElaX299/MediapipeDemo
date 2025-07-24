import cv2
from pygrabber.dshow_graph import FilterGraph


def get_avail_cam():
    devices = FilterGraph().get_input_devices()
    cameras_list = {}
    for device_index, device_name in enumerate(devices):
        cameras_list[device_index] = device_name
    return cameras_list


class Camera:
    def __init__(self, camera_id):
        self.cam_id = camera_id
        self.available_cameras_list = get_avail_cam()
        self.cap = self._init_self_cap(self.cam_id)

    def _init_self_cap(self, cam_id):
        if cam_id not in self.available_cameras_list:
            print("Camera {} not available.".format(cam_id))
            return None
        return cv2.VideoCapture(cam_id)

    def get_available_cameras(self) -> {}:
        return self.available_cameras_list

    def get_cap(self):
        return self.cap

    def release_camera(self):
        if self.cap:
            self.cap.release()

if __name__ == "__main__":
    print("system")
