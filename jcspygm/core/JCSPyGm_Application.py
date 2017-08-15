#  ========================================================================
#  $File: JCSPyGm_Application.py $
#  $Date: 2016-10-14 19:45:26 $
#  $Revision: $
#  $Creator: Jen-Chieh Shen $
#  $Notice: See LICENSE.txt for modification and distribution information
#                     Copyright (c) 2016 by Shen, Jen-Chieh $
#  ========================================================================


import sys
import time

import pygame

from jcspygm.core.JCSPyGm_Window import JCSPyGm_Window
from jcspygm.util.JCSPyGm_GameTime import JCSPyGm_GameTime
from jcspygm.util.JCSPyGm_Input import JCSPyGm_Input


class JCSPyGm_Application(object):

    """Wrap the framework into proper usage."""

    # Hold the window instance.
    __jcspygmWindow = None

    # Game Time instance.
    __jcspygmGameTime = None

    __appPause = False


    def __init__(self):
        """Constructor"""

        # create the window instance.
        self.__jcspygmWindow = JCSPyGm_Window()
        self.__jcspygmGameTime = JCSPyGm_GameTime()

        self.__showFrameRate = False
        
        # set default FPS to 60
        self.__fps = 60
        
        self.__fps_step = 1.0 / self.__fps
        
        self.__fpsTimer = 0.0
        
        self.__fpsCounter = 0
        self.__fpsCounterTimer = 0.0
        
        self.__acc_deltaTime = 0.0
        
    def run(self):
        """Program Loop."""

        # reset game time.
        self.get_game_time().reset()

        # start the main application loop
        while True:
            # start rendering the buffer.
            self.get_window().begin_render()

            # process the window event from OS buffer layer.
            for evt in pygame.event.get():
                self.get_window().process_window_event(evt)

            # do show frame rate setting.
            if self.__showFrameRate:
                self.get_window().calculate_frame_stats(self.get_game_time())

            # tick the time.
            self.get_game_time().tick()

            # check if the application is pause?
            if not self.get_app_pause():
                deltaTime = self.get_game_time().get_delta_time()
                
                self.__fpsTimer += deltaTime
                self.__fpsCounterTimer += deltaTime
                
                # Check how many frame render in a seconds.
                if self.__fpsCounterTimer >= 1.0:
                    self.__fpsCounter = 0
                    
                    # reset FPS counter timer
                    self.__fpsCounterTimer = 0.0
                
                # Limit framerate per seconds
                if self.__fpsTimer < self.__fps_step:
                    self.__acc_deltaTime += deltaTime
                    continue
                
                # make sure at least add the delta time.
                if self.__acc_deltaTime == 0.0:
                    self.__acc_deltaTime = deltaTime
                
                # run the application for library users.
                self._run_app(self.__acc_deltaTime, self.get_window().get_screen())
                
                # reset FPS timer 
                self.__fpsTimer = 0.0
                
                # release accumulate 'delta time'.
                self.__acc_deltaTime = 0.0
                
                self.__fpsCounter += 1
            else:
                # sleep the program.
                time.sleep(100)
                
            # clean input buffer
            JCSPyGm_Input.clean_input_buffer()
            
            # update video buffer
            self.get_window().end_render()
            
        # clean up pygame API buffer stuff.
        pygame.quit()


    # abstract function for user to override this function.
    def _run_app(self, deltaTime, windowInfo):
        """Run the application for the library user."""


    # --------------------------------------------
    # setter / getter
    # --------------------------------------------
    def get_app_pause(self):
        """Return game pause trigger?"""
        return self.__appPause

    def get_game_time(self):
        """Return game time instance."""
        return self.__jcspygmGameTime

    def get_window(self):
        """Return Window handle."""
        return self.__jcspygmWindow
    
    def set_show_frame_rate(self, act):
        """Show the framerate at the title bar?"""
        self.__showFrameRate = act;
        
    def get_current_FPS(self):
        """Actual FPS rate in the current game scene.
        
        NOTE(jenchieh): This is different from the OS layer
        FPS control, this FPS rate is in the game layer. Which
        only do the logic within this framerate.
        """
        return self.__fpsCounter
    
    def set_FPS(self, fps):
        """Set Target FPS"""
        self.__fps = fps
        
    def get_FPS(self):
        """Get Target FPS"""
        return self.__fps
