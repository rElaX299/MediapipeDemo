import time

class Time:
    __stored_time = 0
    def get_stored_time(self):
        return self.__stored_time
    def set_stored_time(self, new_time):
        self.__stored_time = new_time

local_time = Time()

def get_fps():
    prev_time = local_time.get_stored_time()
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    local_time.set_stored_time(curr_time)
    return int(fps)
