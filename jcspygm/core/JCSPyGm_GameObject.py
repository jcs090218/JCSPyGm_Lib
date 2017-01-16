#  ========================================================================
#  $File: JCSPyGm_GameObject.py $
#  $Date: 2016-10-27 23:00:07 $
#  $Revision: $
#  $Creator: Jen-Chieh Shen $
#  $Notice: See LICENSE.txt for modification and distribution information
#                     Copyright (c) 2016 by Shen, Jen-Chieh $
#  ========================================================================

import math
import time

import pygame

from jcspygm.core.JCSPyGm_Animation import JCSPyGm_Animation
from jcspygm.core.JCSPyGm_Animator import JCSPyGm_Animator
from jcspygm.core.JCSPyGm_Sprite import JCSPyGm_Sprite
from jcspygm.util.JCSPyGm_Debug import JCSPyGm_Debug
from jcspygm.util.collider.JCSPyGm_BoxCollider import JCSPyGm_BoxCollider
from jcspygm.util.collider.JCSPyGm_CircleCollider import JCSPyGm_CircleCollider


class JCSPyGm_GameObject(object):

    """Game Object for JCSPyGm Library."""

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

        self.active = True
        
        # get if own pointers for convenience use.
        self.gameObject = self

        self.__animation = None
        self.__sprite = None
        self.__animator = JCSPyGm_Animator()

        # use for camera
        self.camX = 0
        self.camY = 0

        # global position.
        self.x = 0
        self.y = 0

        # velocity
        self.velX = 0
        self.velY = 0

        self.flipX = False
        self.flipY = False

        self.scaleX = 1
        self.scaleY = 1

        # Color attribute.
        self.r = 255
        self.g = 255
        self.b = 255
        self.a = 255

        # trigger of fading.
        self.__fading = False

        # True: fading in. False: fading out.
        self.__fadeIn = False

        # declare the collider pointer.
        self.collider = None

        # some identity value setting.
        self.name = ""
        self.tag = ""

    # --------------------------------------------
    # Public Methods
    # --------------------------------------------
    def update(self, deltaTime):
        """Update the game object logic."""

        # check if active component?
        if not (self.active):
            return

        # update game logic by priority
        if not (self.__animator.get_animations_len() is 0):
            self.__animator.update(deltaTime)
        elif not (self.__animation is None):
            self.__animation.update(deltaTime)
        elif not (self.__sprite is None):
            self.__sprite.update(deltaTime)

        # apply force.
        self.camX += self.velX * deltaTime
        self.camY += self.velY * deltaTime

        # apply force.
        self.x += self.velX * deltaTime
        self.y += self.velY * deltaTime

        self.__do_fading(deltaTime)

        if not (self.collider is None):
            # update collider
            self.collider.update(deltaTime)

    def draw(self, windowInfo):
        """Update the game object graphics."""

        # check if active component?
        if not (self.active):
            return

        # draw by priority
        if not (self.__animator.get_animations_len() is 0):
            self.__animator.draw(windowInfo)
        elif not (self.__animation is None):
            self.__animation.draw(windowInfo)
        elif not (self.__sprite is None):
            self.__sprite.draw(windowInfo)

        if not (self.collider is None):
            # draw collider
            self.collider.draw(windowInfo)

    def load_sprite(self, filePath, ext):
        """Load the sprite from path."""

        # create new sprite instance.
        self.__sprite = JCSPyGm_Sprite(self)

        # load the sprite from the sprite
        # instance we just created.
        self.__sprite.load_sprite(filePath, ext)

    def load_animation(self, filePath, baseName, ext, frameCount):
        """Load the animation from path.
        
        filePath : string to the file
        baseName: base file name of the animation.
        ext : extension string
        frameCount : how many frame in the animation? = sprite count
        """

        # create new animation instance.
        self.__animation = JCSPyGm_Animation(self)

        # load the animation from the animation
        # instance we just created.
        self.__animation.load_animation(filePath, baseName, ext, frameCount)

    def auto_pivot(self):
        """Auto pivto depend on either animation/sprite we have."""

        if not (self.__animator.get_animations_len() is 0):
            self.__animator.auto_pivot()
        elif not (self.__animation is None):
            self.__animation.auto_pivot()
        elif not (self.__sprite is None):
            self.__sprite.auto_pivot()
        else:
            JCSPyGm_Debug.Error("Failed to auto pivot the game object. "
                                "Make sure they have either animation "
                                "or sprite available.")

        if not (self.collider is None):
            self.collider.auto_pivot()

    def auto_collider(self, colliderType):
        """Setup the collider base on the image size."""

        # declare macros.
        radius = -1
        width = -1
        height = -1

        # create collider
        if colliderType is "circle":

            self.collider = JCSPyGm_CircleCollider(self)

            if not (self.__animator.get_animations_len() is 0):
                # get the first sprite's rect.
                animFirstSpriteRect = self.__animator.get_animations_at(0).get_sprite_at(0).get_sprite_rect()

                width = animFirstSpriteRect.width
                height = animFirstSpriteRect.height
            elif not (self.__animation is None):
                # get the first sprite's rect.
                animFirstSpriteRect = self.__animation.get_sprite_at(0).get_sprite_rect()

                width = animFirstSpriteRect.width
                height = animFirstSpriteRect.height
            elif not (self.__sprite is None):
                spriteRect = self.__sprite.get_sprite_rect()

                width = spriteRect.width
                height = spriteRect.height

            # get the radius by Pythagorean Theorem
            radius = math.sqrt(math.pow(width, 2) + math.pow(height, 2)) / 2

            self.collider.radius = radius

        elif colliderType is "box":

            self.collider = JCSPyGm_BoxCollider(self)

            if not (self.__animator.get_animations_len() is 0):
                # get the first animation's sprite's rect.
                animFirstSpriteRect = self.__animator.get_animations_at(0).get_sprite_at(0).get_sprite_rect()

                width = animFirstSpriteRect.width
                height = animFirstSpriteRect.height
            elif not (self.__animation is None):
                # get the first sprite's rect.
                animFirstSpriteRect = self.__animation.get_sprite_at(0).get_sprite_rect()

                width = animFirstSpriteRect.width
                height = animFirstSpriteRect.height
            elif not (self.__sprite is None):
                spriteRect = self.__sprite.get_sprite_rect()

                width = spriteRect.width
                height = spriteRect.height

            self.collider.width = width
            self.collider.height = height

    def fade_out(self, time):
        """Fade out the game object.
        
        NOTE(jenchieh): better design to have it as the 
        composition/component, not just hard coded.
        
        @param time: How long it fade?
        """

        # check if is still fading
        if self.__fading:
            return

        # active gameobject.
        self.active = True

        self.a = 255

        # turn on the fading trigger.
        self.__fading = True

        self.__fadeTime = time

        # TODO(jenchieh): use enum for better design.
        # do fade out.
        self.__fadeIn = False

        # make sure the timer is zero.
        self.__fadeTimer = 0

    def fade_in(self, time):
        """Fade in the game object.
        
        NOTE(jenchieh): better design to have it as the 
        composition/component, not just hard coded.
        
        @param time: How long it fade?
        """

        # check if is still fading
        if self.__fading:
            return

        # active gameobject.
        self.active = True

        self.a = 0

        # turn on the fading trigger.
        self.__fading = True

        self.__fadeTime = time

        # TODO(jenchieh): use enum for better design.
        # do fade in.
        self.__fadeIn = True

        # make sure the timer is zero.
        self.__fadeTimer = 0

    def is_fade_out(self):
        """Check if fade out."""
        return (self.a <= 0)

    def is_fade_in(self):
        """Check if fade in."""
        return (self.a >= 255)

    def is_name(self, cmpName):
        """Check the same name."""
        return self.name is cmpName

    def is_tag(self, cmpTag):
        """Check the same tag."""
        return self.tag is cmpTag

    # --------------------------------------------
    # Protected Methods
    # --------------------------------------------

    # --------------------------------------------
    # Private Methods
    # --------------------------------------------
    def __do_fading(self, deltaTime):
        """Do fading algorithm here."""

        # check if the trigger open space.
        if not (self.__fading):
            return

        # do fade in here.
        if self.__fadeIn:
            self.a += 255 / self.__fadeTime * deltaTime

            if self.a > 255:

                self.a = 255

                # end effect.
                self.__fading = False

        # do fade out here.
        else:
            self.a -= 255 / self.__fadeTime * deltaTime

            if self.a < 0:
                self.a = 0

                # end effect.
                self.__fading = False

    # --------------------------------------------
    # setter / getter
    # --------------------------------------------
    def set_x(self, newX):
        """Set the x position."""
        dif = newX - self.x
        self.camX += dif
        self.x = newX
        
    def set_y(self, newY):
        """Set the y position."""
        dif = newY - self.y
        self.camY += dif
        self.y = newY
    
    def set_sprite(self, newSprite):
        """Set sprite."""
        self.__sprite = newSprite

    def set_animation(self, newAnim):
        """Set animation."""
        self.__animation = newAnim

    def get_sprite(self):
        """Return sprite object."""
        return self.__sprite

    def get_animation(self):
        """Return animation object."""
        return self.__animation

    def get_fading(self):
        """"Return is fading trigger."""
        return self.__fading

    def set_animator(self, newAnimator):
        """Set the animator."""
        self.__animator = newAnimator

    def get_animator(self):
        """Return the animator pointer."""
        return self.__animator

    def set_collider_type(self, colliderType):
        """Create instance and set the collider type."""

        if colliderType is "circle":
            self.collider = JCSPyGm_CircleCollider(self)
        elif colliderType is "box":
            self.collider = JCSPyGm_BoxCollider(self)
        else:
            JCSPyGm_Debug.Error("Failed to set collider type... "
            "No Type: [" + colliderType + "]")

