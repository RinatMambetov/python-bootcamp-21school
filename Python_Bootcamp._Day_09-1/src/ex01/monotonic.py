import ctypes
import os
import sys
import ctypes.util
import time

if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):

    # This value represents a clock that is not subject to NTP adjustments or other clock adjustments, and has a
    # resolution that is not affected by CPU frequency scaling or power saving modes
    CLOCK_MONOTONIC_RAW = 4

    libc_path = ctypes.util.find_library('c')
    libc = ctypes.CDLL(libc_path, use_errno=True)


    class Timespec(ctypes.Structure):
        _fields_ = [
            ('tv_sec', ctypes.c_long),
            ('tv_nsec', ctypes.c_long),
        ]


    def monotonic():
        t = Timespec()
        if libc.clock_gettime(CLOCK_MONOTONIC_RAW, ctypes.byref(t)) != 0:
            # Used to retrieve the error code
            errno = ctypes.get_errno()
            raise OSError(errno, os.strerror(errno))
        return t.tv_sec + t.tv_nsec / 1e9

if __name__ == '__main__':
    for _ in range(10):
        print(monotonic())
        time.sleep(0.1)