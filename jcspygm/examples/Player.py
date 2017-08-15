#  ========================================================================
#  $File: Player.py $
#  $Date: 2016-10-28 22:54:56 $
#  $Revision: $
#  $Creator: Jen-Chieh Shen $
#  $Notice: See LICENSE.txt for modification and distribution information
#                     Copyright (c) 2016 by Shen, Jen-Chieh $
#  ========================================================================

import pygame

from jcspygm.core.JCSPyGm_Camera import JCSPyGm_Camera
from jcspygm.core.JCSPyGm_GameObject import JCSPyGm_GameObject
from jcspygm.managers.JCSPyGm_CollisionManager import JCSPyGm_CollisionManager
from jcspygm.managers.JCSPyGm_SceneManager import JCSPyGm_SceneManager
from jcspygm.managers.JCSPyGm_SoundManager import JCSPyGm_SoundManager
from jcspygm.util.JCSPyGm_Debug import JCSPyGm_Debug
from jcspygm.util.JCSPyGm_Input import JCSPyGm_Input
from jcspygm.util.JCSPyGm_Physics import JCSPyGm_Physics


class Player(JCSPyGm_GameObject):

    """Player for example game."""

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
    def __init__(self, game):
        """Constructor."""
        
        # call super class.
        super(Player, self).__init__()
        
        self.camera = JCSPyGm_Camera.get_instance()
        self.sceneManager = JCSPyGm_SceneManager.get_instance();
        self.collisionManager = JCSPyGm_CollisionManager.get_instance()
        self.soundManager = JCSPyGm_SoundManager.get_instance()
        
        self.speed = 300
        
        self.jumpForce = 440
        self.__gravityProduct = 5
        
        self.lastFrameY = 0
        
        self.jumped = False
        
        self.game = game
        
    # --------------------------------------------
    # Public Methods
    # --------------------------------------------
    def update(self, deltaTime):
        """Update player game logic."""
        
        self.__player_movement(deltaTime);
        
        self.__process_input(deltaTime)
            
        super(Player, self).update(deltaTime)
        
    def is_grounded(self):
        """Check object on the ground."""
        
        if self.collisionManager.check_collide_scene(self.sceneManager.get_current_scene(), self.collider):
            return True
        
        return False
    
    def reset_player_position(self):
        """Reset the player, simulate reset the game."""
        self.set_x(0)
        self.set_y(150)
        
        # reset y velocity
        self.velY = 0
        self.jumped = True
        
        self.soundManager.play_one_shot("../../res/sounds/die", ".wav")

    # --------------------------------------------
    # Protected Methods
    # --------------------------------------------

    # --------------------------------------------
    # Private Methods
    # --------------------------------------------
    def __process_input(self, deltaTime):
        """Process Input"""
        
        #self.__test()
            
        
        # if hit the obstacle reset player position.
        if self.__hit_obstacle_in_same_interface(self.game.get_game_ground()):
            self.reset_player_position()
            
        if (
            JCSPyGm_Input.get_key_down(pygame.constants.K_SPACE) and
            not (self.jumped)
            ):
            self.velY = -self.jumpForce
            self.soundManager.play_one_shot("../../res/sounds/jump", ".wav")
            self.jumped = True 
            
        if JCSPyGm_Input.get_key_down(pygame.constants.K_r):
            self.reset_player_position()
            
        if JCSPyGm_Input.get_key_down(pygame.constants.K_e):
            self.set_x(5000 + -400)
            self.set_y(150)
            
            # reset y velocity
            self.velY = 0
            
            self.jumped = True
            
        #print(self.)
        if self.x > 6000:
            self.game.switch_to_menu_scene()
            
    def __player_movement(self, deltaTime):
        """Player movement."""
        
        # keep setting the velocity to the force.
        self.velX = self.speed
        
        self.flipX = True
        
        # is in the air.
        if not (self.is_grounded()):
            # record down the last frame.
            self.lastFrameY = self.y
            
            # apply gravity force.
            self.velY += JCSPyGm_Physics.GRAVITY_PRODUCT * JCSPyGm_Physics.GRAVITY * deltaTime * self.__gravityProduct
        # is on the ground.
        else:
            self.velY = 0
            
            if self.jumped:
                self.set_y(self.lastFrameY)
                self.jumped = False
            
            
            
    def __hit_obstacle_in_same_interface(self, inter):
        """Check if hit the obstacle."""
        
        # get the length of the collider in per interface.
        interfaceColliderlen = len(inter.get_colliders_in_interface())
        
        for index in range(interfaceColliderlen):
            
            # get the collider in this interface.
            colliderInInterface = inter.get_colliders_in_interface_by_index(index)
            
            # only check the collider that are obstacle
            if not (colliderInInterface.is_tag("Obstacle")):
                continue
            
            # and then check it with basic check
            # collide function.
            if self.collisionManager.check_collide(colliderInInterface, self.collider):
                # it did collide with somthing in this interface.
                return True
            
        # collide nothing.
        return False
    
    def __test(self):
        """Test function."""
        
        if JCSPyGm_Input.get_key(pygame.constants.K_LEFT):
            self.velX = -self.speed
            self.flipX = False
        elif JCSPyGm_Input.get_key(pygame.constants.K_RIGHT):
            self.velX = self.speed
            self.flipX = True
        else:
            self.velX = 0
             
        if JCSPyGm_Input.get_key(pygame.constants.K_DOWN):
            self.velY = self.speed
        elif JCSPyGm_Input.get_key(pygame.constants.K_UP):
            self.velY = -self.speed
        else:
            self.velY = 0
    
    # --------------------------------------------
    # setter / getter
    # --------------------------------------------
    
