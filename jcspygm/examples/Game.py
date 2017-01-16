#  ========================================================================
#  $File: Game.py $
#  $Date: 2016-10-14 19:26:29 $
#  $Revision: $
#  $Creator: Jen-Chieh Shen $
#  $Notice: See LICENSE.txt for modification and distribution information
#                     Copyright (c) 2016 by Shen, Jen-Chieh $
#  ========================================================================

import time

import pygame

from jcspygm.core.JCSPyGm_GameObject import JCSPyGm_GameObject
from jcspygm.core.JCSPyGm_Interface import JCSPyGm_Interface
from jcspygm.core.JCSPyGm_Scene import JCSPyGm_Scene
from jcspygm.examples.Camera import Camera
from jcspygm.examples.GameScene import GameScene
from jcspygm.examples.Player import Player
from jcspygm.managers.JCSPyGm_CollisionManager import JCSPyGm_CollisionManager
from jcspygm.managers.JCSPyGm_SceneManager import JCSPyGm_SceneManager
from jcspygm.managers.JCSPyGm_SoundManager import JCSPyGm_SoundManager
from jcspygm.util.JCSPyGm_Debug import JCSPyGm_Debug
from jcspygm.util.JCSPyGm_Input import JCSPyGm_Input
from jcspygm.util.JCSPyGm_Util import JCSPyGm_Util


