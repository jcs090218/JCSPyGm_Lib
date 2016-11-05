#  ========================================================================
#  $File: JCSPyGm_SoundManager.py $
#  $Date: 2016-10-27 22:10:59 $
#  $Revision: $
#  $Creator: Jen-Chieh Shen $
#  $Notice: See LICENSE.txt for modification and distribution information
#                     Copyright (c) 2016 by Shen, Jen-Chieh $
#  ========================================================================

import pygame
from src.util.JCSPyGm_Debug import JCSPyGm_Debug


class JCSPyGm_SoundManager(object):

    """Manager class handle all the sound buffer I/O."""

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
        """Constructor."""
        
        # create sound instance buffer holder.
        self.sound = None
        self.bgm = None
        
        self.__timeToFadeBGM = 1000 * 1 # milliseconds
        
        self.__volume = 0
        
    @staticmethod
    def get_instance():
        """Singleton pattern."""
        if JCSPyGm_SoundManager.instance is None:
            JCSPyGm_SoundManager.instance = JCSPyGm_SoundManager()
        
        return JCSPyGm_SoundManager.instance

    # --------------------------------------------
    # Public Methods
    # --------------------------------------------
    def play_one_shot(self, filePath, ext):
        """Play one shot of sound.
        
        @param filePath: file to the sound.
        @param ext: extension of the file.
        """
        
        fullFilePath = filePath + ext
        
        self.sound = pygame.mixer.Sound(fullFilePath)
        
        self.sound.play()
        
    def play_bgm(self, filePath, ext, fadeInMs = 0):
        """Play background music.
        
        @param filePath: file to the sound.
        @param ext: extension of the file.
        """
        
        fullFilePath = filePath + ext
        
        self.bgm = pygame.mixer.Sound(fullFilePath)
        
        # loop is negative sign
        loops = -1
        
        fade_ms = fadeInMs
        
        pygame.mixer.fadeout(fade_ms)
        
        self.bgm.play(loops, fade_ms = fade_ms)
        
    def stop_bgm(self, fadeOutMs = 0):
        """Stop background music.
        
        @param fadeOut: fade out before stopping.
        """
        # check if okay to stop background music.
        if self.bgm is None:
            JCSPyGm_Debug.Error("Cannot fade out the sound with null references...")
            return
        
        self.bgm.fadeout(fadeOutMs)
    
    def mute(self):
        """Mute the mixer."""
        pygame.mixer.stop()
        
    def set_volume(self, val):
        """Set the volume of this mixer.
        
        Set the volume of the music playback. The 
        value argument is between 0.0 and 1.0. 
        When new music is loaded the volume is reset.
        """
        
        self.__volume = val
        
        pygame.mixer.music.set_volume(val)
        
    # --------------------------------------------
    # Protected Methods
    # --------------------------------------------

    # --------------------------------------------
    # Private Methods
    # --------------------------------------------

    # --------------------------------------------
    # setter / getter
    # --------------------------------------------
