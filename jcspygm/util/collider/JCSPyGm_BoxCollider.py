#  ========================================================================
#  $File: JCSPyGm_BoxCollider.py $
#  $Date: 2016-10-31 22:40:41 $
#  $Revision: $
#  $Creator: Jen-Chieh Shen $
#  $Notice: See LICENSE.txt for modification and distribution information
#                     Copyright (c) 2016 by Shen, Jen-Chieh $
#  ========================================================================

import pygame
from jcspygm.util.JCSPyGm_Collider import JCSPyGm_Collider
from jcspygm.util.JCSPyGm_Debug import JCSPyGm_Debug


class JCSPyGm_BoxCollider(JCSPyGm_Collider):

    """Coollider Box"""

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
    def __init__(self, gmObj):
        """Constructor."""
        
        super(JCSPyGm_BoxCollider, self).__init__(gmObj)
        
        self.width = 0
        self.height = 0
        
        self.set_type("box")

    # --------------------------------------------
    # Public Methods
    # --------------------------------------------
    def update(self, deltaTime):
        """Update game logics."""
        
        super(JCSPyGm_BoxCollider, self).update(deltaTime)
        
    def draw(self, windowInfo):
        """Update game graphics."""
        
        super(JCSPyGm_BoxCollider, self).draw(windowInfo)
        
        if not JCSPyGm_Debug.DEBUG_MODE or not self.active:
            return
        
        pygame.draw.rect(
            windowInfo,
            JCSPyGm_Debug.DEBUG_COLOR, 
            (self.x, self.y, self.width, self.height))
        
    def auto_pivot(self):
        """Auto pivot the collider."""
        
        self.pivotX = self.width / 2
        self.pivotY = self.height / 2
        
    # --------------------------------------------
    # Protected Methods
    # --------------------------------------------

    # --------------------------------------------
    # Private Methods
    # --------------------------------------------

    # --------------------------------------------
    # setter / getter
    # --------------------------------------------
    def get_width(self):
        """Return width of the collider."""
        return self.width;
    
    def set_width(self, val):
        """Set width of the collider."""
        self.width = val;
        self.auto_pivot()
    
    def get_height(self):
        """Return height of the collider."""
        return self.height;
    
    def set_height(self, val):
        """Set height of the collider."""
        self.height = val;
        self.auto_pivot()