class Game:

    """Game instance that all the framework feature
    will be tested here.
    """
    
    # TODO(jenchieh):Weather check if the game is pause or not.
    # Wrap into application in the future.
    gamePause = False
    
    spriteDir = "../../res/sprites/"
    soundDir = "../../res/sounds/"
    
    BGM_SOUND_FADEIN_TIME = 1000 * 1
    BGM_SOUND_FADEOUT_TIME = 1000 * 1
    
    def __init__(self):
        """Constructor
        made the instance of the game.
        """

        # system specific
        self.gamePause = False
        
        self.initialize()

    def run(self, deltaTime, windowInfo):
        """Run the program here."""

        if not self.gamePause:
            self.update(deltaTime)
            self.draw(windowInfo)
        else:
            time.sleep(100)

    def update(self, deltaTime):
        """Update the game logic

        float: value of delatTime
        """
        
        self.process_input(deltaTime)
        
        # update managers.
        self.sceneManager.update(deltaTime)
        
        
        if self.sceneManager.get_current_scene() is self.gameScene:
            # update camera.
            self.camera.update(deltaTime)
        
        
        self.camera.get_jcspygm_camera().update(deltaTime)

    def draw(self, windowInfo):
        """Main render layer graphics
        """
        
        # draw managers.
        self.sceneManager.draw(windowInfo)
        
    def initialize(self):
        """Initialize the game."""
        
        # create singleton object. (camera, manager , etc.)
        self.player = Player(self)
        self.camera = Camera(self.player)
        
        self.init_scene()
        
        self.init_game_object()
        
    def init_scene(self):
        """Initalize scenes and interfaces."""
        
        #self.camera = JCSPyGm_Camera.get_instance()
        self.sceneManager = JCSPyGm_SceneManager.get_instance()
        self.soundManager = JCSPyGm_SoundManager.get_instance()
        self.collisionManager = JCSPyGm_CollisionManager.get_instance()
        
        # play background music here...
        self.soundManager.play_bgm(Game.soundDir + "test", ".ogg", Game.BGM_SOUND_FADEIN_TIME)
        
        self.init_menu_scene()
        self.init_game_scene()
        
        # set the game scene to the current scene.
        self.sceneManager.switch_scene_with_bgm(self.menuScene, Game.soundDir + "test", ".ogg")
        
    def init_menu_scene(self):
        """Initialize the menu scene."""
        
        # create one scene.
        self.menuScene = JCSPyGm_Scene()
        
        # create basic layer of 2d platformer game.
        self.menu_backGround = JCSPyGm_Interface()
        self.menu_midGround = JCSPyGm_Interface()
        self.menu_gameGround = JCSPyGm_Interface()
        self.menu_foreGround = JCSPyGm_Interface()
        
        self.menu_backGround.set_friction(0.5)
        self.menu_midGround.set_friction(0.75)
        self.menu_gameGround.set_friction(1.0)
        self.menu_foreGround.set_friction(1.0)
        
        # add all interface to the scene.
        # IMPORTANT(jenchieh): plz add the 
        # interface in correct order. 
        self.menuScene.add_interface(self.menu_backGround)
        self.menuScene.add_interface(self.menu_midGround)
        self.menuScene.add_interface(self.menu_gameGround)
        self.menuScene.add_interface(self.menu_foreGround)
        
        # load all scene sprites here...
        logo_anim = JCSPyGm_Util.create_interface_animation(
            self.menu_midGround, 
            Game.spriteDir + "ID WorldSelect_cygnus - no name/", 
            "0_", 
            ".png", 
            32)
        
        logo_anim.camX = 175
        logo_anim.camY = 0
        logo_anim.auto_pivot()
        logo_anim.get_animation().set_time_per_frame(0.1)
        
    def init_game_scene(self):
        """Initialize the game scene."""
        
        # create one scene.
        self.gameScene = GameScene(self.player, self.camera)
        
        # create basic layer of 2d platformer game.
        self.backGround = JCSPyGm_Interface()
        self.midGround = JCSPyGm_Interface()
        self.gameGround = JCSPyGm_Interface()
        self.foreGround = JCSPyGm_Interface()
        
        self.backGround.set_friction(0.5)
        self.midGround.set_friction(0.75)
        self.gameGround.set_friction(1.0)
        self.foreGround.set_friction(1.0)
        
        self.backGround.set_name("backGround")
        self.midGround.set_name("midGround")
        self.gameGround.set_name("gameGround")
        self.foreGround.set_name("foreGround")
        
        # add all interface to the scene.
        # IMPORTANT(jenchieh): plz add the 
        # interface in correct order. 
        self.gameScene.add_interface(self.backGround)
        self.gameScene.add_interface(self.midGround)
        self.gameScene.add_interface(self.gameGround)
        self.gameScene.add_interface(self.foreGround)
        
        # load all scene sprites here...
        self.gameScene.initialize()
        
    def init_game_object(self):
        """Initialize the game object."""
        
        self.player.load_animation(Game.spriteDir + "Black Pig/", "move_", ".png", 3)
        self.player.auto_collider("circle")
        self.player.auto_pivot()
        self.player.collider.radius = 20
        
        self.player.camX = 1280 / 2
        self.player.camY = 720 / 2
        
        # add the game object to the interface.
        self.gameGround.add_game_object(self.player)
        
    def process_input(self, deltaTime):
        """"Temporary process input function."""
        
        if JCSPyGm_Input.get_key(pygame.constants.K_m):
            self.sceneManager.switch_scene_with_bgm(
                self.menuScene, Game.soundDir + "test", ".ogg")
            
        if JCSPyGm_Input.get_key(pygame.constants.K_n):
            self.sceneManager.switch_scene_with_bgm(
                self.gameScene, Game.soundDir + "test", ".ogg")
            
        # trigger debug mode.
        if JCSPyGm_Input.get_key_down(pygame.constants.K_l):
            JCSPyGm_Debug.DEBUG_MODE = not JCSPyGm_Debug.DEBUG_MODE
            
    def get_menu_scene(self):
        """Return menu scene"""
        return self.menuScene
        
    def get_game_scene(self):
        """Return the game scene."""
        return self.gameScene 
    
    def get_game_ground(self):
        return self.gameGround
    
    def switch_to_menu_scene(self):
        self.sceneManager.switch_scene_with_bgm(
            self.menuScene, Game.soundDir + "test", ".ogg")
        
    def switch_to_game_scene(self):
        self.sceneManager.switch_scene_with_bgm(
                self.gameScene, Game.soundDir + "test", ".ogg")
