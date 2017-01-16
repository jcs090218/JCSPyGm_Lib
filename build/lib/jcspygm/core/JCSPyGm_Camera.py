#  ========================================================================
#  $File: JCSPyGm_Camera.py $
#  $Date: 2016-10-27 21:45:22 $
#  $Revision: $
#  $Creator: Jen-Chieh Shen $
#  $Notice: See LICENSE.txt for modification and distribution information
#                     Copyright (c) 2016 by Shen, Jen-Chieh $
#  ========================================================================

from jcspygm.core.JCSPyGm_Window import JCSPyGm_Window
from jcspygm.util import JCSPyGm_Collision
from jcspygm.util.JCSPyGm_Math import JCSPyGm_Math
from jcspygm.util.JCSPyGm_Debug import JCSPyGm_Debug


class JCSPyGm_Camera(object):

    """TODO(jenchieh): Class Description here..."""

    # --------------------------------------------
    # Public Variables
    # --------------------------------------------
    
    # create the camera instance.
    instance = None
    
    # --------------------------------------------
    # Private Variables
    # --------------------------------------------

    # --------------------------------------------
    # Protected Variables
    # --------------------------------------------

    # --------------------------------------------
    # Constructor
    # --------------------------------------------
    def __init__(self):
        """Private Constructor."""
        
        self.active = True
        
        self.x = 0
        self.y = 0
        
        # auto set position.
        self.__realX = 0
        self.__realY = 0
        
        self.velX = 0
        self.velY = 0
        
        # use to recording the x and y position
        self.recordX = 0
        self.recordY = 0
        
        # get the scene from scene manager
        self.__currentScene = None
        
        # offset of the camera.
        self.offsetX = 0
        self.offsetY = 0
        
        self.min_x_distance = float('-inf')
        self.max_x_distance = float('inf')
        self.min_y_distance = float('-inf')
        self.max_y_distance = float('inf')
        
    @staticmethod
    def get_instance():
        """Singleton Pattern."""
        
        if JCSPyGm_Camera.instance is None:
            JCSPyGm_Camera.instance = JCSPyGm_Camera()
            
        return JCSPyGm_Camera.instance
        

    # --------------------------------------------
    # Public Methods
    # --------------------------------------------
    def update(self, deltaTime):
        """"Update camera object."""
        
        # check if component active?
        if not self.active:
            return
        
        sceneManager = JCSPyGm_SceneManager.get_instance()
        self.__currentScene = sceneManager.get_current_scene()
        
        # check if current scene good to be render.
        if self.__currentScene is None:
            JCSPyGm_Debug.Error("No current scene can be render by camera.")
            return
        
        deltaSpeedX = self.velX * deltaTime
        deltaSpeedY = self.velY * deltaTime
        
        self.__realX += deltaSpeedX
        self.__realY += deltaSpeedY
        
        self.recordX += deltaSpeedX
        self.recordY += deltaSpeedY
        
        # get the interface length from the current scene.
        interLen = self.__currentScene.get_interfaces_len()
        
        for index in range(interLen):
            
            # get the each interface
            inter = self.__currentScene.get_interface_by_index(index)
            
            # get the game object len from the interface' game 
            # object array.
            gameObjectLen = inter.get_game_objects_len()
            
            for innerIndex in range(gameObjectLen):
                
                # get the game object from the interface array.
                gameObj = inter.get_game_object_by_index(innerIndex)
                
                gameObj.camX -= self.recordX * JCSPyGm_Math.abs(inter.get_friction())
                gameObj.camY -= self.recordY * JCSPyGm_Math.abs(inter.get_friction())
                
        
        # reset force
        self.recordX = 0
        self.recordY = 0
        
        cameraOffsetX = -(JCSPyGm_Window.WINDOW_WIDTH / 2) + self.offsetX
        cameraOffsetY = -(JCSPyGm_Window.WINDOW_HEIGHT / 2) + self.offsetY
        
        self.__do_min_max_distance()
        
        self.set_camera_position_xy(
            self.x + cameraOffsetX, 
            self.y + cameraOffsetY)
        
        
    def set_camera_position_xy(self, posX, posY):
        """Set camera position directly base on 
        the global position.
        """
        
        diffX = posX - self.__realX
        diffY = posY - self.__realY
        
        # check if the position the same.
        if posX == self.__realX and posY == self.__realY:
            return
        
        # get the interface length from the current scene.
        interLen = self.__currentScene.get_interfaces_len()
        
        for index in range(interLen):
            
            # get the each interface
            inter = self.__currentScene.get_interface_by_index(index)
            
            # get the game object len from the interface' game 
            # object array.
            gameObjectLen = inter.get_game_objects_len()
            
            for innerIndex in range(gameObjectLen):
                
                # get the game object from the interface array.
                gameObj = inter.get_game_object_by_index(innerIndex)
                
                gameObj.camX -= diffX * JCSPyGm_Math.abs(inter.get_friction())
                gameObj.camY -= diffY * JCSPyGm_Math.abs(inter.get_friction())
        
        
        
        # set the macros
        self.__realX = posX
        self.__realY = posY
    
    # --------------------------------------------
    # Protected Methods
    # --------------------------------------------

    # --------------------------------------------
    # Private Methods
    # --------------------------------------------
    def __do_min_max_distance(self):
        """Limit camera in a certain range."""
        
        if self.x > self.max_x_distance:
            self.x = self.max_x_distance
        elif self.x < self.min_x_distance:
            self.x = self.min_x_distance
            
        if self.y > self.max_y_distance:
            self.y = self.max_y_distance
        elif self.y < self.min_y_distance:
            self.y = self.min_y_distance

    # --------------------------------------------
    # setter / getter
    # --------------------------------------------
    
# avoid circular import error.
from jcspygm.managers.JCSPyGm_SceneManager import JCSPyGm_SceneManager
