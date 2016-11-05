#  ========================================================================
#  $File: JCSPyGm_CollisionManager.py $
#  $Date: 2016-10-27 21:59:53 $
#  $Revision: $
#  $Creator: Jen-Chieh Shen $
#  $Notice: See LICENSE.txt for modification and distribution information
#                     Copyright (c) 2016 by Shen, Jen-Chieh $
#  ========================================================================

from src.managers.JCSPyGm_SceneManager import JCSPyGm_SceneManager
from src.util.JCSPyGm_Collision import JCSPyGm_Collision
from src.util.JCSPyGm_Debug import JCSPyGm_Debug


class JCSPyGm_CollisionManager(object):

    """Manage all the collision in current scene."""

    # --------------------------------------------
    # Public Variables
    # --------------------------------------------
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
        
        self.sceneManager = JCSPyGm_SceneManager.get_instance()
        
    @staticmethod
    def get_instance():
        """Singleton Pattern."""
        
        if JCSPyGm_CollisionManager.instance is None:
            JCSPyGm_CollisionManager.instance = JCSPyGm_CollisionManager()
            
        return JCSPyGm_CollisionManager.instance

    # --------------------------------------------
    # Public Methods
    # --------------------------------------------
    def check_collide(self, collider1, collider2):
        """Check the collider. (basic)
        
        @param col: collider
        """
        
        collide = False
        
        if collider1.get_type() is "box" and collider2.get_type() is "box":
            collide = JCSPyGm_Collision.rect_to_rect(collider1, collider2)
        elif collider1.get_type() is "circle" and collider2.get_type() is "circle":
            collide = JCSPyGm_Collision.circle_to_circle(collider1, collider2)
        elif collider1.get_type() is "box" and collider2.get_type() is "circle":
            collide = JCSPyGm_Collision.rect_to_circle(collider1, collider2)
        elif collider1.get_type() is "circle" and collider2.get_type() is "box":
            collide = JCSPyGm_Collision.rect_to_circle(collider2, collider1)
        else:
            # this should not happend
            JCSPyGm_Debug.Error("Collider check error...")
            
        return collide
        
    def check_collide_interface(self, inter, col):
        """Check collide with this specific interface?
        
        @param inter: interface
        @param col: collider
        """
        
        # get the length of the collider in per interface.
        interfaceColliderlen = len(inter.get_colliders_in_interface())
        
        for index in range(interfaceColliderlen):
            
            # get the collider in this interface.
            colliderInInterface = inter.get_colliders_in_interface_by_index(index)
            
            # and then check it with basic check
            # collide function.
            if self.check_collide(colliderInInterface, col):
                # it did collide with somthing in this interface.
                return True
            
        # collide nothing.
        return False
    
    def check_collide_scene(self, scene, col):
        """Check collide with the scene?
        
        @param scene: scene object
        @param col: collider u want to check.
        """
        
        interfaceLen = scene.get_interfaces_len()
        
        for index in range(interfaceLen):
            # get the interface in the scene.
            inter = scene.get_interface_by_index(index)
            
            # check collider collide with interface.
            if self.check_collide_interface(inter, col):
                return True
            
        return False
    
    def add_collider_to_interface(self, inter, newCollider):
        """Add the collider to the specific interface.
        
        NOTE(jenchieh): we do not provide the collider to scene
        because we do not have the array to handle a whole 
        specific scene.
        """
        
        inter.add_collider_to_interface(newCollider)
        
    
    # --------------------------------------------
    # Protected Methods
    # --------------------------------------------

    # --------------------------------------------
    # Private Methods
    # --------------------------------------------

    # --------------------------------------------
    # setter / getter
    # --------------------------------------------
