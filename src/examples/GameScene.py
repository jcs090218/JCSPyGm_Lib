#  ========================================================================
#  $File: GameScene.py $
#  $Date: 2016-11-03 23:56:01 $
#  $Revision: $
#  $Creator: Jen-Chieh Shen $
#  $Notice: See LICENSE.txt for modification and distribution information
#                     Copyright (c) 2016 by Shen, Jen-Chieh $
#  ========================================================================

import pygame

from src.core.JCSPyGm_Camera import JCSPyGm_Camera
from src.core.JCSPyGm_GameObject import JCSPyGm_GameObject
from src.core.JCSPyGm_Scene import JCSPyGm_Scene
from src.util.JCSPyGm_Debug import JCSPyGm_Debug
from src.util.JCSPyGm_Input import JCSPyGm_Input
from src.util.JCSPyGm_Util import JCSPyGm_Util


class GameScene(JCSPyGm_Scene):

    """Game Scene"""

    # --------------------------------------------
    # Public Variables
    # --------------------------------------------
    spriteDir = "../../res/sprites/"
    soundDir = "../../res/sounds/"
    
    # --------------------------------------------
    # Private Variables
    # --------------------------------------------

    # --------------------------------------------
    # Protected Variables
    # --------------------------------------------

    # --------------------------------------------
    # Constructor
    # --------------------------------------------
    def __init__(self, player, camera):
        """Constructor."""
        
        super(GameScene, self).__init__()
        
        self.player = player
        self.camera = camera
        
        self.g_cloud = []

    # --------------------------------------------
    # Public Methods
    # --------------------------------------------
    def on_enable_scene(self):
        """Initialize the scene.
        
        IMPORTANT(jenchieh): this function will be call evertime 
        the scene have been loaded or switch.
        """
    
        super(GameScene, self).on_enable_scene()
        
        # reset the player.
        self.player.reset_player_position()
        JCSPyGm_Camera.get_instance().set_camera_position_xy(self.player.camX, self.player.camY)
    
    def on_disable_scene(self):
        """On Disable the scene.
        
        IMPORTANT(jenchieh): this function will be call evertime 
        the the scene is switched.
        """
        
        super(GameScene, self).on_disable_scene()
        
        # do stuff...
    
    def update(self, deltaTime):
        """Update all interface game logic."""
        
        super(GameScene, self).update(deltaTime)
        
        # do stuff...
    
    def draw(self, windowInfo):
        """Update all interface graphics"""
        
        super(GameScene, self).draw(windowInfo)
        
        # do stuff...
        
    def initialize(self):
        """Call this function only once, cuz we dont want
        to reload sprite over and over again."""
        
        super(GameScene, self).initialize()
        
        self.backGround = self.__get_interface_by_name("backGround")
        self.midGround = self.__get_interface_by_name("midGround")
        self.gameGround = self.__get_interface_by_name("gameGround")
        self.foreGround = self.__get_interface_by_name("foreGround")
        
        
        g_cloudSpeed = -10
        some = 600
        
        back_0 = JCSPyGm_Util.create_interface_sprite(
            self.backGround,
            GameScene.spriteDir + "IDvampireEU_town - no name/back_0", 
            ".png")
        back_0.camX = 640
        back_0.camY = 475 - some
        
        back_1 = JCSPyGm_Util.create_interface_sprite(
            self.backGround,
            GameScene.spriteDir + "IDvampireEU_town - no name/back_0", 
            ".png")
        back_1.camX = 640 - 575
        back_1.camY = 475 - some
        
        back_1_1 = JCSPyGm_Util.create_interface_sprite(
            self.backGround,
            GameScene.spriteDir + "IDvampireEU_town - no name/back_1",
            ".png")
        back_1_1.camX = 600
        back_1_1.camY = 400 - some
        back_1_2 = JCSPyGm_Util.create_interface_sprite(
            self.backGround,
            GameScene.spriteDir + "IDvampireEU_town - no name/back_1", 
            ".png")
        back_1_2.camX = 600 + 426
        back_1_2.camY = 400 - some
        back_1_3 = JCSPyGm_Util.create_interface_sprite(
            self.backGround,
            GameScene.spriteDir + "IDvampireEU_town - no name/back_1",
            ".png")
        back_1_3.camX = 600 - 426
        back_1_3.camY = 400 - some

        back_2_1 = JCSPyGm_Util.create_interface_sprite(
            self.backGround,
            GameScene.spriteDir + "IDvampireEU_town - no name/back_2", 
            ".png")
        back_2_1.camX = 640
        back_2_1.camY = 300 - some
        back_2_2 = JCSPyGm_Util.create_interface_sprite(
            self.backGround,
            GameScene.spriteDir + "IDvampireEU_town - no name/back_2", 
            ".png")
        back_2_2.camX = 640 - 1730
        back_2_2.camY = 300 - some
        back_2_3 = JCSPyGm_Util.create_interface_sprite(
            self.backGround,
            GameScene.spriteDir + "IDvampireEU_town - no name/back_2", 
            ".png")
        back_2_3.camX = 640 + 2000
        back_2_3.camY = 300 - some
        
        # load all scene sprites here...
        ani_5 = JCSPyGm_Util.create_interface_animation(
            self.midGround, 
            GameScene.spriteDir + "ID11thFestival - no name/", 
            "ani.5_", 
            ".png",
            5)
        
        ani_5.camX = 1000
        ani_5.camY = 200
        ani_5.get_animation().set_time_per_frame(0.8)
        
        ani0 = JCSPyGm_Util.create_interface_animation(
            self.midGround,
            GameScene.spriteDir + "IDvampireEU_town - no name/",
            "ani.0_",
            ".png",
            10)
        ani0.camX = 150
        ani0.camY = 375 - some
        ani0.get_animation().set_time_per_frame(0.5)

        back_4_1 = JCSPyGm_Util.create_interface_sprite(
            self.backGround,
            GameScene.spriteDir + "IDvampireEU_town - no name/back_4", ".png")
        back_4_1.camX = 600
        back_4_1.camY = 550 - some

        back_4_2 = JCSPyGm_Util.create_interface_sprite(
          self.backGround,
          GameScene.spriteDir + "IDvampireEU_town - no name/back_4", ".png")
        back_4_2.camX = 600 + 1780
        back_4_2.camY = 550 - some
        
        back_4_3 = JCSPyGm_Util.create_interface_sprite(
          self.backGround,
          GameScene.spriteDir + "IDvampireEU_town - no name/back_4", ".png")
        back_4_3.camX = 600 + (1780 * 2)
        back_4_3.camY = 550 - some
        
        back_4_4 = JCSPyGm_Util.create_interface_sprite(
          self.backGround,
          GameScene.spriteDir + "IDvampireEU_town - no name/back_4", ".png")
        back_4_4.camX = 600 + (-1780 * 1)
        back_4_4.camY = 550 - some

        back_5 = JCSPyGm_Util.create_interface_sprite(
            self.midGround,
            GameScene.spriteDir + "IDvampireEU_town - no name/back_5", ".png")
        back_5.camX = 100
        back_5.camY = 550 - some
        
        # Cloud
        cloud_height = -500
        
        g_clouds_1 = JCSPyGm_Util.create_interface_sprite(
            self.midGround,
            GameScene.spriteDir + "IDvampireEU_town - no name/back_6", ".png")
        g_clouds_1.camX = 2000
        g_clouds_1.camY = 300 + cloud_height
        g_clouds_1.velX = g_cloudSpeed

        g_clouds_2 = JCSPyGm_Util.create_interface_sprite(
            self.midGround,
            GameScene.spriteDir + "IDprofession - no name/back_11", ".png")
        g_clouds_2.camX = 640
        g_clouds_2.camY = -300 + cloud_height
        g_clouds_2.velX = g_cloudSpeed

        back_10 = JCSPyGm_Util.create_interface_sprite(
            self.backGround,
            GameScene.spriteDir + "IDprofession - no name/back_10", ".png")
        back_10.camX = 640
        back_10.camY = -800
        
        # tree
        
        tree_height = -387
        
        g_trees_1 = JCSPyGm_Util.create_interface_sprite(
            self.gameGround,
            GameScene.spriteDir + "ID11thFestival - no name/back_11", ".png")
        g_trees_1.camX = 1300
        g_trees_1.camY = 375 + tree_height
        
        g_trees_2 = JCSPyGm_Util.create_interface_sprite(
            self.foreGround,
            GameScene.spriteDir + "ID11thFestival - no name/back_11", ".png")
        g_trees_2.camX = 1800
        g_trees_2.camY = 500 + tree_height
        
        g_trees_3 = JCSPyGm_Util.create_interface_sprite(
            self.gameGround,
            GameScene.spriteDir + "ID11thFestival - no name/back_11", ".png")
        g_trees_3.camX = 2800
        g_trees_3.camY = 375 + tree_height

        back_17_1 = JCSPyGm_Util.create_interface_sprite(
            self.gameGround,
            GameScene.spriteDir + "ID11thFestival - no name/back_17", ".png")
        back_17_1.camX = 640
        back_17_1.camY = 590 + tree_height

        back_17_2 = JCSPyGm_Util.create_interface_sprite(
            self.gameGround,
            GameScene.spriteDir + "ID11thFestival - no name/back_17", ".png")
        back_17_2.camX = 1838
        back_17_2.camY = 590 + tree_height
        
        back_17_3 = JCSPyGm_Util.create_interface_sprite(
            self.gameGround,
            GameScene.spriteDir + "ID11thFestival - no name/back_17", ".png")
        back_17_3.camX = 640 + (1198 * 2)
        back_17_3.camY = 590 + tree_height
        
        back_17_4 = JCSPyGm_Util.create_interface_sprite(
            self.gameGround,
            GameScene.spriteDir + "ID11thFestival - no name/back_17", ".png")
        back_17_4.camX = 640 + (1198 * 3)
        back_17_4.camY = 590 + tree_height
        
        back_17_5 = JCSPyGm_Util.create_interface_sprite(
            self.gameGround,
            GameScene.spriteDir + "ID11thFestival - no name/back_17", ".png")
        back_17_5.camX = 640 - 1198
        back_17_5.camY = 590 + tree_height
        
        back_17_6 = JCSPyGm_Util.create_interface_sprite(
            self.gameGround,
            GameScene.spriteDir + "ID11thFestival - no name/back_17", ".png")
        back_17_6.camX = 640 + (1198 * 4)
        back_17_6.camY = 590 + tree_height
        
        back_17_6 = JCSPyGm_Util.create_interface_sprite(
            self.gameGround,
            GameScene.spriteDir + "ID11thFestival - no name/back_17", ".png")
        back_17_6.camX = 640 + (1198 * 5)
        back_17_6.camY = 590 + tree_height

        back_19 = JCSPyGm_Util.create_interface_sprite(
          self.gameGround,
          GameScene.spriteDir + "ID11thFestival - no name/back_19", ".png")
        back_19.camX = 1300
        back_19.camY = 590 + tree_height
      
        # Tile Map Start

        tile_height = 650
        tile_second_offset = 37
        
        self.__place_tile(30, 90, 3, 0, self.gameGround, "IDfallenLeaves - no name/enH0_0", tile_height)
        self.__place_tile(30, 90, 3, 1, self.gameGround, "IDfallenLeaves - no name/enH0_1", tile_height)
        self.__place_tile(30, 90, 3, 2, self.gameGround, "IDfallenLeaves - no name/enH0_2", tile_height)

        self.__place_tile(30, 90, 3, 0, self.gameGround, "IDfallenLeaves - no name/bsc_0", tile_height + tile_second_offset)
        self.__place_tile(30, 90, 3, 1, self.gameGround, "IDfallenLeaves - no name/bsc_1", tile_height + tile_second_offset)
        self.__place_tile(30, 90, 3, 2, self.gameGround, "IDfallenLeaves - no name/bsc_2", tile_height + tile_second_offset)

        # Create Lights
        light_height = -220
        
        g_lights_1 = JCSPyGm_Util.create_interface_animation(
            self.foreGround,
            GameScene.spriteDir + "ID11thFestival - no name/",
            "ani.2_",
            ".png",
            2)
        g_lights_1.camX = 1200
        g_lights_1.camY = 125 + light_height
        g_lights_1.get_animation().set_time_per_frame(0.1)

        # Foreground bushes
        fore_back_1 = JCSPyGm_Util.create_interface_sprite(
            self.foreGround,
            GameScene.spriteDir + "IDprofession - no name/back_1", ".png")
        fore_back_1.camX = 150
        fore_back_1.camY = -700
        
        fore_back_0_1 = JCSPyGm_Util.create_interface_sprite(
            self.foreGround,
            GameScene.spriteDir + "IDprofession - no name/back_0", ".png")
        fore_back_0_1.camX = 150 - 1150
        fore_back_0_1.camY = -700
        
        fore_back_0_2 = JCSPyGm_Util.create_interface_sprite(
            self.foreGround,
            GameScene.spriteDir + "IDprofession - no name/back_0", ".png")
        fore_back_0_2.camX = 5000 + 200
        fore_back_0_2.camY = -700

        # Platform
        enH0_0_6 = JCSPyGm_Util.create_interface_sprite(
            self.gameGround,
            GameScene.spriteDir + "IDfallenLeaves - no name/enH0_0", ".png")
        enH0_0_6.camX = 925 + (45 * 1)
        enH0_0_6.camY = 500
        enH0_0_7 = JCSPyGm_Util.create_interface_sprite(
            self.gameGround,
            GameScene.spriteDir + "IDfallenLeaves - no name/enH0_0", ".png")
        enH0_0_7.camX = 925 + (45 * 4)
        enH0_0_7.camY = 500

        enH0_1_6 = JCSPyGm_Util.create_interface_sprite(
            self.gameGround,
            GameScene.spriteDir + "IDfallenLeaves - no name/enH0_1", ".png")
        enH0_1_6.camX = 925 + (45 * 2)
        enH0_1_6.camY = 500
        enH0_1_7 = JCSPyGm_Util.create_interface_sprite(
            self.gameGround,
            GameScene.spriteDir + "IDfallenLeaves - no name/enH0_1", ".png")
        enH0_1_7.camX = 925 + (45 * 5)
        enH0_1_7.camY = 500

        enH0_2_6 = JCSPyGm_Util.create_interface_sprite(
            self.gameGround,
            GameScene.spriteDir + "IDfallenLeaves - no name/enH0_2", ".png")
        enH0_2_6.camX = 925 + (45 * 3)
        enH0_2_6.camY = 500

        enH1_0_1 = JCSPyGm_Util.create_interface_sprite(
            self.gameGround,
            GameScene.spriteDir + "IDfallenLeaves - no name/enH1_0", ".png")
        enH1_0_1.camX = 925 + (45 * 1)
        enH1_0_1.camY = 500 + 35
        enH1_0_2 = JCSPyGm_Util.create_interface_sprite(
            self.gameGround,
            GameScene.spriteDir + "IDfallenLeaves - no name/enH1_0", ".png")
        enH1_0_2.camX = 925 + (45 * 4)
        enH1_0_2.camY = 500 + 35

        enH1_1_1 = JCSPyGm_Util.create_interface_sprite(
            self.gameGround,
            GameScene.spriteDir + "IDfallenLeaves - no name/enH1_1", ".png")
        enH1_1_1.camX = 925 + (45 * 2)
        enH1_1_1.camY = 500 + 35
        enH1_1_2 = JCSPyGm_Util.create_interface_sprite(
            self.gameGround,
            GameScene.spriteDir + "IDfallenLeaves - no name/enH1_1", ".png")
        enH1_1_2.camX = 925 + (45 * 5)
        enH1_1_2.camY = 500 + 35

        enH1_2_1 = JCSPyGm_Util.create_interface_sprite(
            self.gameGround,
            GameScene.spriteDir + "IDfallenLeaves - no name/enH1_2", ".png")
        enH1_2_1.camX = 925 + (45 * 3)
        enH1_2_1.camY = 500 + 35
        
        # -----------------------------------------------
        # initialize the collider after this line.
        
        self.ground = JCSPyGm_GameObject()
        self.ground.set_collider_type("box")
        self.ground.collider.set_tag("Ground")
        self.ground.camX = -2000
        self.ground.camY = 650 + 17
        self.ground.collider.set_width(40000)
        self.ground.collider.set_height(10)
        
        obstacle = self.__create_obstacle(1200, 610)
        # flip initialize.
        obstacle.filpX = True
        obstacle.get_sprite().faceLeft = False
        
        obstacle = self.__create_obstacle(1800, 610)
        obstacle = self.__create_obstacle(2100, 610)
        obstacle = self.__create_obstacle(2400, 610)
        obstacle = self.__create_obstacle(2500, 610)
        obstacle = self.__create_obstacle(2800, 610)
        # flip initialize.
        obstacle.filpX = True
        obstacle.get_sprite().faceLeft = False
        
        obstacle = self.__create_obstacle(3200, 610)
        obstacle = self.__create_obstacle(3700, 610)
        # flip initialize.
        obstacle.filpX = True
        obstacle.get_sprite().faceLeft = False
        
        obstacle = self.__create_obstacle(4000, 610)
        obstacle = self.__create_obstacle(450, 610)
        obstacle = self.__create_obstacle(4700, 610)
        obstacle = self.__create_obstacle(5000, 610)
        obstacle = self.__create_obstacle(5100, 610)
        
        
        # add the game object to the interface.
        self.gameGround.add_game_object_as_collider(self.ground)
        
    # --------------------------------------------
    # Protected Methods
    # --------------------------------------------

    # --------------------------------------------
    # Private Methods
    # --------------------------------------------
    def __get_interface_by_name(self, interName):
        """Add the game object to the interface 
        by interface's name."""
        
        for index in range(self.get_interfaces_len()):
            inter = self.get_interface_by_index(index)
            
            if inter.is_name(interName):
                return inter
            
        JCSPyGm_Debug.Error("Failed to add game object by name...")
        
        return None

    def __place_tile(self, count, basePixel, offset, startCount, inter, spritePath, tileHeight):
        
        for index in range(count):
        
            tile = JCSPyGm_Util.create_interface_sprite(
                inter,
                GameScene.spriteDir + spritePath, ".png")
            tile.camX = (basePixel * (index * offset + startCount))
            tile.camY = tileHeight
            
    def __create_obstacle(self, xPos, yPos):
        """"""
        
        obstacle = JCSPyGm_Util.create_interface_collider_sprite(
            self.gameGround, 
            "box", 
            GameScene.spriteDir + "ID2012037 - Orbis Tower Warning Sign/stand_0", 
            ".png", 
            True)
        obstacle.camX = xPos
        obstacle.camY = yPos
        obstacle.collider.set_tag("Obstacle")
        
        obstacle.collider.set_width(40)
        obstacle.collider.set_height(60)
        
        return obstacle
        
    # --------------------------------------------
    # setter / getter
    # --------------------------------------------
