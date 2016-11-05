#  ========================================================================
#  $File: JCSPyGm_Collision.py $
#  $Date: 2016-10-14 22:33:12 $
#  $Revision: $
#  $Creator: Jen-Chieh Shen $
#  $Notice: See LICENSE.txt for modification and distribution information
#                     Copyright (c) 2016 by Shen, Jen-Chieh $
#  ========================================================================

import math
from src.util.JCSPyGm_Math import JCSPyGm_Math
from nt import stat


class JCSPyGm_Collision(object):

    """Collision utilities methods design here..."""


    @staticmethod
    def rect_to_rect(rectA, rectB):
        """Simple AABB test.

        @param rectA->rectangle A
        @param rectB->rectangle B

        @return 
        true->touch
        false->not touch
        """
        
        if (rectA.x + rectA.width > rectB.x and 
            rectA.x < rectB.x + rectB.width and 
            rectA.y + rectA.height > rectB.y and 
            rectA.y < rectB.y + rectB.height):
            return True

        return False

    @staticmethod
    def circle_to_circle(circA, circB):
        """Simple Circle to circle collision
        check.

        @param circA->circle A
        @param circB->circle B

        @return 
        true->touch
        false->not touch
        """
        
        distance = JCSPyGm_Collision.point_distance(circA, circB)
        
        if distance < circA.get_raidus() + circB.get_raidus():
            return True

        return False

    @staticmethod
    def rect_to_circle(rect, circ):
        """Check collision rectangle
        and circle.

        @param rect->rectangle
        @param circ->circle

        @return 
        true->touch
        false->not touch
        """
        
        cx = rect.x + rect.width / 2
        cy = rect.y + rect.height / 2
        
        px = circ.x
        py = circ.y
        
        vx = JCSPyGm_Collision.one_dimension(cx, px)
        vy = JCSPyGm_Collision.one_dimension(cy, py)
        
        side1 = JCSPyGm_Math.abs(rect.x - (rect.x + rect.width))
        side2 = JCSPyGm_Math.abs(rect.y - (rect.y + rect.height))
        
        hx = side1 / 2
        hy = side2 / 2
        
        ux = max(vx - hx, 0)
        uy = max(vy - hy, 0)
        
        return JCSPyGm_Math.dot_product(ux, uy, ux, uy) <= circ.radius * circ.radius
    
    @staticmethod
    def point_distance(p1, p2):
        """Return distance between two point."""
        
        vDistance = JCSPyGm_Math.abs(p1.x - p2.x)
        hDistance = JCSPyGm_Math.abs(p1.y - p2.y)
        
        return math.sqrt(math.pow(vDistance, 2) + math.pow(hDistance, 2))
    
    @staticmethod
    def one_dimension(a, b):
        return JCSPyGm_Math.abs(a - b)
