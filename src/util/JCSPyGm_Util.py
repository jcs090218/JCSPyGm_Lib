#  ========================================================================
#  $File: JCSPyGm_Util.py $
#  $Date: 2016-10-14 22:33:27 $
#  $Revision: $
#  $Creator: Jen-Chieh Shen $
#  $Notice: See LICENSE.txt for modification and distribution information
#                     Copyright (c) 2016 by Shen, Jen-Chieh $
#  ========================================================================


import random
import pygame

from src.core.JCSPyGm_GameObject import JCSPyGm_GameObject


class JCSPyGm_Util:

    """Utility Class for JCSPyGm."""

    @staticmethod
    def IsPossible(val):
        """Simple algorithm decide the
        possibility."""
        
        chance = random.randint(0, 100)
        
        if val > chance:
            return True
        
        return False
    
    @staticmethod
    def create_interface_sprite(inter, filePath, ext, autoPivot = False):
        """Create the Interface Sprite
        
        @param inter: interface object.
        @param filePath: path of the sprite file.
        @param ext: extension
        @param autoPivot: auto pivot the sprite.
        """
        
        # create a sprite object.
        tempSprite = JCSPyGm_GameObject()
        
        # load the sprite base on the parameters.
        tempSprite.load_sprite(filePath, ext)
        
        # add to interface.
        inter.add_game_object(tempSprite)
        
        if autoPivot:
            tempSprite.auto_pivot()
        
        # in case the user want the pointer of what
        # we just create for him, so return the object
        # we just created.
        return tempSprite
    
    @staticmethod
    def create_interface_animation(inter, filePath, baseName, ext, frameCount, autoPivot = False):
        """Create the interface animation
        
        @param inter: interface object.
        @param filePath: path of the sprite file.
        @param baseName: base name of the animation
        @param ext: extension
        @param frameCount: frame count
        @param autoPivot: auto pivot the animation.
        """
        
        # create a animation object.
        tempAnim = JCSPyGm_GameObject()
        
        # load the animation base on the parameters.
        tempAnim.load_animation(filePath, baseName, ext, frameCount)
        
        # add to interface.
        inter.add_game_object(tempAnim)
        
        if autoPivot:
            tempAnim.auto_pivot()
        
        # in case the user want the pointer of what
        # we just create for him, so return the object
        # we just created.
        return tempAnim
    
    @staticmethod
    def create_interface_collider_sprite(
            inter, 
            colliderType,
            filePath, 
            ext, 
            autoPivot = False):
        """Create the interface collider object and 
        is sprite.
        
        @param inter: interface object.
        @param colliderType: collider type (string)
        @param filePath: path of the sprite file.
        @param ext: extension
        @param autoPivot: auto pivot the sprite and collider.
        """
        
        # create the sprite object and add it to interface.
        newSpriteColliderObj = JCSPyGm_Util.create_interface_sprite(inter, filePath, ext, autoPivot)
        
        # auto collider the type
        newSpriteColliderObj.auto_collider(colliderType)
        
        # add collider to interface
        inter.add_collider_to_interface(newSpriteColliderObj.collider)
        
        if autoPivot:
            newSpriteColliderObj.auto_pivot()
        
        return newSpriteColliderObj
    
    @staticmethod
    def create_interface_collider_animation(
            inter, 
            colliderType, 
            filePath, 
            baseName, 
            ext, 
            frameCount, 
            autoPivot = False):
        """Create the interface collider object and 
        is animated.
        
        @param inter: interface object.
        @param colliderType: collider type (string)
        @param filePath: path of the sprite file.
        @param baseName: base name of the animation
        @param ext: extension
        @param frameCount: frame count
        @param autoPivot: auto pivot the animation and collider.
        """
        
        # TODO(jenchieh): finish this...
        newAnimColliderObj = JCSPyGm_Util.create_interface_animation(inter, filePath, baseName, ext, frameCount, autoPivot)
        
        # auto collider the type
        newAnimColliderObj.auto_collider(colliderType)
        
        # add collider to interface
        inter.add_collider_to_interface(newAnimColliderObj.collider)
        
        if autoPivot:
            newAnimColliderObj.auto_pivot()
            
        return newAnimColliderObj
