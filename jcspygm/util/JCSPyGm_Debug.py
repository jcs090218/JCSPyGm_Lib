#  ========================================================================
#  $File: JCSPyGm_Debug.py $
#  $Date: 2016-10-27 20:36:34 $
#  $Revision: $
#  $Creator: Jen-Chieh Shen $
#  $Notice: See LICENSE.txt for modification and distribution information
#                     Copyright (c) 2016 by Shen, Jen-Chieh $
#  ========================================================================



class JCSPyGm_Debug(object):

    """Debug the for the library."""

    # --------------------------------------------
    # Public Variables
    # --------------------------------------------
    DEBUG_MODE = False
    DEBUG_COLOR = (255, 255, 255, 127)
    
    # --------------------------------------------
    # Private Variables
    # --------------------------------------------

    # --------------------------------------------
    # Protected Variables
    # --------------------------------------------

    # --------------------------------------------
    # Constructor
    # --------------------------------------------

    # --------------------------------------------
    # Public Methods
    # --------------------------------------------
    @staticmethod
    def Error(log):
        print("\n***")
        print("* JCSPyGm - Error: " + log)
        print("***\n")
        
    @staticmethod
    def Warning(log):
        print("\n***")
        print("* JCSPyGm - Warning: " + log)
        print("***\n")
        
    @staticmethod
    def Log(log):
        print("\n***")
        print("* JCSPyGm - Log: " + log)
        print("***\n")

    # --------------------------------------------
    # Protected Methods
    # --------------------------------------------

    # --------------------------------------------
    # Private Methods
    # --------------------------------------------

    # --------------------------------------------
    # setter / getter
    # --------------------------------------------
