#  ========================================================================
#  $File: JCSPyGm_Input.py $
#  $Date: 2016-10-14 22:41:37 $
#  $Revision: $
#  $Creator: Jen-Chieh Shen $
#  $Notice: See LICENSE.txt for modification and distribution information
#                     Copyright (c) 2016 by Shen, Jen-Chieh $
#  ========================================================================

import pygame


class JCSPyGm_Input:

    """Input hanlde."""
    
    mouseDownThisFrame = False
    mouseIsDown = False
    mouseUpThisFrame = False
    mousePosition = (0, 0)
    
    keysPressedThisFrame = []
    keysDown = []
    keysReleasedThisFrame = []


    @staticmethod
    def clean_input_buffer():
        """Update the key meta table."""
        
        # reset mouse states
        JCSPyGm_Input.mouseDownThisFrame = False
        JCSPyGm_Input.mouseUpThisFrame = False
        
        # reset key array
        JCSPyGm_Input.keysPressedThisFrame = []
        JCSPyGm_Input.keysReleasedThisFrame = []
        

    @staticmethod
    def get_key_down(keyCode):
        """Check whether the given key was pressed this frame."""
        
        # To use static variables, you must reference the class.
        for key in JCSPyGm_Input.keysPressedThisFrame:
            
            # We found the key being requested.
            if key == keyCode:
                return True
         
        # We did not find the requested key.   
        return False

    @staticmethod
    def get_key(keyCode):
        """Check whether the given key is pressed."""
        
        for key in JCSPyGm_Input.keysDown:
            if key == keyCode:
                return True
         
        return False

    @staticmethod
    def get_key_up(keyCode):
        """Check whether the given key was released this frame."""
        
        for key in JCSPyGm_Input.keysReleasedThisFrame:
            if key == keyCode:
                return True
         
        return False
    
    @staticmethod
    def get_mouse_x():
        """Get mouse position on x-axis."""
        pX, pY = pygame.mouse.get_pos()
        return pX
    
    @staticmethod
    def get_mouse_y():
        """Get mouse position on x-axis."""
        pX, pY = pygame.mouse.get_pos()
        return pY
    
    @staticmethod
    def get_mouse_button():
        """Check whether the mouse is held down."""
        return JCSPyGm_Input.mouseIsDown
    
    @staticmethod
    def get_mouse_button_down():
        """Check whether the mouse was pressed this frame."""
        return JCSPyGm_Input.mouseDownThisFrame
    
    @staticmethod
    def get_mouse_button_up():
        """Check whether the mouse was released this frame."""
        return JCSPyGm_Input.mouseUpThisFrame
