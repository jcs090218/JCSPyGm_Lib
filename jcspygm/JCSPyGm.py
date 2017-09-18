#  ========================================================================
#  $File: JCSPyGm.py $
#  $Date: 2016-10-19 22:13:20 $
#  $Revision: $
#  $Creator: Jen-Chieh Shen $
#  $Notice: See LICENSE.txt for modification and distribution information
#                     Copyright (c) 2016 by Shen, Jen-Chieh $
#  ========================================================================

import pygame


class JCSPyGm:
    """Core JCSPyGm Lib"""
    
    @staticmethod
    def init():
        """Initialize the JCSPyGm"""

        # initialize the sound API
        pygame.mixer.init()

        # initialize the pygame API
        pygame.init()
