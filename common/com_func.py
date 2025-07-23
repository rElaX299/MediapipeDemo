import time

class Time:
    """
    Store time.
    """
    __stored_time = time.time()
    def get_stored_time(self):
        """
        Get previous stored time
        :return: previous stored time.
        """
        return self.__stored_time
    def set_stored_time(self, new_time):
        """
        Store new time.
        :param new_time: time to store.
        :return: None
        """
        self.__stored_time = new_time

local_time = Time()

def get_fps() -> int:
    """
    Get current fps.
    :return: FPS
    """
    prev_time = local_time.get_stored_time()
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    local_time.set_stored_time(curr_time)
    return int(fps)
