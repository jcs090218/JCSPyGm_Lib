#  ========================================================================
#  $File: JCSPyGm_Animation.py $
#  $Date: 2016-10-27 20:20:37 $
#  $Revision: $
#  $Creator: Jen-Chieh Shen $
#  $Notice: See LICENSE.txt for modification and distribution information
#                     Copyright (c) 2016 by Shen, Jen-Chieh $
#  ======================================================================== 

from jcspygm.util.JCSPyGm_Debug import JCSPyGm_Debug
from jcspygm.core.JCSPyGm_Sprite import JCSPyGm_Sprite


class JCSPyGm_Animation(object):

    """Handle animation and provide related functions."""

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
        
        # default component active?
        self.active = True
        
        self.gameObject = gameObj
        
        # default timer per frame
        self.__timePerFrame = 0.15
        
        # timer for calculate each animation frame displayed.
        self.__timer = 0
        
        # create the table of the sprites.
        self.__sprites = []
        
        # current frame this animation are rendering.
        self.__currentFrame = 0
        
        # total frame count
        self.__frameCount = -1

    # --------------------------------------------
    # Public Methods
    # --------------------------------------------
    def update(self, deltaTime):
        """Update the animation frame logic"""
        
        # check if the component active?
        if not self.active:
            return
        
        # update the single frame base on the current frame.
        self.__sprites[self.__currentFrame].update(deltaTime)
        
        # --------------------------------------
        # start the timer
        self.__timer += deltaTime
        
        if self.__timer < self.__timePerFrame:
            return
        
        # reset timer
        self.__timer = 0
        
        # increase frame 
        self.__currentFrame += 1

        # check if out of range.
        if self.__currentFrame >= self.__frameCount:
            
            # start the animation back from the beginning.
            self.__currentFrame = 0
        
        
    def draw(self, windowInfo):
        """Draw the animation frame."""
        
        # check if the component active?
        if not self.active:
            return
        
        # draw the single frame base on the current frame.
        self.__sprites[self.__currentFrame].draw(windowInfo)
        
    def load_animation(self, filePath, baseName, ext, frameCount):
        """Load the animation from path.
        
        filePath : string to the file
        baseName: base file name of the animation.
        ext : extension string
        frameCount : how many frame in the animation? = sprite count
        """

        # check the frame count.
        if frameCount <= 0 :
            JCSPyGm_Debug.Error("Frame count cannot be lower "
             "than/equal to zero...")
            
        self.__frameCount = frameCount

        # this will loop through 0 - frame count.
        for index in range(frameCount):
            
            # setup the full path
            fullPath = filePath + baseName + str(index)
            
            # Place new column in the grid.
            self.__sprites.append([])
            
            # create sprite instance
            self.__sprites[index] = JCSPyGm_Sprite(self.gameObject)
            
            # load the sprite base on the full file path
            self.__sprites[index].load_sprite(fullPath, ext)
        
    def auto_pivot(self):
        """Auto pivot all the sprite."""
        
        # auto pivot all the sprite.
        for index in range(self.__frameCount):
            self.__sprites[index].auto_pivot()

    # --------------------------------------------
    # Protected Methods
    # --------------------------------------------

    # --------------------------------------------
    # Private Methods
    # --------------------------------------------

    # --------------------------------------------
    # setter / getter
    # --------------------------------------------d
    def set_time_per_frame(self, newTime):
        """Set time per frame value."""
        self.__timePerFrame = newTime
        
    def get_frame_count(self):
        """Return the total frame count in this animation."""
        return self.__frameCount
    
    def get_sprite_at(self, index):
        """Return sprite at frame."""
        return self.__sprites[index]
