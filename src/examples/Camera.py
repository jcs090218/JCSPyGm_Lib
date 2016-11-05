#  ========================================================================
#  $File: Camera.py $
#  $Date: 2016-10-28 22:54:07 $
#  $Revision: $
#  $Creator: Jen-Chieh Shen $
#  $Notice: See LICENSE.txt for modification and distribution information
#                     Copyright (c) 2016 by Shen, Jen-Chieh $
#  ========================================================================

import pygame

from src.core.JCSPyGm_Camera import JCSPyGm_Camera
from src.managers.JCSPyGm_SceneManager import JCSPyGm_SceneManager
from src.util.JCSPyGm_Input import JCSPyGm_Input


class Camera(object):

    """Camera that follows the player..."""

    # --------------------------------------------
    # Public Variables
    # --------------------------------------------

    # --------------------------------------------
    # Private Variables
    # --------------------------------------------

    # --------------------------------------------
    # Protected Variables
    # --------------------------------------------

    # --------------------------------------------
    # Constructor
    # --------------------------------------------
    def __init__(self, player):
        """Constructor."""
        
        # get the player.
        self.player = player
        
        # get the camera, this cannot be null reference.
        self.camera = JCSPyGm_Camera.get_instance()
        
        # set the move friction default as 0.2
        self.__moveFriction = 0.2
        
        # set the camera min max distance here.
        self.camera.max_x_distance = 5000
        self.camera.min_x_distance = -500
        
        self.camera.max_y_distance = 5
        self.camera.min_y_distance = -90
        
        # set the camera target offset here.
        self.offsetX = 200
        self.offsetY = -100
        

    # --------------------------------------------
    # Public Methods
    # --------------------------------------------
    def update(self, deltaTime):
        """Do the camera game logic."""
        
        # check the player is good to use.
        if self.player is None:
            return
        
        self.camera.x += ((self.player.x + self.offsetX) - self.camera.x) / self.__moveFriction * deltaTime
        self.camera.y += ((self.player.y + self.offsetY) - self.camera.y) / self.__moveFriction * deltaTime
        
        #self.__process_input(deltaTime)

    # --------------------------------------------
    # Protected Methods
    # --------------------------------------------

    # --------------------------------------------
    # Private Methods
    # --------------------------------------------
    def __process_input(self, deltaTime):
        """Test input"""
        
        if JCSPyGm_Input.get_key_down(pygame.constants.K_a):
            self.camera.set_camera_position_xy(-100, 0)
        elif JCSPyGm_Input.get_key(pygame.constants.K_d):
            self.camera.velX = 10
        else:
            self.camera.velX = 0
            
        if JCSPyGm_Input.get_key(pygame.constants.K_w):
            self.camera.velY = -10
        elif JCSPyGm_Input.get_key(pygame.constants.K_s):
            self.camera.velY = 10
        else:
            self.camera.velY = 0
    
    # --------------------------------------------
    # setter / getter
    # --------------------------------------------
    def set_move_friction(self, newFriction):
        """Set the move friction."""
        self.__moveFriction = newFriction
        
    def get_jcspygm_camera(self):
        """Return jcspygm lib's camera."""
        return self.camera
