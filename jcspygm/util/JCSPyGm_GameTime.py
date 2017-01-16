#  ========================================================================
#  $File: JCSPyGm_GameTime.py $
#  $Date: 2016-10-14 19:54:31 $
#  $Revision: $
#  $Creator: Jen-Chieh Shen $
#  $Notice: See LICENSE.txt for modification and distribution information
#                     Copyright (c) 2016 by Shen, Jen-Chieh $
#  ========================================================================

from ctypes import *


class JCSPyGm_GameTime:

    """Class handles program time, beaware this class
    is not cross platform. It uses window specific api.
    """

    __fps = 60.0
    

    def __init__(self):
        """Constructor"""

        self.__deltaTime = -1.0
        self.__secondsPerCount = 0.0

        self.__baseTime = 0.0
        self.__pauseTime = 0.0
        self.__stopTime = 0.0
        self.__prevTime = 0.0
        self.__currTime = 0.0

        self.__fps = 60.0

        self.__stopped = False

        countsPerSec = c_int64()
        windll.Kernel32.QueryPerformanceFrequency(byref(countsPerSec))
        
        self.__secondsPerCount = 1.0 / countsPerSec.value


    def reset(self):
        """Call before message loop."""
        
        currTime = c_int64()
        windll.Kernel32.QueryPerformanceCounter(byref(currTime))
        
        self.__baseTime = currTime.value
        self.__prevTime = currTime.value
        self.__stopTime = 0.0
        self.__stopped = False

    def start(self):
        """Call when unpaused."""

        startTime = c_int64()
        windll.Kernel32.QueryPerformanceCounter(byref(startTime))

        if self.__stopped:
            self.__pauseTime += startTime - self.__stopTime

            self.__prevTime = startTime
            self.__stopTime = 0.0
            self.__stopped = False

    def stop(self):
        """Call when paused."""
        if self.__stopped:
            currTime = c_int64()
            windll.Kernel32.QueryPerformanceCounter(byref(currTime))

            self.__stopTime = currTime.value
            self.__stopped = True

    def tick(self):
        """Call every frame."""

        if self.__stopped:
            self.__deltaTime = 0.0
            return

        # SOURCE(jenchieh): http://stackoverflow.com/questions/4430227/python-on-win32-how-to-get-absolute-timing-cpu-cycle-count
        currTime = c_int64()
        windll.Kernel32.QueryPerformanceCounter(byref(currTime))

        # NOTE(jenchieh): http://stackoverflow.com/questions/2330587/how-to-convert-ctypes-c-long-to-pythons-int
        self.__currTime = currTime.value

        # Time difference between this frame and the previous.
        self.__deltaTime = (self.__currTime - self.__prevTime) * self.__secondsPerCount

        # Prepare for next frame.
        self.__prevTime = self.__currTime

        # Force nonnegative.  The DXSDK's CDXUTTimer mentions that if the
        # processor goes into a power save mode or we get shuffled to another
        # processor, then mDeltaTime can be negative.
        if self.__deltaTime < 0.0:
            self.__deltaTime = 0.0

    # --------------------------------------------
    # setter / getter
    # --------------------------------------------
    def get_delta_time(self):
        """Return current frame delta time."""
        return float(self.__deltaTime)

    def get_total_time(self):
        """Return total time."""

        if self.__stopped:
            return float((((self.__stopTime - self.__pauseTime) - self.__baseTime) * self.__secondsPerCount))

        return float((((self.__currTime - self.__pauseTime) - self.__baseTime) * self.__secondsPerCount))
