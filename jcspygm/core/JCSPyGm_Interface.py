#  ========================================================================
#  $File: JCSPyGm_Interface.py $
#  $Date: 2016-10-27 21:40:04 $
#  $Revision: $
#  $Creator: Jen-Chieh Shen $
#  $Notice: See LICENSE.txt for modification and distribution information
#                     Copyright (c) 2016 by Shen, Jen-Chieh $
#  ========================================================================

from xml.dom import IndexSizeErr


class JCSPyGm_Interface(object):

    """Handle friction layer of the scene."""

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
    def __init__(self):
        """Constructor."""
        
        self.active = True
        
        self.__gameObjects = []
        
        # colliders in per interface.
        self.__collider = []
        
        # default friction value is one.
        self.__friction = 1
        
        self.__name = ""
        self.__tag = ""

    # --------------------------------------------
    # Public Methods
    # --------------------------------------------
    def update(self, deltaTime):
        """Update logic for all game object in the interface."""
        
        # check active interface?
        if not self.active:
            return
        
        # get the length of the array
        arrLen = len(self.__gameObjects)
        
        # loop through and do the game logic
        for index in range(arrLen):
            self.__gameObjects[index].update(deltaTime)
        
    def draw(self, windowInfo):
        """Update graphic for all the game object."""
        
        # check active interface?
        if not self.active:
            return
        
        # get the length of the array
        arrLen = len(self.__gameObjects)
        
        # loop through and do the render
        for index in range(arrLen):
            self.__gameObjects[index].draw(windowInfo)
        
    
    def add_game_object(self, gmObj):
        """Add the game object to render queue."""
        
        arrLen = len(self.__gameObjects)
        
        # add one to array.
        self.__gameObjects.append([])
        
        self.__gameObjects[arrLen] = gmObj
        
    def add_collider_to_interface(self, newCollider):
        """Add a collider into the interface."""
        
        arrLen = len(self.__collider)
        
        self.__collider.append([])
        
        self.__collider[arrLen] = newCollider
        
    def add_game_object_as_collider(self, gmObj):
        """Add collider to this interface and render queue."""
        
        self.add_game_object(gmObj)
        self.add_collider_to_interface(gmObj.collider)
        
    def is_name(self, cmpName):
        """Check the same name."""
        return self.__name is cmpName

    def is_tag(self, cmpTag):
        """Check the same tag."""
        return self.__tag is cmpTag
        
    # --------------------------------------------
    # Protected Methods
    # --------------------------------------------

    # --------------------------------------------
    # Private Methods
    # --------------------------------------------

    # --------------------------------------------
    # setter / getter
    # --------------------------------------------
    def get_game_object_by_index(self, index):
        """Return the index gameobject."""
        return self.__gameObjects[index]
    
    def get_game_objects_len(self):
        """Return game objects array length."""
        return len(self.__gameObjects)
    
    def get_game_objects(self):
        """Return game objects array."""
        return self.__gameObjects
    
    def set_friction(self, newFriction):
        """Set the interface friction."""
        self.__friction = newFriction
        
    def get_friction(self):
        """Return interface friction value."""
        return self.__friction
    
    def get_colliders_in_interface(self):
        """Return collider in this interface."""
        return self.__collider
    
    def get_colliders_in_interface_by_index(self, index):
        """Return collider in this interface."""
        return self.__collider[index]
    
    def set_name(self, newId):
        """Identity of the collider name,"""
        self.__name = newId
    
    def get_name(self):
        """Return the identity of the collider name."""
        return self.__name
    
    def set_tag(self, newTag):
        """Identity of the collider tag,"""
        self.__tag = newTag
    
    def get_tag(self):
        """Return the identity of the collider tag."""
        return self.__tag
