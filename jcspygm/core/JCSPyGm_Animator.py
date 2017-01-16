#  ========================================================================
#  $File: JCSPyGm_Animator.py $
#  $Date: 2016-10-27 21:43:18 $
#  $Revision: $
#  $Creator: Jen-Chieh Shen $
#  $Notice: See LICENSE.txt for modification and distribution information
#                     Copyright (c) 2016 by Shen, Jen-Chieh $
#  ========================================================================
from jcspygm.core.JCSPyGm_Animation import JCSPyGm_Animation
from jcspygm.util.JCSPyGm_Debug import JCSPyGm_Debug


class JCSPyGm_Animator(object):

    """Handle transition of mutliple animation."""

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
        
        # array pointer holds all the animation in
        # this animator.
        self.__animations = []
        
        self.__currentAnimation = None

    # --------------------------------------------
    # Public Methods
    # --------------------------------------------
    def update(self, deltaTime):
        """Update the animator game logic."""
        
        # check current animation available to use.
        if self.__currentAnimation is None:
            return
        
        self.__currentAnimation.update(deltaTime)
        
    def draw(self, windowInfo):
        """Update the animator game graphics."""
        
        # check current animation available to use.
        if self.__currentAnimation is None:
            return
        
        self.__currentAnimation.draw(windowInfo)
        
    def switch_animation(self, newAnimIndex):
        """Switch the current animation to new animation."""
        
        if self.__animations[newAnimIndex] is None:
            JCSPyGm_Debug.Error("Animation index u pass in does not exists.")
            return
        
        # switch the current animation to new animations.
        self.__currentAnimation = self.__animations[newAnimIndex]
        
    def load_animation_and_add(self, filePath, baseName, ext, frameCount):
        """Create a animation and add it into animator system."""
        
        # create the new animation object.
        newAnim = JCSPyGm_Animation()
        
        # load the animation.
        newAnim.load_animation(filePath, baseName, ext, frameCount)
        
        # add the animation we just created.
        self.add_animation(newAnim)
        
    def add_animation(self, newAnim):
        """Add the animation into current animator system."""
        
        self.__animations.append([])
        
        # add the animation into array
        self.__animations[len(self.__animations) - 1] = newAnim
        
    def remove_animation(self, newAnim):
        """Remove the animation from the animator system."""
        
        # TODO(jenchieh): finish this function.
        
    def auto_pivot(self):
        """Auto pivot all the animations in system."""
        
        for index in range(self.get_animations_len()):
            self.get_animations_at(index).auto_pivot()

    # --------------------------------------------
    # Protected Methods
    # --------------------------------------------

    # --------------------------------------------
    # Private Methods
    # --------------------------------------------

    # --------------------------------------------
    # setter / getter
    # --------------------------------------------
    def get_current_animation(self):
        """Return currently play animation."""
        return self.__currentAnimation
    
    def get_animations_at(self, index):
        """Return the animation at index of."""
        return self.__animations[index]
    
    def get_animations_len(self):
        """Return the length of the animations in animator system."""
        return len(self.__animations)
