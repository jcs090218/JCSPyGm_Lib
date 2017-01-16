#  ========================================================================
#  $File: JCSPyGm_Scene.py $
#  $Date: 2016-10-27 21:39:53 $
#  $Revision: $
#  $Creator: Jen-Chieh Shen $
#  $Notice: See LICENSE.txt for modification and distribution information
#                     Copyright (c) 2016 by Shen, Jen-Chieh $
#  ========================================================================



class JCSPyGm_Scene(object):

    """Handle all interface(JCSPyGm_Interface)."""

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
        
        self.__interfaces = []

    # --------------------------------------------
    # Public Methods
    # --------------------------------------------
    def on_enable_scene(self):
        """On Enable the scene.
        
        IMPORTANT(jenchieh): this function will be call evertime 
        the scene have been loaded or switch.
        """
    
    def on_disable_scene(self):
        """On Disable the scene.
        
        IMPORTANT(jenchieh): this function will be call evertime 
        the the scene is switched.
        """
        
    def initialize(self):
        """On initialize the scene.
        
        Call this function only once, cuz we dont want
        to reload assets over and over again.
        """
    
    def update(self, deltaTime):
        """Update all interface game logic."""
        
        # get the length of the array
        arrLen = len(self.__interfaces)
        
        # loop through and do the game logic
        for index in range(arrLen):
            self.__interfaces[index].update(deltaTime)
    
    def draw(self, windowInfo):
        """Update all interface graphics"""
        
        # get the length of the array
        arrLen = len(self.__interfaces)
        
        # loop through and do the render
        for index in range(arrLen):
            self.__interfaces[index].draw(windowInfo)
    
    def add_interface(self, inter):
        """Add a interface."""
        
        arrLen = len(self.__interfaces)
        
        # add one to array.
        self.__interfaces.append([])
        
        self.__interfaces[arrLen] = inter

    # --------------------------------------------
    # Protected Methods
    # --------------------------------------------

    # --------------------------------------------
    # Private Methods
    # --------------------------------------------

    # --------------------------------------------
    # setter / getter
    # --------------------------------------------
    def get_interfaces(self):
        """Return interfaces array."""
        return self.__interfaces
    
    def get_interfaces_len(self):
        """Return interfaces array length."""
        return len(self.__interfaces)
    
    def get_interface_by_index(self, index):
        """Return interface by passing in the index value."""
        return self.__interfaces[index]
