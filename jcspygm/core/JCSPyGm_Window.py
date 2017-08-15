#  ========================================================================
#  $File: JCSPyGm_Window.py $
#  $Date: 2016-10-14 19:47:17 $
#  $Revision: $
#  $Creator: Jen-Chieh Shen $
#  $Notice: See LICENSE.txt for modification and distribution information
#                     Copyright (c) 2016 by Shen, Jen-Chieh $
#  ========================================================================



from os.path import sys

import pygame

from jcspygm.JCSPyGm import JCSPyGm
from jcspygm.util.JCSPyGm_Input import JCSPyGm_Input


class JCSPyGm_Window:

    """Take care of all the window message."""

    # --------------------------------------------
    # public variables
    # --------------------------------------------
    WINDOW_WIDTH = 1280
    WINDOW_HEIGHT = 720

    # window title
    WINDOW_TITLE = "JCSPyGm Library Default Title"

    # --------------------------------------------
    # private variables
    # --------------------------------------------

    # window size
    __windowRect = WINDOW_WIDTH, WINDOW_HEIGHT

    __screenColor = 0, 0, 0

    __screen = None

    __frameCnt = 0
    __timeElapsed = 0.0
    __fps = 0.0
    __tempTitle = ""

    # --------------------------------------------
    # protected variables
    # --------------------------------------------

    # --------------------------------------------
    # Constructor
    # --------------------------------------------
    def __init__(self):
        """Manage window info
        """

        # initialize the library it self.
        JCSPyGm.init()

        # set window size to pygame api
        self.set_window_size(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        
        # initialize the window title.
        self.set_window_title(self.WINDOW_TITLE)

    # --------------------------------------------
    # Public Methods
    # --------------------------------------------

    def begin_render(self):
        """Begin update the video buffer for this program."""
        self.__screen.fill(self.__screenColor)

    def end_render(self):
        """Flip the screen back buffer to front."""

        # NOTE(jenchieh): flip back buffer call
        # from the pygame API, fortunatily we
        # do not have do code this ourselves.
        pygame.display.flip()
        
        pygame.display.update()

    def calculate_frame_stats(self, gameTimer):
        """Code computes the average frames per second, and also the
        average time it takes to render one frame.  These stats
        are appended to the window caption bar."""
        
        self.__frameCnt += 1

        # Compute averages over one second period.
        if gameTimer.get_total_time() - self.__timeElapsed >= 1.0:
            
            self.__fps = float(self.__frameCnt)
            mspf = 1000.0 / self.__fps
            
            self.set_window_title(self.__tempTitle + '    '
                                  + 'FPS: ' + str(self.__fps) + '    ' 
                                  + 'Frame Time: ' + str(mspf) + ' (ms)')
            
            self.__frameCnt = 0
            self.__timeElapsed += 1.0
            
    def update_window_title(self):
        """Make the copy of the string."""
        self.__tempTitle = self.get_window_title()
        
    def process_window_event(self, evt):
        """Processes a window event."""
        
        # Exit when the X button is clicked.
        if evt.type == pygame.QUIT:
            sys.exit()
            
        # Add other events here.
        if evt.type == pygame.MOUSEBUTTONDOWN:
            JCSPyGm_Input.mouseDownThisFrame = True
            JCSPyGm_Input.mouseIsDown = True
            
        if evt.type == pygame.MOUSEBUTTONUP:
            JCSPyGm_Input.mouseUpThisFrame = True
            JCSPyGm_Input.mouseIsDown = False
            
        if evt.type == pygame.MOUSEMOTION:
            JCSPyGm_Input.mousePosition = pygame.mouse.get_pos()
            
        if evt.type == pygame.KEYDOWN:
            JCSPyGm_Input.keysPressedThisFrame.append(evt.key)
            JCSPyGm_Input.keysDown.append(evt.key)
            
        if evt.type == pygame.KEYUP:
            JCSPyGm_Input.keysReleasedThisFrame.append(evt.key)
            
            # remove any occurence of this key in the keysDown array.
            JCSPyGm_Input.keysDown.remove(evt.key)

    # --------------------------------------------
    # Protected Methods
    # --------------------------------------------

    # --------------------------------------------
    # Private Methods
    # --------------------------------------------
    def __update_screen_size(self):
        """Update the screen size base of the rect provided."""

        # then set to the PyGame api.
        self.__screen = pygame.display.set_mode(self.__windowRect)

    # --------------------------------------------
    # setter / getter
    # --------------------------------------------
    def set_window_title(self, titleName):
        """Set the title of the window.
        """
        self.__windowTitle = titleName

        # set the title to py game api
        pygame.display.set_caption(self.__windowTitle)
        
    def get_window_title(self):
        """Return window title"""
        return (self.__windowTitle + '.')[:-1]
    
    def get_screen(self):
        """"Return screen from pygame API."""
        return self.__screen

    def set_window_size(self, width, height):
        """Set window size."""

        # set to the value.
        JCSPyGm_Window.WINDOW_WIDTH = width
        JCSPyGm_Window.WINDOW_HEIGHT = height

        tempRect = width, height
        self.__windowRect = tempRect

        # update and message to PyGame api.
        self.__update_screen_size()

    def set_screen_color(self, color):
        """TODO(jenchieh): better if we wrap it with
        device manager.
        """
        self.__screenColor = color
    
    def get_window_rect(self):
        """Return window rect."""
        return self.__windowRect
