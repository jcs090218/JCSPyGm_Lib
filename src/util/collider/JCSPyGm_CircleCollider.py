#  ========================================================================
#  $File: JCSPyGm_CircleCollider.py $
#  $Date: 2016-10-31 22:41:04 $
#  $Revision: $
#  $Creator: Jen-Chieh Shen $
#  $Notice: See LICENSE.txt for modification and distribution information
#                     Copyright (c) 2016 by Shen, Jen-Chieh $
#  ========================================================================

import pygame

from src.util.JCSPyGm_Collider import JCSPyGm_Collider
from src.util.JCSPyGm_Debug import JCSPyGm_Debug


class JCSPyGm_CircleCollider(JCSPyGm_Collider):

    """Collider circle"""

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
        
        super(JCSPyGm_CircleCollider, self).__init__(gmObj)
        
        self.radius = 0.0
        
        self.set_type("circle")

    # --------------------------------------------
    # Public Methods
    # --------------------------------------------
    def update(self, deltaTime):
        """Update game logics."""
        
        super(JCSPyGm_CircleCollider, self).update(deltaTime)
        
    def draw(self, windowInfo):
        """Update game graphics."""
        
        super(JCSPyGm_CircleCollider, self).draw(windowInfo)
        
        if not JCSPyGm_Debug.DEBUG_MODE or not self.active:
            return
        
        pygame.draw.circle(
            windowInfo, 
            JCSPyGm_Debug.DEBUG_COLOR,
            (int(self.x), int(self.y)),
            int(self.radius), 
            int(0))
        
    def auto_pivot(self):
        """Auto pivot the collider."""
        
        # you do not need to auto pivot the circle
        
    # --------------------------------------------
    # Protected Methods
    # --------------------------------------------

    # --------------------------------------------
    # Private Methods
    # --------------------------------------------

    # --------------------------------------------
    # setter / getter
    # --------------------------------------------
    def get_raidus(self):
        """Return radius."""
        return self.radius
