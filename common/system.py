import sys
from enum import Enum

class CameraId(Enum):
    """
    Define the camera id in different OS.
    """
    WINDOWS_DEFAULT_CAMERA = 0  # Windows 默认摄像头为 0
    MAC_IPHONE_CAMERA = 0       # macos 0 为调用iphone摄像头
    MAC_DEFAULT_CAMERA = 1      # macos 默认摄像头为 1

def get_camera_id() -> int:
    """
    Get camera id in different OS.
    Windows default camera id is 0.
    Mac default camera id is 1.
    :return: camera id in current OS.
    """
    camera_id = 0
    if sys.platform.startswith("win"):
        camera_id = CameraId.WINDOWS_DEFAULT_CAMERA.value
    elif sys.platform.startswith("darwin"):
        camera_id = CameraId.MAC_DEFAULT_CAMERA.value
    elif sys.platform.startswith("linux"):
        pass
    else:
        pass
    return camera_id
