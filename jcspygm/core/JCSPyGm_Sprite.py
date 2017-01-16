#  ========================================================================
#  $File: JCSPyGm_Sprite.py $
#  $Date: 2016-10-27 20:44:19 $
#  $Revision: $
#  $Creator: Jen-Chieh Shen $
#  $Notice: See LICENSE.txt for modification and distribution information
#                     Copyright (c) 2016 by Shen, Jen-Chieh $
#  ========================================================================

import pygame

from jcspygm.util.JCSPyGm_Debug import JCSPyGm_Debug


class JCSPyGm_Sprite(object):

    """Handle sprite info."""

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
    def __init__(self, gameObj):
        """Constructor."""
        
        self.active = True
        self.gameObject = gameObj
        
        # create the sprite buffer pointer.
        self.__sprite = None
        self.__spriteSurface = None
        
        self.__spriteRect = None
        
        self.flipXVal = 0
        self.flipYVal = 0
        
        self.faceLeft = True
        self.faceUp = True
        
        self.pivotOffsetX = 0
        self.pivotOffsetY = 0

    # --------------------------------------------
    # Public Methods
    # --------------------------------------------
    def update(self, deltaTime):
        """Update sprite logic."""
        
        # check if the component active?
        if not self.active:
            return
        
        # Override the position directly from 
        # the game object
        self.__spriteRect.x = self.gameObject.camX - self.pivotOffsetX
        self.__spriteRect.y = self.gameObject.camY - self.pivotOffsetY
        
    def draw(self, windowInfo):
        """Update the graphics"""
        
        # check if the component active?
        if not self.active:
            return
        
        # NOTE(jenchieh): some reason do this again
        # in order to get the sprite work correctly...
        
        # -----------------------------------------
        # check position
        # -----------------------------------------
        self.__spriteRect.x = self.gameObject.camX - self.pivotOffsetX
        self.__spriteRect.y = self.gameObject.camY - self.pivotOffsetY
        
        # -----------------------------------------
        # check flip
        # -----------------------------------------
        doFlip = False
        
        if self.gameObject.flipX and self.faceLeft:
            self.flipXVal = 1
            doFlip = True
            self.faceLeft = False
            
        elif not self.gameObject.flipX and not self.faceLeft:
            self.flipXVal = 1
            doFlip = True
            self.faceLeft = True
            
        if self.gameObject.flipY and self.faceUp:
            self.flipYVal = 1
            doFlip = True
            self.faceUp = False
            
        elif not self.gameObject.flipY and not self.faceUp:
            self.flipYVal = 1
            doFlip = True
            self.faceUp = True
        
        
        if doFlip:
            self.__sprite = pygame.transform.flip(
                self.__sprite, 
                self.flipXVal, 
                self.flipYVal)
            
            # set back to zero.
            self.flipXVal = 0
            self.flipYVal = 0
            
        # -----------------------------------------
        # check scale
        # -----------------------------------------
        
        # -----------------------------------------
        # check rotation
        # -----------------------------------------
        
        # -----------------------------------------
        # check color
        # -----------------------------------------
        #self.__sprite.set_alpha(self.gameObject.a)
        
        if self.gameObject.get_fading() or doFlip:
            self.__spriteSurface = JCSPyGm_Sprite.get_colored(
                self.__sprite,
                self.gameObject.r,
                self.gameObject.g,
                self.gameObject.b, 
                self.gameObject.a)
        
        # -----------------------------------------
        # draw the sprite using pygame api
        # -----------------------------------------
        #windowInfo.blit(self.__sprite, self.__spriteRect)
        
        # SOURCE(jenchieh): 
        # http://thepythongamebook.com/en:resources:people:jens_horst:colordemo
        windowInfo.blit(self.__spriteSurface, self.__spriteRect)
        
    def load_sprite(self, filePath, ext):
        """Load the sprite from path."""
        
        fullPath = filePath + ext
        
        # load the sprite using pygame api
        self.__sprite = pygame.image.load(fullPath)
        
        # convert to 32 bit.
        self.__sprite = self.__sprite.convert_alpha()
        
        self.__spriteSurface = JCSPyGm_Sprite.get_colored(
            self.__sprite, 
            self.gameObject.r,
            self.gameObject.g,
            self.gameObject.b,
            self.gameObject.a)
        
        # get the sprite rect using pygame api
        self.__spriteRect = self.__sprite.get_rect()
        
    def auto_pivot(self):
        """Auto Pivot the image by their own width and height."""
        
        if self.__spriteRect is None:
            JCSPyGm_Debug.Error("Auto pivot with out the sprite is not legal...")
            
            return
        
        self.pivotOffsetX = self.__spriteRect.width / 2
        self.pivotOffsetY = self.__spriteRect.height / 2
        
    @staticmethod
    def get_colored(surf, r, g, b, a):
        """returns a copy of a surface object with user-defined alpha-value (0-255)"""
        
        tmp = pygame.Surface(surf.get_size(), pygame.SRCALPHA, 32)
        tmp.fill((r, g, b, a))
        tmp.blit(surf, (0,0), surf.get_rect(), pygame.BLEND_RGBA_MULT)
        return tmp
    
    # --------------------------------------------
    # Protected Methods
    # --------------------------------------------

    # --------------------------------------------
    # Private Methods
    # --------------------------------------------

    # --------------------------------------------
    # setter / getter
    # --------------------------------------------
    def get_sprite(self):
        """"Return the sprite pointer."""
        return self.__sprite
    
    def get_sprite_rect(self):
        """Return the sprite rect."""
        return self.__spriteRect
